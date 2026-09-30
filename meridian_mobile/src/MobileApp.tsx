import React, { useState, useEffect, useRef } from "react";
import { DropdownNav, MobileTabMode } from "./components/mobile/DropdownNav";
import { VoiceOrbHUD } from "./components/mobile/VoiceOrbHUD";
import { LiveThoughtCarousel, ThoughtStep } from "./components/mobile/LiveThoughtCarousel";
import { QRScannerModal } from "./components/mobile/QRScannerModal";
import { ServerConnectionModal } from "./components/mobile/ServerConnectionModal";
import {
  Send,
  Mic,
  Camera,
  ShieldCheck,
  Search,
  Phone,
  RefreshCw,
  AlertTriangle,
  Check,
  X,
  Cpu,
  HardDrive,
  Activity,
  Copy,
  Sparkles,
  Server,
} from "lucide-react";

interface ChatMessage {
  id: string;
  sender: "user" | "agent";
  text: string;
  timestamp: string;
}

interface SafetyGateConfirmation {
  id: string;
  tool: string;
  args: Record<string, any>;
  tier: number;
}

export const MobileApp: React.FC = () => {
  const [activeTab, setActiveTab] = useState<MobileTabMode>("voice");
  const [isListening, setIsListening] = useState(false);
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [isRemote, setIsRemote] = useState(false);
  const [pingMs, setPingMs] = useState(12);
  const [cpuPercent, setCpuPercent] = useState(18);
  const [vramUsage, setVramUsage] = useState("4.2 GB");
  const [ramUsage, setRamUsage] = useState("8.5 GB");
  const [brainModel, setBrainModel] = useState("qwen2.5-coder:7b");
  
  const [isQRModalOpen, setIsQRModalOpen] = useState(false);
  const [isServerModalOpen, setIsServerModalOpen] = useState(false);

  const [inputText, setInputText] = useState("");
  const [backendUrl, setBackendUrl] = useState<string>("http://10.0.2.2:4132");
  const [authToken, setAuthToken] = useState<string>("");
  const [isSending, setIsSending] = useState(false);

  const [ragQuery, setRagQuery] = useState("");
  const [ragResults, setRagResults] = useState<Array<{ id: string; content: string; score?: number }>>([]);
  const [isSearchingRag, setIsSearchingRag] = useState(false);

  const [activeConfirmation, setActiveConfirmation] = useState<SafetyGateConfirmation | null>(null);

  const [thoughts, setThoughts] = useState<ThoughtStep[]>([
    { id: "1", type: "planning", text: "[System] Mobile agent engine online.", status: "completed" },
    { id: "2", type: "audit", text: "[Defense] Zero-trust security active. Port 4132 ready.", status: "completed" },
  ]);

  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: "m1",
      sender: "agent",
      text: "Meridian-X Mobile Agent online. Connected to desktop backend engine.",
      timestamp: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
    },
  ]);

  const chatBottomRef = useRef<HTMLDivElement | null>(null);

  // Auto-scroll chat on new messages
  useEffect(() => {
    chatBottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, thoughts]);

  // Load saved connection settings on mount
  useEffect(() => {
    const savedUrl = localStorage.getItem("meridian_backend_url");
    const savedToken = localStorage.getItem("meridian_auth_token");
    if (savedUrl) {
      setBackendUrl(savedUrl);
      setIsRemote(savedUrl.includes("trycloudflare.com") || (!savedUrl.includes("192.168") && !savedUrl.includes("localhost") && !savedUrl.includes("10.0.2.2")));
    }
    if (savedToken) setAuthToken(savedToken);
  }, []);

  // Poll system telemetry health & system usage endpoints
  useEffect(() => {
    let isMounted = true;
    const fetchTelemetry = async () => {
      const startTime = Date.now();
      try {
        const headers = authToken ? { Authorization: `Bearer ${authToken}` } : {};
        const [healthRes, usageRes] = await Promise.allSettled([
          fetch(`${backendUrl}/api/health`, { headers }),
          fetch(`${backendUrl}/api/system-usage`, { headers }),
        ]);

        const latency = Date.now() - startTime;
        if (isMounted) {
          if (healthRes.status === "fulfilled" && healthRes.value.ok) {
            setPingMs(latency);
            const data = await healthRes.value.json().catch(() => ({}));
            if (data.brain_model) setBrainModel(data.brain_model);
          } else {
            setPingMs(999);
          }

          if (usageRes.status === "fulfilled" && usageRes.value.ok) {
            const usageData = await usageRes.value.json().catch(() => ({}));
            if (usageData.cpu_usage !== undefined) setCpuPercent(Math.round(usageData.cpu_usage));
            if (usageData.vram_usage) setVramUsage(usageData.vram_usage);
            if (usageData.ram_usage) setRamUsage(usageData.ram_usage);
          }
        }
      } catch {
        if (isMounted) setPingMs(999);
      }
    };

    fetchTelemetry();
    const interval = setInterval(fetchTelemetry, 8000);
    return () => {
      isMounted = false;
      clearInterval(interval);
    };
  }, [backendUrl, authToken]);

  const handleSaveConnection = (newUrl: string, newToken: string) => {
    setBackendUrl(newUrl);
    setAuthToken(newToken);
    setIsRemote(newUrl.includes("trycloudflare.com") || (!newUrl.includes("192.168") && !newUrl.includes("localhost") && !newUrl.includes("10.0.2.2")));
    localStorage.setItem("meridian_backend_url", newUrl);
    localStorage.setItem("meridian_auth_token", newToken);

    setMessages((prev) => [
      ...prev,
      {
        id: `sys-${Date.now()}`,
        sender: "agent",
        text: `Backend target updated to ${newUrl}. Target endpoint ready.`,
        timestamp: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
      },
    ]);
  };

  const handlePairSuccess = (config: { localUrl: string; remoteUrl: string; token: string }) => {
    const targetUrl = config.remoteUrl || config.localUrl;
    handleSaveConnection(targetUrl, config.token);
  };

  // Real-time SSE Agent Execution Stream (/api/chat/stream)
  const handleSendMessage = async (customQuery?: string) => {
    const query = customQuery || inputText;
    if (!query.trim() || isSending) return;

    const userMsg: ChatMessage = {
      id: `u-${Date.now()}`,
      sender: "user",
      text: query,
      timestamp: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
    };

    setMessages((prev) => [...prev, userMsg]);
    if (!customQuery) setInputText("");
    setIsSending(true);

    const streamId = `a-${Date.now()}`;
    const agentMsg: ChatMessage = {
      id: streamId,
      sender: "agent",
      text: "Thinking...",
      timestamp: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
    };
    setMessages((prev) => [...prev, agentMsg]);

    try {
      const response = await fetch(`${backendUrl}/api/chat/stream`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...(authToken ? { Authorization: `Bearer ${authToken}` } : {}),
        },
        body: JSON.stringify({ message: query }),
      });

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }

      if (!response.body) {
        throw new Error("No response body received from SSE stream.");
      }

      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let streamAccumulator = "";
      let buffer = "";

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split("\n\n");
        buffer = lines.pop() || "";

        for (const block of lines) {
          const blockLines = block.split("\n");
          let eventType = "text";
          let dataText = "";

          for (const line of blockLines) {
            if (line.startsWith("event:")) {
              eventType = line.replace("event:", "").trim();
            } else if (line.startsWith("data:")) {
              dataText += line.replace("data:", "").trim();
            }
          }

          if (!dataText) continue;

          if (eventType === "thought") {
            try {
              const thoughtObj = JSON.parse(dataText);
              const stepType = (thoughtObj.type || "planning").toLowerCase() as any;
              setThoughts((prev) => [
                ...prev,
                {
                  id: `t-${Date.now()}-${Math.random()}`,
                  type: stepType === "exec" ? "execution" : stepType === "status" ? "audit" : "planning",
                  text: thoughtObj.text || JSON.stringify(thoughtObj),
                  status: "completed",
                },
              ]);
            } catch {
              setThoughts((prev) => [
                ...prev,
                { id: `t-${Date.now()}`, type: "planning", text: dataText, status: "completed" },
              ]);
            }
          } else if (eventType === "confirmation") {
            try {
              const confObj = JSON.parse(dataText);
              setActiveConfirmation({
                id: confObj.id,
                tool: confObj.tool || "Action",
                args: confObj.args || {},
                tier: confObj.tier || 2,
              });
            } catch (e) {
              console.error("Failed to parse confirmation event:", e);
            }
          } else if (eventType === "text") {
            streamAccumulator += dataText;
            setMessages((prev) =>
              prev.map((msg) => (msg.id === streamId ? { ...msg, text: streamAccumulator } : msg))
            );
          }
        }
      }

      setIsSpeaking(true);
      setTimeout(() => setIsSpeaking(false), 2500);
    } catch (err: any) {
      setMessages((prev) =>
        prev.map((msg) =>
          msg.id === streamId
            ? { ...msg, text: `⚠️ Connection Error: ${err.message || "Failed to reach Meridian backend."}` }
            : msg
        )
      );
    } finally {
      setIsSending(false);
    }
  };

  // Confirm or Reject Safety Gate Tool Action (/api/chat/confirm)
  const handleConfirmDecision = async (approved: boolean) => {
    if (!activeConfirmation) return;
    const confId = activeConfirmation.id;
    setActiveConfirmation(null);

    try {
      await fetch(`${backendUrl}/api/chat/confirm`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...(authToken ? { Authorization: `Bearer ${authToken}` } : {}),
        },
        body: JSON.stringify({ id: confId, approved }),
      });

      setThoughts((prev) => [
        ...prev,
        {
          id: `t-conf-${Date.now()}`,
          type: approved ? "audit" : "warning",
          text: approved ? `[Approved] Action execution authorized by mobile user.` : `[Rejected] Action execution denied by mobile user.`,
          status: "completed",
        },
      ]);
    } catch (err: any) {
      console.error("Failed to send confirmation decision:", err);
    }
  };

  const handleExecuteRagSearch = async () => {
    if (!ragQuery.trim()) return;
    setIsSearchingRag(true);
    try {
      const res = await fetch(`${backendUrl}/api/memory/search`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...(authToken ? { Authorization: `Bearer ${authToken}` } : {}),
        },
        body: JSON.stringify({ query: ragQuery }),
      });
      if (res.ok) {
        const data = await res.json();
        setRagResults(data.results || data.memories || []);
      } else {
        setRagResults([{ id: "err", content: `Search returned HTTP ${res.status}` }]);
      }
    } catch (err: any) {
      setRagResults([{ id: "err", content: `Failed to search RAG memory: ${err.message}` }]);
    } finally {
      setIsSearchingRag(false);
    }
  };

  const quickActions = [
    { label: "Security Audit", icon: ShieldCheck, query: "Run full security audit on codebase" },
    { label: "Call Logs", icon: Phone, query: "Check recent AI receptionist call logs" },
    { label: "RAG Vector Memory", icon: Search, query: "Search Turbovec knowledge base for project specs" },
    { label: "Camera Vision", icon: Camera, query: "Analyze current camera view" },
  ];

  return (
    <div className="flex flex-col h-screen w-screen bg-[#080C14] text-white font-sans overflow-hidden select-none">
      <DropdownNav
        activeTab={activeTab}
        onSelectTab={setActiveTab}
        isRemote={isRemote}
        pingMs={pingMs}
        cpuPercent={cpuPercent}
        onOpenQRScanner={() => setIsQRModalOpen(true)}
        onOpenServerModal={() => setIsServerModalOpen(true)}
      />

      <div className="flex-1 flex flex-col overflow-y-auto px-4 py-2 space-y-3">
        {activeTab === "voice" && (
          <>
            <VoiceOrbHUD
              isListening={isListening}
              isSpeaking={isSpeaking}
              audioLevel={isListening ? 0.7 : isSpeaking ? 0.8 : 0.2}
              onToggleListening={() => setIsListening(!isListening)}
              statusText={
                isSending
                  ? "ReAct streaming active..."
                  : isSpeaking
                  ? "Agent Speaking..."
                  : isListening
                  ? "Listening (VAD Active)..."
                  : "Tap Orb or type command"
              }
            />

            <LiveThoughtCarousel thoughts={thoughts} />

            <div className="flex items-center gap-2 overflow-x-auto py-1 no-scrollbar">
              {quickActions.map((action, i) => {
                const Icon = action.icon;
                return (
                  <button
                    key={i}
                    onClick={() => handleSendMessage(action.query)}
                    className="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-white/5 border border-white/10 hover:border-cyan-400/50 text-[11px] text-slate-300 hover:text-white whitespace-nowrap shrink-0 transition-all active:scale-95 shadow-md"
                  >
                    <Icon className="w-3.5 h-3.5 text-cyan-400" />
                    <span>{action.label}</span>
                  </button>
                );
              })}
            </div>

            <div className="flex-1 space-y-3 my-2">
              {messages.map((msg) => (
                <div
                  key={msg.id}
                  className={`flex flex-col ${msg.sender === "user" ? "items-end" : "items-start"}`}
                >
                  <div
                    className={`max-w-[88%] px-4 py-3 rounded-2xl text-xs leading-relaxed shadow-xl ${
                      msg.sender === "user"
                        ? "bg-gradient-to-r from-cyan-600 to-purple-600 text-white rounded-br-none shadow-cyan-600/20"
                        : "bg-[#0D1322]/95 border border-white/10 text-slate-200 backdrop-blur-xl rounded-bl-none shadow-black/40"
                    }`}
                  >
                    <p className="whitespace-pre-wrap font-sans">{msg.text}</p>
                  </div>
                  <span className="text-[10px] text-slate-500 px-1 mt-0.5 font-mono">{msg.timestamp}</span>
                </div>
              ))}

              {/* Safety Gate Confirmation Card */}
              {activeConfirmation && (
                <div className="p-4 rounded-2xl bg-amber-500/10 border border-amber-500/40 text-xs space-y-3 shadow-2xl animate-in zoom-in-95 duration-200">
                  <div className="flex items-center gap-2 text-amber-400 font-bold uppercase tracking-wider text-[11px]">
                    <AlertTriangle className="w-4 h-4 animate-bounce" />
                    <span>Security Confirmation Gate (Tier {activeConfirmation.tier})</span>
                  </div>
                  <p className="text-slate-200 leading-snug">
                    Agent requested tool execution:{" "}
                    <span className="font-mono text-cyan-300 font-semibold">{activeConfirmation.tool}</span>
                  </p>
                  {Object.keys(activeConfirmation.args).length > 0 && (
                    <pre className="p-2.5 rounded-xl bg-black/40 border border-white/10 text-[10px] text-slate-300 font-mono overflow-x-auto">
                      {JSON.stringify(activeConfirmation.args, null, 2)}
                    </pre>
                  )}
                  <div className="flex items-center gap-2 pt-1">
                    <button
                      onClick={() => handleConfirmDecision(true)}
                      className="flex-1 flex items-center justify-center gap-1.5 py-2 rounded-xl bg-emerald-600 text-white font-medium text-xs shadow-lg shadow-emerald-600/20 active:scale-95 transition-all"
                    >
                      <Check className="w-4 h-4" />
                      <span>Approve</span>
                    </button>
                    <button
                      onClick={() => handleConfirmDecision(false)}
                      className="flex-1 flex items-center justify-center gap-1.5 py-2 rounded-xl bg-rose-600/80 hover:bg-rose-600 text-white font-medium text-xs shadow-lg active:scale-95 transition-all"
                    >
                      <X className="w-4 h-4" />
                      <span>Reject</span>
                    </button>
                  </div>
                </div>
              )}

              <div ref={chatBottomRef} />
            </div>
          </>
        )}

        {activeTab === "vision" && (
          <div className="flex-1 flex flex-col items-center justify-center p-6 text-center space-y-4">
            <div className="p-4 rounded-3xl bg-purple-500/10 border border-purple-500/30 text-purple-400 animate-pulse">
              <Camera className="w-12 h-12" />
            </div>
            <h3 className="text-base font-bold text-white">Camera Vision Mode</h3>
            <p className="text-xs text-slate-400 max-w-xs">
              Point phone camera at physical screens, whiteboards, or components for Moondream / Gemini vision context.
            </p>
            <button
              onClick={() => handleSendMessage("Analyze current camera vision snapshot for text and objects")}
              className="px-5 py-2.5 rounded-xl bg-gradient-to-r from-purple-600 to-cyan-600 text-white text-xs font-medium shadow-lg shadow-purple-600/30 active:scale-95 transition-all"
            >
              Analyze Snapshot
            </button>
          </div>
        )}

        {activeTab === "metrics" && (
          <div className="flex-1 space-y-3 py-2">
            <div className="flex items-center justify-between">
              <h3 className="text-xs font-bold uppercase tracking-wider text-slate-400">Desktop Hardware Telemetry</h3>
              <button
                onClick={() => setIsServerModalOpen(true)}
                className="text-[10px] text-cyan-400 hover:underline flex items-center gap-1"
              >
                <Server className="w-3 h-3" />
                <span>Change Server</span>
              </button>
            </div>
            <div className="grid grid-cols-2 gap-2.5">
              <div className="p-3 rounded-2xl bg-white/5 border border-white/10 space-y-1">
                <div className="flex items-center gap-1.5 text-slate-400 text-[10px]">
                  <Cpu className="w-3 h-3 text-cyan-400" />
                  <span>CPU Load</span>
                </div>
                <span className="text-lg font-mono font-bold text-cyan-400">{cpuPercent}%</span>
              </div>
              <div className="p-3 rounded-2xl bg-white/5 border border-white/10 space-y-1">
                <div className="flex items-center gap-1.5 text-slate-400 text-[10px]">
                  <Activity className="w-3 h-3 text-purple-400" />
                  <span>GPU VRAM</span>
                </div>
                <span className="text-lg font-mono font-bold text-purple-400">{vramUsage}</span>
              </div>
              <div className="p-3 rounded-2xl bg-white/5 border border-white/10 space-y-1">
                <div className="flex items-center gap-1.5 text-slate-400 text-[10px]">
                  <HardDrive className="w-3 h-3 text-emerald-400" />
                  <span>System RAM</span>
                </div>
                <span className="text-lg font-mono font-bold text-emerald-400">{ramUsage}</span>
              </div>
              <div className="p-3 rounded-2xl bg-white/5 border border-white/10 space-y-1">
                <div className="flex items-center gap-1.5 text-slate-400 text-[10px]">
                  <Sparkles className="w-3 h-3 text-amber-400" />
                  <span>Brain Model</span>
                </div>
                <span className="text-xs font-mono font-bold text-amber-300 truncate block">{brainModel}</span>
              </div>
            </div>
            <div className="p-3.5 rounded-2xl bg-white/5 border border-white/10 space-y-1.5">
              <span className="text-[10px] text-slate-400 block uppercase font-semibold">Active Backend URL</span>
              <span className="text-xs font-mono text-cyan-300 block truncate">{backendUrl}</span>
            </div>
          </div>
        )}

        {activeTab === "rag" && (
          <div className="flex-1 space-y-3 py-2">
            <h3 className="text-xs font-bold uppercase tracking-wider text-slate-400">Turbovec Vector RAG Search</h3>
            <div className="relative flex items-center gap-2">
              <input
                type="text"
                value={ragQuery}
                onChange={(e) => setRagQuery(e.target.value)}
                onKeyDown={(e) => e.key === "Enter" && handleExecuteRagSearch()}
                placeholder="Query project context & vector memory..."
                className="flex-1 px-3.5 py-2.5 rounded-xl bg-white/5 border border-white/10 text-xs text-white focus:outline-none focus:border-cyan-500"
              />
              <button
                onClick={handleExecuteRagSearch}
                disabled={isSearchingRag}
                className="p-2.5 rounded-xl bg-cyan-600 text-white hover:bg-cyan-500 transition-all"
              >
                {isSearchingRag ? <RefreshCw className="w-4 h-4 animate-spin" /> : <Search className="w-4 h-4" />}
              </button>
            </div>

            <div className="space-y-2 mt-3">
              {ragResults.map((res) => (
                <div key={res.id} className="p-3 rounded-xl bg-white/5 border border-white/10 text-xs space-y-1">
                  <p className="text-slate-200 font-mono">{res.content}</p>
                  {res.score !== undefined && (
                    <span className="text-[10px] text-cyan-400 font-mono block">Score: {res.score.toFixed(4)}</span>
                  )}
                </div>
              ))}
            </div>
          </div>
        )}
      </div>

      <div className="p-3 bg-[#0D1322]/95 border-t border-white/10 backdrop-blur-xl flex items-center gap-2">
        <button
          onClick={() => setIsListening(!isListening)}
          className={`p-2.5 rounded-xl transition-all ${
            isListening ? "bg-purple-600 text-white animate-pulse" : "bg-white/5 text-slate-400 hover:text-white"
          }`}
        >
          <Mic className="w-4 h-4" />
        </button>

        <input
          type="text"
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSendMessage()}
          placeholder="Command Meridian-X agent..."
          className="flex-1 bg-white/5 border border-white/10 rounded-xl px-3.5 py-2.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-cyan-500/60"
        />

        <button
          onClick={() => handleSendMessage()}
          disabled={isSending}
          className="p-2.5 rounded-xl bg-gradient-to-tr from-cyan-500 to-purple-600 text-white active:scale-95 transition-all shadow-md shadow-cyan-500/20 disabled:opacity-50"
        >
          {isSending ? <RefreshCw className="w-4 h-4 animate-spin" /> : <Send className="w-4 h-4" />}
        </button>
      </div>

      <ServerConnectionModal
        isOpen={isServerModalOpen}
        onClose={() => setIsServerModalOpen(false)}
        currentBackendUrl={backendUrl}
        currentAuthToken={authToken}
        onSaveConfig={handleSaveConnection}
        onOpenQRScanner={() => {
          setIsServerModalOpen(false);
          setIsQRModalOpen(true);
        }}
      />

      <QRScannerModal
        isOpen={isQRModalOpen}
        onClose={() => setIsQRModalOpen(false)}
        onPairSuccess={handlePairSuccess}
      />
    </div>
  );
};

export default MobileApp;

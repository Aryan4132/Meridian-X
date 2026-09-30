import React, { useState } from "react";
import { DropdownNav, MobileTabMode } from "./components/mobile/DropdownNav";
import { VoiceOrbHUD } from "./components/mobile/VoiceOrbHUD";
import { LiveThoughtCarousel, ThoughtStep } from "./components/mobile/LiveThoughtCarousel";
import { QRScannerModal } from "./components/mobile/QRScannerModal";
import { Send, Mic, Camera, Sparkles, Activity, ShieldCheck, Search, FileText, Phone, Play } from "lucide-react";

interface ChatMessage {
  id: string;
  sender: "user" | "agent";
  text: string;
  timestamp: string;
}

export const MobileApp: React.FC = () => {
  const [activeTab, setActiveTab] = useState<MobileTabMode>("voice");
  const [isListening, setIsListening] = useState(false);
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [isRemote, setIsRemote] = useState(false);
  const [pingMs, setPingMs] = useState(12);
  const [cpuPercent, setCpuPercent] = useState(18);
  const [isQRModalOpen, setIsQRModalOpen] = useState(false);
  const [inputText, setInputText] = useState("");

  // Sample thought steps for HUD stream
  const [thoughts, setThoughts] = useState<ThoughtStep[]>([
    { id: "1", type: "planning", text: "[Self-Questioning] Verified target codebase paths and dependencies.", status: "completed" },
    { id: "2", type: "audit", text: "[Security Audit] Execution of tool 'search_web' approved.", status: "completed" },
    { id: "3", type: "execution", text: "[Consensus Debate] Running Coder vs QA Reviewer verification loop...", status: "running" },
  ]);

  // Sample chat message stream
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: "m1",
      sender: "agent",
      text: "System initialized. Connected to Meridian-X backend engine. All anti-hallucination guardrails active.",
      timestamp: "23:40",
    },
  ]);

  const handleSendMessage = () => {
    if (!inputText.trim()) return;
    const userMsg: ChatMessage = {
      id: `u-${Date.now()}`,
      sender: "user",
      text: inputText,
      timestamp: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
    };

    setMessages((prev) => [...prev, userMsg]);
    setInputText("");

    // Simulate agent response
    setTimeout(() => {
      setIsSpeaking(true);
      const agentMsg: ChatMessage = {
        id: `a-${Date.now()}`,
        sender: "agent",
        text: `Received: "${userMsg.text}". Verified logic against system context.`,
        timestamp: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
      };
      setMessages((prev) => [...prev, agentMsg]);
      setTimeout(() => setIsSpeaking(false), 2000);
    }, 1000);
  };

  const handlePairSuccess = (config: { localUrl: string; remoteUrl: string; token: string }) => {
    setIsRemote(true);
    setPingMs(42);
    setMessages((prev) => [
      ...prev,
      {
        id: `sys-${Date.now()}`,
        sender: "agent",
        text: `Successfully paired with Desktop Backend at ${config.remoteUrl}! E2E encrypted session active.`,
        timestamp: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
      },
    ]);
  };

  const quickActions = [
    { label: "Run Security Audit", icon: ShieldCheck, query: "Run full security audit on codebase" },
    { label: "Screen Active Calls", icon: Phone, query: "Check recent phone receptionist call logs" },
    { label: "Search RAG Memory", icon: Search, query: "Search Turbovec knowledge base for project specs" },
    { label: "Camera Vision Scan", icon: Camera, query: "Analyze current camera view" },
  ];

  return (
    <div className="flex flex-col h-screen w-screen bg-[#080C14] text-white font-sans overflow-hidden select-none">
      {/* Top Header Dropdown Navigation */}
      <DropdownNav
        activeTab={activeTab}
        onSelectTab={setActiveTab}
        isRemote={isRemote}
        pingMs={pingMs}
        cpuPercent={cpuPercent}
        onOpenQRScanner={() => setIsQRModalOpen(true)}
      />

      {/* Main View Router Content */}
      <div className="flex-1 flex flex-col overflow-y-auto px-4 py-2 space-y-3">
        {activeTab === "voice" && (
          <>
            {/* Interactive Voice Visualizer Orb HUD */}
            <VoiceOrbHUD
              isListening={isListening}
              isSpeaking={isSpeaking}
              audioLevel={isListening ? 0.7 : isSpeaking ? 0.8 : 0.2}
              onToggleListening={() => setIsListening(!isListening)}
              statusText={isSpeaking ? "Agent Speaking..." : isListening ? "Listening (VAD Active)..." : "Tap Orb or speak prompt"}
            />

            {/* Micro-Animated Thought Carousel */}
            <LiveThoughtCarousel thoughts={thoughts} />

            {/* Quick Action Chips */}
            <div className="flex items-center gap-2 overflow-x-auto py-1 no-scrollbar">
              {quickActions.map((action, i) => {
                const Icon = action.icon;
                return (
                  <button
                    key={i}
                    onClick={() => {
                      setInputText(action.query);
                    }}
                    className="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-white/5 border border-white/10 hover:border-cyan-400/50 text-[11px] text-slate-300 hover:text-white whitespace-nowrap shrink-0 transition-all active:scale-95 shadow-md"
                  >
                    <Icon className="w-3.5 h-3.5 text-cyan-400" />
                    <span>{action.label}</span>
                  </button>
                );
              })}
            </div>

            {/* Agent Chat Message Stream */}
            <div className="flex-1 space-y-2.5 my-2">
              {messages.map((msg) => (
                <div
                  key={msg.id}
                  className={`flex flex-col ${msg.sender === "user" ? "items-end" : "items-start"}`}
                >
                  <div
                    className={`max-w-[85%] px-4 py-2.5 rounded-2xl text-xs leading-relaxed shadow-lg ${
                      msg.sender === "user"
                        ? "bg-gradient-to-r from-cyan-600 to-purple-600 text-white rounded-br-none"
                        : "bg-[#111827]/90 border border-white/10 text-slate-200 backdrop-blur-xl rounded-bl-none"
                    }`}
                  >
                    <p>{msg.text}</p>
                  </div>
                  <span className="text-[10px] text-slate-400 px-1 mt-0.5">{msg.timestamp}</span>
                </div>
              ))}
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
              Point camera at physical objects, whiteboards, or screen logs for Moondream / Gemini vision analysis.
            </p>
            <button className="px-5 py-2.5 rounded-xl bg-purple-600 text-white text-xs font-medium shadow-lg shadow-purple-600/30 active:scale-95 transition-all">
              Capture Snapshot
            </button>
          </div>
        )}

        {activeTab === "metrics" && (
          <div className="flex-1 space-y-3 py-2">
            <h3 className="text-xs font-bold uppercase tracking-wider text-slate-400">Desktop Hardware Telemetry</h3>
            <div className="grid grid-cols-2 gap-2.5">
              <div className="p-3 rounded-2xl bg-white/5 border border-white/10">
                <span className="text-[10px] text-slate-400 block">CPU Usage</span>
                <span className="text-base font-mono font-bold text-cyan-400">{cpuPercent}%</span>
              </div>
              <div className="p-3 rounded-2xl bg-white/5 border border-white/10">
                <span className="text-[10px] text-slate-400 block">GPU VRAM</span>
                <span className="text-base font-mono font-bold text-purple-400">4.2 GB / 12 GB</span>
              </div>
              <div className="p-3 rounded-2xl bg-white/5 border border-white/10">
                <span className="text-[10px] text-slate-400 block">Active Ping</span>
                <span className="text-base font-mono font-bold text-emerald-400">{pingMs} ms</span>
              </div>
              <div className="p-3 rounded-2xl bg-white/5 border border-white/10">
                <span className="text-[10px] text-slate-400 block">Anti-Hallucination</span>
                <span className="text-base font-mono font-bold text-amber-400">ACTIVE</span>
              </div>
            </div>
          </div>
        )}

        {activeTab === "rag" && (
          <div className="flex-1 space-y-3 py-2">
            <h3 className="text-xs font-bold uppercase tracking-wider text-slate-400">Turbovec Vector RAG Search</h3>
            <div className="relative">
              <input
                type="text"
                placeholder="Query project context & vector memory..."
                className="w-full px-3.5 py-2.5 rounded-xl bg-white/5 border border-white/10 text-xs text-white focus:outline-none focus:border-cyan-500"
              />
              <Search className="w-4 h-4 text-slate-400 absolute right-3 top-3" />
            </div>
          </div>
        )}
      </div>

      {/* Bottom Voice & Text Input Bar */}
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
          className="flex-1 bg-white/5 border border-white/10 rounded-xl px-3.5 py-2 text-xs text-white placeholder-slate-400 focus:outline-none focus:border-cyan-500/60"
        />

        <button
          onClick={handleSendMessage}
          className="p-2.5 rounded-xl bg-gradient-to-tr from-cyan-500 to-purple-600 text-white active:scale-95 transition-all shadow-md shadow-cyan-500/20"
        >
          <Send className="w-4 h-4" />
        </button>
      </div>

      {/* QR Pairing Modal */}
      <QRScannerModal
        isOpen={isQRModalOpen}
        onClose={() => setIsQRModalOpen(false)}
        onPairSuccess={handlePairSuccess}
      />
    </div>
  );
};

import React, { useState } from "react";
import { Mic, Eye, Activity, Search, QrCode, Shield, Sparkles, ChevronDown, Check, Wifi, Cloud } from "lucide-react";

export type MobileTabMode = "voice" | "vision" | "metrics" | "rag" | "settings";

interface DropdownNavProps {
  activeTab: MobileTabMode;
  onSelectTab: (tab: MobileTabMode) => void;
  isRemote: boolean;
  pingMs: number;
  cpuPercent: number;
  onOpenQRScanner: () => void;
}

export const DropdownNav: React.FC<DropdownNavProps> = ({
  activeTab,
  onSelectTab,
  isRemote,
  pingMs,
  cpuPercent,
  onOpenQRScanner,
}) => {
  const [isOpen, setIsOpen] = useState(false);

  const menuItems = [
    { id: "voice" as MobileTabMode, label: "Voice Agent Mode", icon: Mic, color: "text-cyan-400" },
    { id: "vision" as MobileTabMode, label: "Camera Vision Mode", icon: Eye, color: "text-purple-400" },
    { id: "metrics" as MobileTabMode, label: "Telemetry & System", icon: Activity, color: "text-emerald-400" },
    { id: "rag" as MobileTabMode, label: "RAG Memory Search", icon: Search, color: "text-amber-400" },
  ];

  const currentItem = menuItems.find((item) => item.id === activeTab) || menuItems[0];

  return (
    <div className="relative w-full z-50">
      {/* Header Top Bar */}
      <div className="flex items-center justify-between px-4 py-3 bg-[#0D1322]/90 backdrop-blur-xl border-b border-white/10 shadow-2xl">
        {/* Brand & Connection Badge */}
        <div className="flex items-center gap-2.5">
          <div className="w-8 h-8 rounded-lg bg-gradient-to-tr from-cyan-500 to-purple-600 p-[1px] flex items-center justify-center shadow-lg shadow-cyan-500/20">
            <div className="w-full h-full bg-[#080C14] rounded-[7px] flex items-center justify-center">
              <Sparkles className="w-4 h-4 text-cyan-400 animate-pulse" />
            </div>
          </div>
          <div>
            <span className="text-sm font-bold tracking-wider text-white font-sans bg-clip-text text-transparent bg-gradient-to-r from-white via-slate-200 to-cyan-400">
              MERIDIAN-X
            </span>
            <div className="flex items-center gap-1.5 text-[10px] text-slate-400">
              <span className={`w-1.5 h-1.5 rounded-full ${isRemote ? "bg-amber-400 animate-ping" : "bg-emerald-400 animate-pulse"}`} />
              <span className="flex items-center gap-1">
                {isRemote ? <Cloud className="w-2.5 h-2.5 text-amber-400" /> : <Wifi className="w-2.5 h-2.5 text-emerald-400" />}
                {isRemote ? "Remote Tunnel" : "Local Wi-Fi"} • {pingMs}ms
              </span>
            </div>
          </div>
        </div>

        {/* Status Pill & Dropdown Toggle */}
        <div className="flex items-center gap-2">
          <div className="hidden xs:flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-white/5 border border-white/10 text-[11px] text-slate-300">
            <span className="text-slate-400">CPU</span>
            <span className="font-mono font-semibold text-cyan-400">{cpuPercent}%</span>
          </div>

          <button
            onClick={() => setIsOpen(!isOpen)}
            className="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-gradient-to-r from-cyan-500/10 to-purple-500/10 border border-cyan-500/30 hover:border-cyan-400/60 text-white text-xs font-medium transition-all duration-200 active:scale-95 shadow-lg shadow-cyan-500/10"
          >
            <currentItem.icon className={`w-4 h-4 ${currentItem.color}`} />
            <span className="hidden sm:inline">{currentItem.label}</span>
            <ChevronDown className={`w-3.5 h-3.5 text-slate-400 transition-transform duration-300 ${isOpen ? "rotate-180 text-cyan-400" : ""}`} />
          </button>
        </div>
      </div>

      {/* Dropdown Menu Overlay */}
      {isOpen && (
        <>
          <div className="fixed inset-0 bg-black/60 backdrop-blur-sm z-40" onClick={() => setIsOpen(false)} />
          <div className="absolute top-full left-2 right-2 mt-2 bg-[#0D1322]/95 backdrop-blur-2xl border border-cyan-500/30 rounded-2xl p-2.5 shadow-2xl shadow-cyan-950/80 z-50 animate-in fade-in slide-in-from-top-3 duration-200">
            <div className="text-[10px] uppercase font-semibold text-slate-400 px-3 py-1.5 tracking-wider">
              Navigation Mode
            </div>
            
            <div className="space-y-1">
              {menuItems.map((item) => {
                const Icon = item.icon;
                const isSelected = activeTab === item.id;
                return (
                  <button
                    key={item.id}
                    onClick={() => {
                      onSelectTab(item.id);
                      setIsOpen(false);
                    }}
                    className={`w-full flex items-center justify-between px-3 py-2.5 rounded-xl text-xs transition-all duration-200 ${
                      isSelected
                        ? "bg-gradient-to-r from-cyan-500/20 to-purple-500/20 text-white font-medium border border-cyan-500/30"
                        : "text-slate-300 hover:bg-white/5 hover:text-white"
                    }`}
                  >
                    <div className="flex items-center gap-2.5">
                      <div className={`p-1.5 rounded-lg ${isSelected ? "bg-cyan-500/20" : "bg-white/5"}`}>
                        <Icon className={`w-4 h-4 ${item.color}`} />
                      </div>
                      <span>{item.label}</span>
                    </div>
                    {isSelected && <Check className="w-4 h-4 text-cyan-400" />}
                  </button>
                );
              })}
            </div>

            <div className="my-2 border-t border-white/10" />

            {/* QR Pairing Trigger */}
            <button
              onClick={() => {
                onOpenQRScanner();
                setIsOpen(false);
              }}
              className="w-full flex items-center justify-between px-3 py-2.5 rounded-xl text-xs bg-gradient-to-r from-purple-600/20 to-cyan-600/20 border border-purple-500/30 text-purple-200 hover:text-white transition-all duration-200"
            >
              <div className="flex items-center gap-2.5">
                <QrCode className="w-4 h-4 text-purple-400" />
                <span>Pair Desktop (QR Code)</span>
              </div>
              <Shield className="w-3.5 h-3.5 text-purple-400" />
            </button>
          </div>
        </>
      )}
    </div>
  );
};

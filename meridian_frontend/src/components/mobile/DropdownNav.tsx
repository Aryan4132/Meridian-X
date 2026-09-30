import React, { useState } from "react";
import { Mic, Eye, Activity, Search, Shield, Sparkles, ChevronDown, Check, Wifi, Cloud } from "lucide-react";

export type MobileTabMode = "voice" | "vision" | "metrics" | "rag" | "settings";

interface DropdownNavProps {
  activeTab: MobileTabMode;
  onSelectTab: (tab: MobileTabMode) => void;
  isRemote: boolean;
  pingMs: number;
  cpuPercent: number;
}

export const DropdownNav: React.FC<DropdownNavProps> = ({
  activeTab,
  onSelectTab,
  isRemote,
  pingMs,
  cpuPercent,
}) => {
  const [isOpen, setIsOpen] = useState(false);

  const menuItems = [
    { id: "voice" as MobileTabMode, label: "Voice Agent Mode", icon: Mic, color: "text-[var(--accent)]" },
    { id: "vision" as MobileTabMode, label: "Camera Vision Mode", icon: Eye, color: "text-[var(--accent-2)]" },
    { id: "metrics" as MobileTabMode, label: "Telemetry & System", icon: Activity, color: "text-[var(--success)]" },
    { id: "rag" as MobileTabMode, label: "RAG Memory Search", icon: Search, color: "text-[var(--warning)]" },
  ];

  const currentItem = menuItems.find((item) => item.id === activeTab) || menuItems[0];

  return (
    <div className="relative w-full z-50">
      {/* Header Top Bar */}
      <div className="flex items-center justify-between px-4 py-3 bg-[var(--bg-panel)] backdrop-blur-xl border-b border-[var(--border-subtle)] shadow-2xl">
        {/* Brand & Connection Badge */}
        <div className="flex items-center gap-2.5">
          <div className="w-8 h-8 rounded-lg bg-[var(--accent)] p-[1px] flex items-center justify-center shadow-lg">
            <div className="w-full h-full bg-[var(--bg-void)] rounded-[7px] flex items-center justify-center">
              <Sparkles className="w-4 h-4 text-[var(--accent)] animate-pulse" />
            </div>
          </div>
          <div>
            <span className="text-sm font-bold tracking-wider text-[var(--text-bright)]">
              MERIDIAN-X
            </span>
            <div className="flex items-center gap-1.5 text-[10px] text-[var(--text-dim)]">
              <span className={`w-1.5 h-1.5 rounded-full ${isRemote ? "bg-[var(--warning)] animate-ping" : "bg-[var(--success)] animate-pulse"}`} />
              <span className="flex items-center gap-1">
                {isRemote ? <Cloud className="w-2.5 h-2.5 text-[var(--warning)]" /> : <Wifi className="w-2.5 h-2.5 text-[var(--success)]" />}
                {isRemote ? "Remote Tunnel" : "Local Wi-Fi"} • {pingMs}ms
              </span>
            </div>
          </div>
        </div>

        {/* Status Pill & Dropdown Toggle */}
        <div className="flex items-center gap-2">
          <div className="hidden xs:flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-[var(--bg-surface)] border border-[var(--border-subtle)] text-[11px] text-[var(--text-main)]">
            <span className="text-[var(--text-dim)]">CPU</span>
            <span className="font-mono font-semibold text-[var(--accent)]">{cpuPercent}%</span>
          </div>

          <button
            onClick={() => setIsOpen(!isOpen)}
            className="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-[var(--bg-surface)] border border-[var(--border-active)] text-[var(--text-bright)] text-xs font-medium transition-all duration-200 active:scale-95 shadow-lg"
          >
            <currentItem.icon className={`w-4 h-4 ${currentItem.color}`} />
            <span className="hidden sm:inline">{currentItem.label}</span>
            <ChevronDown className={`w-3.5 h-3.5 text-[var(--text-dim)] transition-transform duration-300 ${isOpen ? "rotate-180 text-[var(--accent)]" : ""}`} />
          </button>
        </div>
      </div>

      {/* Dropdown Menu Overlay */}
      {isOpen && (
        <>
          <div className="fixed inset-0 bg-[var(--bg-void)]/60 backdrop-blur-sm z-40" onClick={() => setIsOpen(false)} />
          <div className="absolute top-full left-2 right-2 mt-2 bg-[var(--bg-float)] backdrop-blur-2xl border border-[var(--border-active)] rounded-2xl p-2.5 shadow-2xl z-50 animate-in fade-in slide-in-from-top-3 duration-200">
            <div className="text-[10px] uppercase font-semibold text-[var(--text-dim)] px-3 py-1.5 tracking-wider">
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
                        ? "bg-[var(--accent-muted)] text-[var(--text-bright)] font-medium border border-[var(--border-active)]"
                        : "text-[var(--text-main)] hover:bg-[var(--bg-surface)] hover:text-[var(--text-bright)]"
                    }`}
                  >
                    <div className="flex items-center gap-2.5">
                      <div className={`p-1.5 rounded-lg ${isSelected ? "bg-[var(--accent-muted)]" : "bg-[var(--bg-surface)]"}`}>
                        <Icon className={`w-4 h-4 ${item.color}`} />
                      </div>
                      <span>{item.label}</span>
                    </div>
                    {isSelected && <Check className="w-4 h-4 text-[var(--accent)]" />}
                  </button>
                );
              })}
            </div>

          </div>
        </>
      )}
    </div>
  );
};

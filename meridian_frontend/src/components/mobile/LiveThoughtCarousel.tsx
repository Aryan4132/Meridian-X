import React, { useState } from "react";
import { Brain, ChevronLeft, ChevronRight, CheckCircle2, AlertTriangle, Cpu, Terminal } from "lucide-react";

export interface ThoughtStep {
  id: string;
  type: "planning" | "warning" | "execution" | "audit";
  text: string;
  status: "running" | "completed" | "failed";
}

interface LiveThoughtCarouselProps {
  thoughts: ThoughtStep[];
}

export const LiveThoughtCarousel: React.FC<LiveThoughtCarouselProps> = ({ thoughts }) => {
  const [activeIndex, setActiveIndex] = useState(0);

  if (!thoughts || thoughts.length === 0) {
    return (
      <div className="mx-4 my-2 p-3 rounded-2xl bg-[var(--bg-surface)] border border-[var(--border-subtle)] backdrop-blur-xl flex items-center justify-between text-xs text-[var(--text-dim)] font-mono">
        <div className="flex items-center gap-2">
          <Brain className="w-4 h-4 text-[var(--accent)] animate-pulse" />
          <span>[Agent Ready] System standby. Awaiting input.</span>
        </div>
        <span className="text-[10px] text-[var(--text-dim)]">0 steps</span>
      </div>
    );
  }

  const current = thoughts[activeIndex] || thoughts[thoughts.length - 1];

  const getStepIcon = (type: ThoughtStep["type"]) => {
    switch (type) {
      case "planning":
        return <Brain className="w-4 h-4 text-[var(--accent-2)]" />;
      case "warning":
        return <AlertTriangle className="w-4 h-4 text-[var(--warning)]" />;
      case "execution":
        return <Terminal className="w-4 h-4 text-[var(--accent)]" />;
      case "audit":
        return <Cpu className="w-4 h-4 text-[var(--success)]" />;
      default:
        return <Brain className="w-4 h-4 text-[var(--accent)]" />;
    }
  };

  return (
    <div className="mx-4 my-2 p-3 rounded-2xl bg-[var(--bg-panel)] border border-[var(--border-active)] backdrop-blur-xl shadow-xl transition-all duration-300">
      <div className="flex items-center justify-between mb-1.5">
        <div className="flex items-center gap-2">
          <span className="p-1 rounded-lg bg-[var(--accent-muted)] border border-[var(--border-active)]">
            {getStepIcon(current.type)}
          </span>
          <span className="text-[11px] font-bold tracking-wider uppercase text-[var(--accent)]">
            Live Thought Stream
          </span>
        </div>

        {/* Counter Navigation Controls */}
        <div className="flex items-center gap-1.5 text-xs text-[var(--text-dim)]">
          <button
            disabled={activeIndex === 0}
            onClick={() => setActiveIndex((prev) => Math.max(0, prev - 1))}
            className="p-1 rounded-md hover:bg-[var(--bg-hover)] disabled:opacity-30 disabled:hover:bg-transparent text-[var(--text-main)] transition-colors"
          >
            <ChevronLeft className="w-3.5 h-3.5" />
          </button>
          <span className="font-mono text-[10px] text-[var(--text-main)]">
            {activeIndex + 1} / {thoughts.length}
          </span>
          <button
            disabled={activeIndex === thoughts.length - 1}
            onClick={() => setActiveIndex((prev) => Math.min(thoughts.length - 1, prev + 1))}
            className="p-1 rounded-md hover:bg-[var(--bg-hover)] disabled:opacity-30 disabled:hover:bg-transparent text-[var(--text-main)] transition-colors"
          >
            <ChevronRight className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>

      {/* Thought Content Body */}
      <div className="flex items-start justify-between gap-2">
        <p className="text-xs font-mono text-[var(--text-main)] line-clamp-2 leading-relaxed">
          {current.text}
        </p>
        {current.status === "completed" ? (
          <CheckCircle2 className="w-4 h-4 text-[var(--success)] shrink-0 mt-0.5" />
        ) : (
          <span className="w-3 h-3 rounded-full bg-[var(--accent)] animate-ping shrink-0 mt-1" />
        )}
      </div>
    </div>
  );
};

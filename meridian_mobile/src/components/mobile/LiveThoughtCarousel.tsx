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
      <div className="mx-4 my-2 p-3 rounded-2xl bg-white/[0.03] border border-white/10 backdrop-blur-xl flex items-center justify-between text-xs text-slate-400 font-mono">
        <div className="flex items-center gap-2">
          <Brain className="w-4 h-4 text-cyan-400 animate-pulse" />
          <span>[Agent Ready] System standby. Awaiting input.</span>
        </div>
        <span className="text-[10px] text-slate-400">0 steps</span>
      </div>
    );
  }

  const current = thoughts[activeIndex] || thoughts[thoughts.length - 1];

  const getStepIcon = (type: ThoughtStep["type"]) => {
    switch (type) {
      case "planning":
        return <Brain className="w-4 h-4 text-purple-400" />;
      case "warning":
        return <AlertTriangle className="w-4 h-4 text-amber-400" />;
      case "execution":
        return <Terminal className="w-4 h-4 text-cyan-400" />;
      case "audit":
        return <Cpu className="w-4 h-4 text-emerald-400" />;
      default:
        return <Brain className="w-4 h-4 text-cyan-400" />;
    }
  };

  return (
    <div className="mx-4 my-2 p-3 rounded-2xl bg-gradient-to-r from-cyan-950/40 via-[#0D1322]/80 to-purple-950/40 border border-cyan-500/20 backdrop-blur-xl shadow-xl transition-all duration-300">
      <div className="flex items-center justify-between mb-1.5">
        <div className="flex items-center gap-2">
          <span className="p-1 rounded-lg bg-cyan-500/10 border border-cyan-500/30">
            {getStepIcon(current.type)}
          </span>
          <span className="text-[11px] font-bold tracking-wider uppercase text-cyan-300 font-sans">
            Live Thought Stream
          </span>
        </div>

        <div className="flex items-center gap-1.5 text-xs text-slate-400">
          <button
            disabled={activeIndex === 0}
            onClick={() => setActiveIndex((prev) => Math.max(0, prev - 1))}
            className="p-1 rounded-md hover:bg-white/10 disabled:opacity-30 disabled:hover:bg-transparent text-slate-300 transition-colors"
          >
            <ChevronLeft className="w-3.5 h-3.5" />
          </button>
          <span className="font-mono text-[10px] text-slate-300">
            {activeIndex + 1} / {thoughts.length}
          </span>
          <button
            disabled={activeIndex === thoughts.length - 1}
            onClick={() => setActiveIndex((prev) => Math.min(thoughts.length - 1, prev + 1))}
            className="p-1 rounded-md hover:bg-white/10 disabled:opacity-30 disabled:hover:bg-transparent text-slate-300 transition-colors"
          >
            <ChevronRight className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>

      <div className="flex items-start justify-between gap-2">
        <p className="text-xs font-mono text-slate-200 line-clamp-2 leading-relaxed">
          {current.text}
        </p>
        {current.status === "completed" ? (
          <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
        ) : (
          <span className="w-3 h-3 rounded-full bg-cyan-400 animate-ping shrink-0 mt-1" />
        )}
      </div>
    </div>
  );
};

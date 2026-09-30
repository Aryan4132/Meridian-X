import React, { useEffect, useRef } from "react";
import { Mic, MicOff, Volume2 } from "lucide-react";

interface VoiceOrbHUDProps {
  isListening: boolean;
  isSpeaking: boolean;
  audioLevel?: number; // 0.0 to 1.0
  onToggleListening: () => void;
  statusText?: string;
}

export const VoiceOrbHUD: React.FC<VoiceOrbHUDProps> = ({
  isListening,
  isSpeaking,
  audioLevel = 0.4,
  onToggleListening,
  statusText = "Listening for prompt...",
}) => {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    let animationFrameId: number;
    let time = 0;

    const render = () => {
      time += 0.05;
      const width = canvas.width;
      const height = canvas.height;
      const centerX = width / 2;
      const centerY = height / 2;

      ctx.clearRect(0, 0, width, height);

      // Base radius with dynamic audio scaling
      const baseRadius = 42 + Math.sin(time * 2) * 4 + audioLevel * 25;

      // Outer Pulsing Neon Rings
      const ringGradients = [
        { radius: baseRadius * 1.6, color: "rgba(0, 242, 254, 0.15)" },
        { radius: baseRadius * 1.3, color: "rgba(127, 0, 255, 0.25)" },
        { radius: baseRadius * 1.1, color: "rgba(0, 230, 118, 0.35)" },
      ];

      ringGradients.forEach((ring) => {
        ctx.beginPath();
        ctx.arc(centerX, centerY, ring.radius, 0, Math.PI * 2);
        ctx.fillStyle = ring.color;
        ctx.fill();
      });

      // Core Orb Radial Gradient
      const gradient = ctx.createRadialGradient(
        centerX - baseRadius * 0.3,
        centerY - baseRadius * 0.3,
        baseRadius * 0.1,
        centerX,
        centerY,
        baseRadius
      );

      if (isSpeaking) {
        gradient.addColorStop(0, "#00f2fe");
        gradient.addColorStop(0.5, "#4facfe");
        gradient.addColorStop(1, "#000000");
      } else if (isListening) {
        gradient.addColorStop(0, "#a855f7");
        gradient.addColorStop(0.5, "#7e22ce");
        gradient.addColorStop(1, "#090d16");
      } else {
        gradient.addColorStop(0, "#64748b");
        gradient.addColorStop(0.7, "#1e293b");
        gradient.addColorStop(1, "#0f172a");
      }

      ctx.beginPath();
      ctx.arc(centerX, centerY, baseRadius, 0, Math.PI * 2);
      ctx.fillStyle = gradient;
      ctx.shadowColor = isSpeaking ? "#00f2fe" : isListening ? "#a855f7" : "transparent";
      ctx.shadowBlur = 30;
      ctx.fill();

      // Dynamic Audio Wave Ring Nodes
      const nodes = 12;
      ctx.beginPath();
      for (let i = 0; i < nodes; i++) {
        const angle = (i / nodes) * Math.PI * 2;
        const wave = Math.sin(time * 3 + i) * (audioLevel * 12 + 3);
        const r = baseRadius + wave;
        const x = centerX + Math.cos(angle) * r;
        const y = centerY + Math.sin(angle) * r;

        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.closePath();
      ctx.strokeStyle = isSpeaking ? "rgba(0, 242, 254, 0.8)" : "rgba(168, 85, 247, 0.8)";
      ctx.lineWidth = 2;
      ctx.stroke();

      animationFrameId = requestAnimationFrame(render);
    };

    render();

    return () => {
      cancelAnimationFrame(animationFrameId);
    };
  }, [isListening, isSpeaking, audioLevel]);

  return (
    <div className="flex flex-col items-center justify-center p-4 my-2">
      {/* 3D Visualizer Canvas Orb */}
      <div className="relative flex items-center justify-center cursor-pointer group" onClick={onToggleListening}>
        <canvas ref={canvasRef} width={220} height={220} className="w-[180px] h-[180px] sm:w-[220px] sm:h-[220px]" />
        <div className="absolute inset-0 flex items-center justify-center pointer-events-none">
          <div className="p-3.5 rounded-full bg-[var(--bg-void)]/60 backdrop-blur-md border border-[var(--border-subtle)] shadow-xl group-hover:scale-110 transition-transform duration-300">
            {isSpeaking ? (
              <Volume2 className="w-6 h-6 text-[var(--accent)] animate-bounce" />
            ) : isListening ? (
              <Mic className="w-6 h-6 text-[var(--accent-2)] animate-pulse" />
            ) : (
              <MicOff className="w-6 h-6 text-[var(--text-dim)]" />
            )}
          </div>
        </div>
      </div>

      {/* Dynamic Status Text Badge */}
      <div className="mt-1 px-4 py-1.5 rounded-full bg-[var(--bg-surface)] border border-[var(--border-subtle)] backdrop-blur-md text-xs font-mono text-[var(--text-main)] flex items-center gap-2 shadow-lg">
        <span
          className={`w-2 h-2 rounded-full ${
            isSpeaking ? "bg-[var(--accent)] animate-ping" : isListening ? "bg-[var(--accent-2)] animate-pulse" : "bg-[var(--text-ghost)]"
          }`}
        />
        <span>{statusText}</span>
      </div>
    </div>
  );
};

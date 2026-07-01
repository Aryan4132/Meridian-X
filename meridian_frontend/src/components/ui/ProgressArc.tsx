import React from 'react';

interface ProgressArcProps {
  value: number;
  max?: number;
  size?: number;
  strokeWidth?: number;
  label?: string;
  color?: string;
  trackColor?: string;
  animated?: boolean;
  className?: string;
}

export default function ProgressArc({
  value, max = 100, size = 160, strokeWidth = 8,
  label, color = 'var(--accent)', trackColor = 'var(--bg-surface)',
  animated = false, className = '',
}: ProgressArcProps) {
  const r = (size - strokeWidth) / 2;
  const cx = size / 2;
  const cy = size / 2;
  const circumference = 2 * Math.PI * r;
  const pct = Math.min(1, Math.max(0, value / max));
  const offset = circumference * (1 - pct);

  return (
    <div className={`relative inline-flex items-center justify-center ${className}`} style={{ width: size, height: size }}>
      {/* Pulse ring (animated) */}
      {animated && value > 0 && (
        <div
          className="absolute rounded-full animate-pulse-ring"
          style={{
            width: size - strokeWidth * 2,
            height: size - strokeWidth * 2,
            border: `1px solid ${color}`,
            opacity: 0.4,
          }}
        />
      )}

      <svg width={size} height={size} style={{ transform: 'rotate(-90deg)' }}>
        {/* Track */}
        <circle
          cx={cx} cy={cy} r={r}
          fill="none"
          stroke={trackColor}
          strokeWidth={strokeWidth}
        />
        {/* Arc */}
        <circle
          cx={cx} cy={cy} r={r}
          fill="none"
          stroke={color}
          strokeWidth={strokeWidth}
          strokeLinecap="round"
          strokeDasharray={circumference}
          strokeDashoffset={offset}
          style={{ transition: 'stroke-dashoffset 0.8s ease' }}
        />
      </svg>

      {/* Center content */}
      <div className="absolute inset-0 flex flex-col items-center justify-center">
        <span style={{
          fontSize: size < 100 ? '14px' : '22px',
          fontWeight: 700,
          color: 'var(--text-bright)',
          fontFamily: "'JetBrains Mono', monospace",
          lineHeight: 1,
        }}>
          {max !== 100
            // Timer mode (e.g. Pomodoro): format as MM:SS
            ? `${Math.floor(value / 60).toString().padStart(2, '0')}:${Math.floor(value % 60).toString().padStart(2, '0')}`
            // Percentage mode (CPU, RAM, etc.): always show as X%
            : `${Math.round(value)}%`}
        </span>
        {label && (
          <span style={{ fontSize: '9px', color: 'var(--text-dim)', marginTop: 2, fontFamily: "'JetBrains Mono', monospace", textTransform: 'uppercase', letterSpacing: '0.08em' }}>
            {label}
          </span>
        )}
      </div>
    </div>
  );
}

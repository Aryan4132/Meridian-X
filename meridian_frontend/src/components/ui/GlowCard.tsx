import React from 'react';

interface GlowCardProps {
  children: React.ReactNode;
  glow?: 'accent' | 'danger' | 'warning' | 'success' | 'none';
  hover?: boolean;
  className?: string;
  onClick?: () => void;
  style?: React.CSSProperties;
}

const glowColors: Record<string, string> = {
  accent:  'var(--accent)',
  danger:  'var(--danger)',
  warning: 'var(--warning)',
  success: 'var(--success)',
  none:    'transparent',
};

export default function GlowCard({ children, glow = 'none', hover = false, className = '', onClick, style }: GlowCardProps) {
  // NOTE: cannot append alpha hex to var(--...) — use color-mix instead.
  const glowStyle: React.CSSProperties = glow !== 'none' ? {
    borderColor: `color-mix(in srgb, ${glowColors[glow]} 35%, transparent)`,
    borderLeftColor: `color-mix(in srgb, ${glowColors[glow]} 65%, transparent)`,
  } : {};

  return (
    <div
      onClick={onClick}
      className={`glass ${hover ? 'glass-hover' : ''} ${onClick ? 'cursor-pointer' : ''} ${className}`}
      style={{ ...glowStyle, ...style }}
    >
      {children}
    </div>
  );
}

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
  const glowStyle: React.CSSProperties = glow !== 'none' ? {
    boxShadow: `0 0 0 1px ${glowColors[glow]}22, 0 0 24px ${glowColors[glow]}10`,
    borderColor: `${glowColors[glow]}33`,
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

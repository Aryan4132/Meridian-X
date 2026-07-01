import React from 'react';

interface DataBadgeProps {
  label?: string;
  value: string | number;
  color?: 'accent' | 'accent-2' | 'success' | 'danger' | 'warning' | 'dim';
  className?: string;
}

const colorMap: Record<string, string> = {
  accent:   'var(--accent)',
  'accent-2': 'var(--accent-2)',
  success:  'var(--success)',
  danger:   'var(--danger)',
  warning:  'var(--warning)',
  dim:      'var(--text-dim)',
};

export default function DataBadge({ label, value, color = 'dim', className = '' }: DataBadgeProps) {
  const c = colorMap[color];
  return (
    <span
      className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold ${className}`}
      style={{
        background: `${c}14`,
        color: c,
        border: `1px solid ${c}28`,
        fontFamily: "'JetBrains Mono', monospace",
        letterSpacing: '0.02em',
      }}
    >
      {label && <span style={{ color: `${c}99` }}>{label}</span>}
      {value}
    </span>
  );
}

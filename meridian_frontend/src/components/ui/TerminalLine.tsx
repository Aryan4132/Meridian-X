import React from 'react';

type LineType = 'system' | 'coder' | 'auditor' | 'qa' | 'consensus' | 'error' | 'ok' | 'dim';

interface TerminalLineProps {
  text: string;
  type?: LineType;
  delay?: number;
  prefix?: string;
  key?: React.Key;
}

const typeColors: Record<LineType, string> = {
  system:    'var(--text-dim)',
  coder:     'var(--success)',
  auditor:   'var(--warning)',
  qa:        '#60A5FA',
  consensus: 'var(--accent)',
  error:     'var(--danger)',
  ok:        'var(--success)',
  dim:       'var(--text-ghost)',
};

const typePrefixes: Partial<Record<LineType, string>> = {
  coder:     '[CODER]',
  auditor:   '[AUDITOR]',
  qa:        '[QA]',
  consensus: '──── CONSENSUS ────',
};

export default function TerminalLine({ text, type = 'system', delay = 0, prefix }: TerminalLineProps) {
  const color = typeColors[type];
  const auto = typePrefixes[type];
  const pfx = prefix ?? auto;

  return (
    <div
      className="animate-data-pulse text-[11px] leading-relaxed py-0.5"
      style={{
        color,
        animationDelay: `${delay}ms`,
        fontFamily: "'JetBrains Mono', monospace",
        opacity: 0,
        animationFillMode: 'forwards',
      }}
    >
      {pfx && (
        <span className="mr-2 opacity-70 font-semibold">{pfx}</span>
      )}
      {text}
    </div>
  );
}

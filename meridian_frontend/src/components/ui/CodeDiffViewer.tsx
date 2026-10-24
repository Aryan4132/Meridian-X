import React, { useState } from 'react';
import { Copy, Check, FileCode, ChevronDown, ChevronRight } from 'lucide-react';

interface CodeDiffViewerProps {
  diffText: string;
  filePath?: string;
  initialCollapsed?: boolean;
}

interface DiffLine {
  type: 'addition' | 'deletion' | 'header' | 'context';
  content: string;
  oldLineNumber?: number;
  newLineNumber?: number;
}

export const CodeDiffViewer: React.FC<CodeDiffViewerProps> = ({
  diffText,
  filePath,
  initialCollapsed = false
}) => {
  const [collapsed, setCollapsed] = useState(initialCollapsed);
  const [copied, setCopied] = useState(false);

  const lines = diffText.split('\n');
  let detectedPath = filePath;
  const parsedLines: DiffLine[] = [];

  let oldCounter = 1;
  let newCounter = 1;

  for (const line of lines) {
    if (line.startsWith('diff --git')) {
      const match = line.match(/b\/(.*)$/);
      if (match && !detectedPath) {
        detectedPath = match[1];
      }
      parsedLines.push({ type: 'header', content: line });
    } else if (line.startsWith('---') || line.startsWith('+++')) {
      parsedLines.push({ type: 'header', content: line });
    } else if (line.startsWith('@@')) {
      const match = line.match(/@@ -(\d+)(?:,\d+)? \+(\d+)(?:,\d+)? @@/);
      if (match) {
        oldCounter = parseInt(match[1], 10);
        newCounter = parseInt(match[2], 10);
      }
      parsedLines.push({ type: 'header', content: line });
    } else if (line.startsWith('+')) {
      parsedLines.push({
        type: 'addition',
        content: line.slice(1),
        newLineNumber: newCounter++
      });
    } else if (line.startsWith('-')) {
      parsedLines.push({
        type: 'deletion',
        content: line.slice(1),
        oldLineNumber: oldCounter++
      });
    } else {
      parsedLines.push({
        type: 'context',
        content: line.startsWith(' ') ? line.slice(1) : line,
        oldLineNumber: oldCounter++,
        newLineNumber: newCounter++
      });
    }
  }

  const handleCopy = () => {
    navigator.clipboard.writeText(diffText);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const additions = parsedLines.filter(l => l.type === 'addition').length;
  const deletions = parsedLines.filter(l => l.type === 'deletion').length;

  return (
    <div style={{
      margin: '10px 0',
      borderRadius: '8px',
      border: '1px solid var(--border-subtle)',
      background: 'rgba(10, 12, 16, 0.75)',
      backdropFilter: 'blur(12px)',
      overflow: 'hidden',
      fontFamily: "'JetBrains Mono', 'Fira Code', monospace"
    }}>
      {/* Diff Header */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: '6px 12px',
        background: 'rgba(255, 255, 255, 0.03)',
        borderBottom: collapsed ? 'none' : '1px solid var(--border-subtle)',
        fontSize: '11px',
      }}>
        <button
          type="button"
          onClick={() => setCollapsed(v => !v)}
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 6,
            background: 'none',
            border: 'none',
            color: 'var(--text-main, #e2e8f0)',
            cursor: 'pointer',
            padding: 0,
            fontWeight: 600,
          }}
        >
          {collapsed ? <ChevronRight size={13} /> : <ChevronDown size={13} />}
          <FileCode size={13} style={{ color: 'var(--accent, #6366f1)' }} />
          <span>{detectedPath || 'Code Modifications'}</span>
          <span style={{
            display: 'inline-flex',
            gap: 6,
            marginLeft: 8,
            fontSize: '10px'
          }}>
            <span style={{ color: '#10b981' }}>+{additions}</span>
            <span style={{ color: '#ef4444' }}>-{deletions}</span>
          </span>
        </button>

        <button
          type="button"
          onClick={handleCopy}
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 4,
            background: 'rgba(255, 255, 255, 0.05)',
            border: '1px solid var(--border-subtle)',
            borderRadius: '4px',
            color: copied ? '#10b981' : 'var(--text-dim, #94a3b8)',
            padding: '3px 8px',
            cursor: 'pointer',
            fontSize: '10px',
            transition: 'all 0.15s ease'
          }}
        >
          {copied ? <Check size={11} /> : <Copy size={11} />}
          <span>{copied ? 'Copied' : 'Copy Diff'}</span>
        </button>
      </div>

      {/* Diff Lines Body */}
      {!collapsed && (
        <div style={{
          overflowX: 'auto',
          fontSize: '11px',
          lineHeight: '1.45',
          padding: '4px 0'
        }}>
          {parsedLines.map((line, idx) => {
            let bg = 'transparent';
            let textColor = 'var(--text-dim, #94a3b8)';
            let sign = ' ';

            if (line.type === 'addition') {
              bg = 'rgba(16, 185, 129, 0.12)';
              textColor = '#34d399';
              sign = '+';
            } else if (line.type === 'deletion') {
              bg = 'rgba(239, 68, 68, 0.12)';
              textColor = '#f87171';
              sign = '-';
            } else if (line.type === 'header') {
              bg = 'rgba(99, 102, 241, 0.08)';
              textColor = '#818cf8';
              sign = ' ';
            }

            return (
              <div
                key={idx}
                style={{
                  display: 'flex',
                  background: bg,
                  padding: '1px 8px',
                  whiteSpace: 'pre',
                }}
              >
                {/* Old Line Number */}
                <span style={{
                  width: '32px',
                  userSelect: 'none',
                  textAlign: 'right',
                  paddingRight: '6px',
                  color: 'rgba(255, 255, 255, 0.2)',
                  fontSize: '10px'
                }}>
                  {line.oldLineNumber || ''}
                </span>

                {/* New Line Number */}
                <span style={{
                  width: '32px',
                  userSelect: 'none',
                  textAlign: 'right',
                  paddingRight: '8px',
                  color: 'rgba(255, 255, 255, 0.2)',
                  fontSize: '10px'
                }}>
                  {line.newLineNumber || ''}
                </span>

                {/* Sign Indicator (+ / -) */}
                <span style={{
                  width: '14px',
                  userSelect: 'none',
                  textAlign: 'center',
                  fontWeight: 700,
                  color: textColor
                }}>
                  {sign}
                </span>

                {/* Code Content */}
                <span style={{ color: textColor, flex: 1 }}>
                  {line.content}
                </span>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};

export default CodeDiffViewer;

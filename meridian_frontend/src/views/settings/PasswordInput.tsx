import React, { useState } from 'react';
import { Eye, EyeOff } from 'lucide-react';

export interface PasswordInputProps {
  label: string;
  value: string;
  onChange: (v: string) => void;
  placeholder: string;
  requireUnlock?: boolean;
  keysUnlocked?: boolean;
  onRequestUnlock?: () => void;
}

export default function PasswordInput({
  label,
  value,
  onChange,
  placeholder,
  requireUnlock,
  keysUnlocked,
  onRequestUnlock,
}: PasswordInputProps) {
  const [show, setShow] = useState(false);
  const locked = requireUnlock && !keysUnlocked;
  return (
    <div>
      <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
        {label} {locked && <span style={{ color: 'var(--accent)' }}>· 🔒</span>}
      </label>
      <div style={{ position: 'relative' }}>
        <input
          type={show && !locked ? 'text' : 'password'}
          value={locked && value ? '••••••••••••••••' : value}
          onChange={e => { if (!locked) onChange(e.target.value); }}
          placeholder={placeholder}
          className="input-base"
          style={{ paddingRight: 36 }}
          readOnly={locked}
          onFocus={e => { if (locked) { e.target.blur(); onRequestUnlock?.(); } }}
        />
        <button
          type="button"
          onClick={() => {
            if (locked) { onRequestUnlock?.(); return; }
            setShow(v => !v);
          }}
          title={locked ? 'Enter password to reveal' : (show ? 'Hide' : 'Show')}
          style={{
            position: 'absolute', right: 8, top: '50%', transform: 'translateY(-50%)',
            background: 'none', border: 'none', cursor: 'pointer', color: 'var(--text-dim)', padding: 2,
          }}
        >
          {show && !locked ? <EyeOff size={14} /> : <Eye size={14} />}
        </button>
      </div>
    </div>
  );
}

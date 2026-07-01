import React from 'react';
import { Loader2 } from 'lucide-react';

interface HoloButtonProps {
  children: React.ReactNode;
  variant?: 'primary' | 'ghost' | 'danger' | 'icon';
  size?: 'sm' | 'md' | 'lg';
  loading?: boolean;
  disabled?: boolean;
  onClick?: (e: React.MouseEvent<HTMLButtonElement>) => void;
  type?: 'button' | 'submit';
  className?: string;
  title?: string;
}

const sizeClasses = {
  sm: 'px-3 py-1.5 text-xs',
  md: 'px-4 py-2 text-sm',
  lg: 'px-6 py-3 text-base',
  icon: 'p-2',
};

export default function HoloButton({
  children, variant = 'primary', size = 'md',
  loading, disabled, onClick, type = 'button', className = '', title
}: HoloButtonProps) {
  const base = 'inline-flex items-center gap-2 font-semibold rounded-[var(--radius-sm)] transition-all duration-150 select-none whitespace-nowrap';

  if (variant === 'primary') {
    return (
      <button
        type={type}
        onClick={onClick}
        disabled={disabled || loading}
        title={title}
        className={`btn-primary ${sizeClasses[size]} ${base} ${className}`}
      >
        {loading ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> : null}
        {children}
      </button>
    );
  }

  if (variant === 'ghost') {
    return (
      <button
        type={type}
        onClick={onClick}
        disabled={disabled || loading}
        title={title}
        className={`btn-ghost ${size === 'sm' ? 'px-3 py-1.5 text-xs' : size === 'lg' ? 'px-6 py-3 text-base' : 'px-4 py-2 text-sm'} ${base} ${className}`}
      >
        {loading ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> : null}
        {children}
      </button>
    );
  }

  if (variant === 'danger') {
    return (
      <button
        type={type}
        onClick={onClick}
        disabled={disabled || loading}
        title={title}
        className={`btn-danger ${sizeClasses[size]} ${base} ${className}`}
      >
        {loading ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> : null}
        {children}
      </button>
    );
  }

  // icon variant
  return (
    <button
      type={type}
      onClick={onClick}
      disabled={disabled || loading}
      title={title}
      className={`p-2 rounded-[var(--radius-sm)] text-[var(--text-dim)] hover:text-[var(--text-main)] hover:bg-[var(--bg-surface)] transition-all duration-150 ${className}`}
    >
      {loading ? <Loader2 className="w-4 h-4 animate-spin" /> : children}
    </button>
  );
}

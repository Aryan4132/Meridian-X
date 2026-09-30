import React from 'react';

interface ProfileHeaderProps {
  className?: string;
  children?: React.ReactNode;
}

export default function ProfileHeader({ className = '', children }: ProfileHeaderProps) {
  return (
    <div className={`p-4 rounded-xl glass-card ${className}`}>
      <h3 className="text-lg font-semibold text-white">ProfileHeader</h3>
      {children}
    </div>
  );
}

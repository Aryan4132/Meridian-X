import { useState, useEffect, useCallback } from 'react';

/**
 * Hook for managing tab visibility lifecycle.
 * Allows components to unmount heavy subtrees or pause high-frequency timers when tab is hidden.
 */
export function useTabLifecycle() {
  const [isTabActive, setIsTabActive] = useState<boolean>(!document.hidden);

  useEffect(() => {
    const handleVisibilityChange = () => {
      setIsTabActive(!document.hidden);
    };

    document.addEventListener('visibilitychange', handleVisibilityChange);
    return () => {
      document.removeEventListener('visibilitychange', handleVisibilityChange);
    };
  }, []);

  return isTabActive;
}

/**
 * Low-RAM Performance Mode Hook.
 * Toggles low-RAM styling class on root element to strip blurs, shadows, and heavy animations.
 */
export function useLowRamMode() {
  const [isLowRam, setIsLowRam] = useState<boolean>(() => {
    return localStorage.getItem('meridian_low_ram_mode') === 'true';
  });

  const toggleLowRamMode = useCallback((enable?: boolean) => {
    setIsLowRam((prev) => {
      const next = enable !== undefined ? enable : !prev;
      localStorage.setItem('meridian_low_ram_mode', String(next));
      if (next) {
        document.documentElement.classList.add('low-ram-mode');
      } else {
        document.documentElement.classList.remove('low-ram-mode');
      }
      return next;
    });
  }, []);

  useEffect(() => {
    if (isLowRam) {
      document.documentElement.classList.add('low-ram-mode');
    } else {
      document.documentElement.classList.remove('low-ram-mode');
    }
  }, [isLowRam]);

  return { isLowRam, toggleLowRamMode };
}


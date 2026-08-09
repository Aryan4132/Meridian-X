import { useState, useEffect, useCallback, useRef } from 'react';

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
 * Garbage collection manager for Blob URLs.
 * Automatically revokes created Blob URLs when component unmounts or explicitly requested.
 */
export function useBlobGC() {
  const activeBlobs = useRef<Set<string>>(new Set());

  const createManagedBlobUrl = useCallback((blob: Blob): string => {
    const url = URL.createObjectURL(blob);
    activeBlobs.current.add(url);
    return url;
  }, []);

  const revokeBlobUrl = useCallback((url: string) => {
    if (activeBlobs.current.has(url)) {
      URL.revokeObjectURL(url);
      activeBlobs.current.delete(url);
    }
  }, []);

  useEffect(() => {
    const blobs = activeBlobs.current;
    return () => {
      blobs.forEach((url) => {
        URL.revokeObjectURL(url);
      });
      blobs.clear();
    };
  }, []);

  return { createManagedBlobUrl, revokeBlobUrl };
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

/**
 * Virtualized list helper hook for rendering ultra-large item collections with low RAM footprint.
 */
export function useVirtualList<T>({
  items,
  itemHeight,
  containerHeight,
  scrollTop,
  overscan = 3,
}: {
  items: T[];
  itemHeight: number;
  containerHeight: number;
  scrollTop: number;
  overscan?: number;
}) {
  const totalHeight = items.length * itemHeight;
  const startIndex = Math.max(0, Math.floor(scrollTop / itemHeight) - overscan);
  const endIndex = Math.min(
    items.length,
    Math.ceil((scrollTop + containerHeight) / itemHeight) + overscan
  );

  const visibleItems = items.slice(startIndex, endIndex).map((item, index) => ({
    item,
    index: startIndex + index,
    top: (startIndex + index) * itemHeight,
  }));

  return {
    totalHeight,
    startIndex,
    endIndex,
    visibleItems,
  };
}

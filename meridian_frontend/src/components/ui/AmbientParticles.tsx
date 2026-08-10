import React, { useEffect, useRef } from 'react';
import { useLowRamMode } from '../../hooks/useMemoryOptimizer';

export default function AmbientParticles() {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const { isLowRam } = useLowRamMode();

  useEffect(() => {
    if (isLowRam) return;

    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let animId: number;
    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    const handleResize = () => {
      if (!canvas) return;
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    };

    window.addEventListener('resize', handleResize);

    // Particle pool
    const particleCount = Math.min(35, Math.floor((width * height) / 35000));
    const particles = Array.from({ length: particleCount }, () => ({
      x: Math.random() * width,
      y: Math.random() * height,
      vx: (Math.random() - 0.5) * 0.4,
      vy: (Math.random() - 0.5) * 0.4,
      radius: Math.random() * 1.8 + 0.8,
      alpha: Math.random() * 0.4 + 0.15,
    }));

    const getAccentColor = () => {
      const style = getComputedStyle(document.documentElement);
      const accent = style.getPropertyValue('--accent').trim() || '#E8A020';
      return accent;
    };

    let accentHex = getAccentColor();

    // Listen for theme changes to update color
    const onThemeChanged = () => {
      accentHex = getAccentColor();
    };
    window.addEventListener('meridian-theme-changed', onThemeChanged);

    const render = () => {
      ctx.clearRect(0, 0, width, height);

      // Draw particles & links
      for (let i = 0; i < particles.length; i++) {
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;

        if (p.x < 0) p.x = width;
        if (p.x > width) p.x = 0;
        if (p.y < 0) p.y = height;
        if (p.y > height) p.y = 0;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = accentHex;
        ctx.globalAlpha = p.alpha * 0.4;
        ctx.fill();

        // Connect nearby particles
        for (let j = i + 1; j < particles.length; j++) {
          const p2 = particles[j];
          const dx = p.x - p2.x;
          const dy = p.y - p2.y;
          const dist = Math.sqrt(dx * dx + dy * dy);

          if (dist < 110) {
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.strokeStyle = accentHex;
            ctx.globalAlpha = (1 - dist / 110) * 0.08;
            ctx.lineWidth = 0.8;
            ctx.stroke();
          }
        }
      }

      ctx.globalAlpha = 1;
      animId = requestAnimationFrame(render);
    };

    render();

    return () => {
      window.removeEventListener('resize', handleResize);
      window.removeEventListener('meridian-theme-changed', onThemeChanged);
      cancelAnimationFrame(animId);
    };
  }, [isLowRam]);

  if (isLowRam) return null;

  return (
    <canvas
      ref={canvasRef}
      style={{
        position: 'fixed',
        inset: 0,
        pointerEvents: 'none',
        zIndex: 0,
        opacity: 0.85,
      }}
    />
  );
}

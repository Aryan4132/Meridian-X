import React, { useEffect, useRef, useState } from 'react';
import * as THREE from 'three';
import { animate } from 'animejs';

const resolveColor = (colorStr?: string): string => {
  if (colorStr && !colorStr.startsWith('var(')) return colorStr;
  return '#3B82F6';
};

interface Mascot3DCharacterProps {
  state?: string;
  accentColor?: string;
  speechAmplitude?: number;
  size?: number;
  onClick?: () => void;
}

export const Mascot3DCharacter: React.FC<Mascot3DCharacterProps> = ({
  state = 'idle',
  accentColor = '#F59E0B',
  speechAmplitude = 0,
  size = 56,
  onClick,
}) => {
  const mountRef = useRef<HTMLDivElement>(null);
  const mainGroupRef = useRef<THREE.Group | null>(null);
  const coreMeshRef = useRef<THREE.Mesh | null>(null);
  const innerRingRef = useRef<THREE.Mesh | null>(null);
  const outerRingRef = useRef<THREE.Mesh | null>(null);
  const particlesRef = useRef<THREE.Points | null>(null);
  
  const [isSpinning, setIsSpinning] = useState(false);
  const resolvedAccent = resolveColor(accentColor);

  useEffect(() => {
    const container = mountRef.current;
    if (!container) return;

    // 1. Scene & Camera Setup
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 1000);
    camera.position.z = 4.2;

    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    renderer.setSize(size, size);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    container.appendChild(renderer.domElement);

    const mainGroup = new THREE.Group();
    scene.add(mainGroup);
    mainGroupRef.current = mainGroup;

    // 2. Lighting (Soft Warm Ambient Light, No Metallic Glare)
    const ambientLight = new THREE.AmbientLight(0xffffff, 1.2);
    scene.add(ambientLight);

    const pointLight = new THREE.PointLight(
      new THREE.Color(resolvedAccent),
      1.6,
      10
    );
    pointLight.position.set(2, 3, 4);
    scene.add(pointLight);

    // 3. Central Core Mesh (Tactile Satin/Ceramic AI Orb - Non Metallic)
    const coreGeo = new THREE.IcosahedronGeometry(0.85, 2);
    const coreMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color('#161B22'),
      emissive: new THREE.Color(resolvedAccent),
      emissiveIntensity: 0.4,
      wireframe: state === 'diagnostic',
      roughness: 0.75, // Non-metallic satin finish
      metalness: 0.05, // Zero metallic sheen
    });
    const coreMesh = new THREE.Mesh(coreGeo, coreMat);
    mainGroup.add(coreMesh);
    coreMeshRef.current = coreMesh;

    // 4. Multi-Axis Revolving Orbital Rings (Revolving around each other)
    const ringMat1 = new THREE.MeshStandardMaterial({
      color: new THREE.Color(resolvedAccent),
      wireframe: true,
      roughness: 0.8,
      metalness: 0.0,
    });
    const ringGeo1 = new THREE.TorusGeometry(1.15, 0.025, 16, 48);
    const innerRing = new THREE.Mesh(ringGeo1, ringMat1);
    innerRing.rotation.x = Math.PI / 3;
    mainGroup.add(innerRing);
    innerRingRef.current = innerRing;

    const ringGeo2 = new THREE.TorusGeometry(1.38, 0.02, 16, 48);
    const ringMat2 = new THREE.MeshBasicMaterial({
      color: new THREE.Color('#10B981'),
      wireframe: true,
    });
    const outerRing = new THREE.Mesh(ringGeo2, ringMat2);
    outerRing.rotation.y = Math.PI / 4;
    mainGroup.add(outerRing);
    outerRingRef.current = outerRing;

    // 5. Orbiting Soft Particle Cloud
    const particleCount = 28;
    const particleGeo = new THREE.BufferGeometry();
    const positions = new Float32Array(particleCount * 3);
    for (let i = 0; i < particleCount; i++) {
      const angle = (i / particleCount) * Math.PI * 2;
      const radius = 1.48 + (Math.random() - 0.5) * 0.2;
      positions[i * 3] = Math.cos(angle) * radius;
      positions[i * 3 + 1] = (Math.random() - 0.5) * 0.5;
      positions[i * 3 + 2] = Math.sin(angle) * radius;
    }
    particleGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));

    const particleMat = new THREE.PointsMaterial({
      size: 0.06,
      color: new THREE.Color(resolvedAccent),
      transparent: true,
      opacity: 0.8,
    });
    const particles = new THREE.Points(particleGeo, particleMat);
    mainGroup.add(particles);
    particlesRef.current = particles;

    // 6. Anime.js Idle Float Oscillation
    const floatAnim = animate(mainGroup.position, {
      y: [-0.06, 0.06],
      duration: state === 'sleeping' ? 3200 : state === 'working' ? 1200 : 2000,
      alternate: true,
      loop: true,
      ease: 'inOutSine',
    });

    // Render loop (Multi-axis ring revolution around each other, mouse tracking removed)
    let frameId: number;
    const render = () => {
      frameId = requestAnimationFrame(render);

      const isFailed = state === 'disapproving' || state === 'error' || state === 'failed';
      const isWorking = state === 'working' || state === 'diagnostic' || state === 'typing';

      // Ring rotation speed dynamics:
      // Fast for working (3.0x), Slow for idle/success (0.8x), Halted/Frozen for failed (0.0x)
      const speedMultiplier = isFailed ? 0 : isWorking ? 3.0 : 0.8;

      // Inner ring revolves on X and Y axes
      if (innerRing) {
        innerRing.rotation.x += 0.015 * speedMultiplier;
        innerRing.rotation.y += 0.02 * speedMultiplier;
      }

      // Outer ring revolves around counter directions on Y and Z axes
      if (outerRing) {
        outerRing.rotation.y -= 0.018 * speedMultiplier;
        outerRing.rotation.z += 0.012 * speedMultiplier;
      }

      // Particle halo slow counter-orbit
      if (particles) {
        particles.rotation.y += 0.006 * speedMultiplier;
        particles.rotation.x -= 0.003 * speedMultiplier;
      }

      renderer.render(scene, camera);
    };

    render();

    return () => {
      cancelAnimationFrame(frameId);
      floatAnim.pause();
      renderer.dispose();
      if (container.contains(renderer.domElement)) {
        container.removeChild(renderer.domElement);
      }
    };
  }, [size, resolvedAccent, state]);

  // Speech Amplitude Core Pulse
  useEffect(() => {
    if (!coreMeshRef.current) return;
    const baseScale = 1 + speechAmplitude * 0.35;
    coreMeshRef.current.scale.set(baseScale, baseScale, baseScale);
  }, [speechAmplitude]);

  // Click 360 Spin Handler
  const handleContainerClick = () => {
    if (onClick) onClick();
    if (isSpinning || !mainGroupRef.current) return;
    setIsSpinning(true);

    animate(mainGroupRef.current.rotation, {
      y: `+=${Math.PI * 2}`,
      z: `+=${Math.PI * 0.5}`,
      duration: 900,
      ease: 'outElastic(1, .5)',
      onComplete: () => setIsSpinning(false),
    });

    if (outerRingRef.current) {
      animate(outerRingRef.current.scale, {
        x: [1, 1.4, 1],
        y: [1, 1.4, 1],
        duration: 500,
        ease: 'outCubic',
      });
    }
  };

  return (
    <div
      onClick={handleContainerClick}
      className="relative flex items-center justify-center cursor-pointer select-none"
      style={{ width: `${size}px`, height: `${size}px` }}
      title={`3D Mascot (${state}) - Click to spin`}
    >
      <div ref={mountRef} style={{ width: `${size}px`, height: `${size}px` }} />
    </div>
  );
};

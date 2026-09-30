import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../core/theme.dart';

class VoiceOrbPainter extends CustomPainter {
  final double animationValue;
  final double amplitude;
  final bool isListening;

  VoiceOrbPainter({
    required this.animationValue,
    required this.amplitude,
    required this.isListening,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    final baseRadius = math.min(size.width, size.height) * 0.28;
    final pulseRadius = baseRadius + (amplitude * 24.0 * math.sin(animationValue * math.pi * 2));

    // Outer aura glow
    final auraPaint = Paint()
      ..shader = RadialGradient(
        colors: [
          (isListening ? MeridianTheme.cyanAccent : MeridianTheme.purpleAccent).withValues(alpha: 0.35),
          MeridianTheme.purpleAccent.withValues(alpha: 0.1),
          Colors.transparent,
        ],
        stops: const [0.2, 0.6, 1.0],
      ).createShader(Rect.fromCircle(center: center, radius: pulseRadius * 2.2));

    canvas.drawCircle(center, pulseRadius * 2.2, auraPaint);

    // Dynamic wave spectrum ring
    final wavePaint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2.5
      ..shader = SweepGradient(
        colors: const [
          MeridianTheme.cyanAccent,
          MeridianTheme.purpleAccent,
          MeridianTheme.emeraldGreen,
          MeridianTheme.cyanAccent,
        ],
        transform: GradientRotation(animationValue * math.pi * 2),
      ).createShader(Rect.fromCircle(center: center, radius: pulseRadius * 1.4));

    final path = Path();
    const wavePoints = 72;
    for (int i = 0; i <= wavePoints; i++) {
      final angle = (i / wavePoints) * math.pi * 2;
      final waveOffset = math.sin(angle * 8 + animationValue * math.pi * 4) * (amplitude * 12.0);
      final r = pulseRadius * 1.35 + waveOffset;
      final x = center.dx + r * math.cos(angle);
      final y = center.dy + r * math.sin(angle);
      if (i == 0) {
        path.moveTo(x, y);
      } else {
        path.lineTo(x, y);
      }
    }
    canvas.drawPath(path, wavePaint);

    // Inner glowing core
    final corePaint = Paint()
      ..shader = const RadialGradient(
        colors: [
          Colors.white,
          MeridianTheme.cyanAccent,
          MeridianTheme.purpleAccent,
          MeridianTheme.background,
        ],
        stops: [0.0, 0.45, 0.8, 1.0],
      ).createShader(Rect.fromCircle(center: center, radius: pulseRadius));

    canvas.drawCircle(center, pulseRadius, corePaint);
  }

  @override
  bool shouldRepaint(covariant VoiceOrbPainter oldDelegate) {
    return oldDelegate.animationValue != animationValue ||
        oldDelegate.amplitude != amplitude ||
        oldDelegate.isListening != isListening;
  }
}

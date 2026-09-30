import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../core/theme.dart';
import '../providers/voice_orb_provider.dart';
import 'voice_orb_painter.dart';

class VoiceOrbHUD extends ConsumerStatefulWidget {
  const VoiceOrbHUD({super.key});

  @override
  ConsumerState<VoiceOrbHUD> createState() => _VoiceOrbHUDState();
}

class _VoiceOrbHUDState extends ConsumerState<VoiceOrbHUD> with SingleTickerProviderStateMixin {
  late AnimationController _animController;

  @override
  void initState() {
    super.initState();
    _animController = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 4),
    )..repeat();
  }

  @override
  void dispose() {
    _animController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final voiceState = ref.watch(voiceOrbProvider);
    final voiceNotifier = ref.read(voiceOrbProvider.notifier);

    final isListening = voiceState.state == OrbListeningState.listening;

    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        GestureDetector(
          onTap: () => voiceNotifier.toggleListening(),
          child: AnimatedBuilder(
            animation: _animController,
            builder: (context, child) {
              return SizedBox(
                width: 260,
                height: 260,
                child: CustomPaint(
                  painter: VoiceOrbPainter(
                    animationValue: _animController.value,
                    amplitude: voiceState.amplitude,
                    isListening: isListening,
                  ),
                ),
              );
            },
          ),
        ),
        const SizedBox(height: 12),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
              decoration: BoxDecoration(
                color: MeridianTheme.surface,
                borderRadius: BorderRadius.circular(20),
                border: Border.all(
                  color: isListening ? MeridianTheme.cyanAccent : MeridianTheme.surfaceLight,
                ),
              ),
              child: Row(
                children: [
                  Icon(
                    isListening ? Icons.mic : Icons.mic_off,
                    size: 16,
                    color: isListening ? MeridianTheme.cyanAccent : MeridianTheme.textSecondary,
                  ),
                  const SizedBox(width: 8),
                  Text(
                    isListening ? 'VOICE VAD ACTIVE' : 'TAP ORB TO SPEAK',
                    style: TextStyle(
                      color: isListening ? MeridianTheme.cyanAccent : MeridianTheme.textSecondary,
                      fontSize: 12,
                      fontWeight: FontWeight.bold,
                      letterSpacing: 1.1,
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(width: 12),
            IconButton(
              onPressed: () => voiceNotifier.toggleMute(),
              icon: Icon(
                voiceState.isMicMuted ? Icons.volume_off : Icons.volume_up,
                color: voiceState.isMicMuted ? MeridianTheme.roseError : MeridianTheme.textPrimary,
              ),
              style: IconButton.styleFrom(
                backgroundColor: MeridianTheme.surface,
                side: const BorderSide(color: MeridianTheme.surfaceLight),
              ),
            ),
          ],
        ),
      ],
    );
  }
}

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../core/theme_engine.dart';
import '../providers/agent_chat_provider.dart';
import '../providers/voice_orb_provider.dart';
import 'voice_orb_hud.dart';

class VoiceModeView extends ConsumerWidget {
  const VoiceModeView({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final themeState = ref.watch(themeProvider);
    final colors = themeState.colors;
    final voiceState = ref.watch(voiceOrbProvider);
    final voiceNotifier = ref.read(voiceOrbProvider.notifier);
    final agentState = ref.watch(agentChatProvider);

    final isListening = voiceState.state == OrbListeningState.listening;

    return Center(
      child: SingleChildScrollView(
        padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 16),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            // Voice Orb Visualizer HUD
            const VoiceOrbHUD(),

            const SizedBox(height: 24),

            // Live Transcript or Status Banner
            Container(
              constraints: const BoxConstraints(maxWidth: 380),
              padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 12),
              decoration: BoxDecoration(
                color: colors.surface,
                borderRadius: BorderRadius.circular(16),
                border: Border.all(
                  color: isListening
                      ? colors.primaryAccent.withValues(alpha: 0.5)
                      : colors.borderSubtle,
                ),
                boxShadow: [
                  BoxShadow(
                    color: isListening
                        ? colors.primaryAccent.withValues(alpha: 0.15)
                        : Colors.transparent,
                    blurRadius: 16,
                  ),
                ],
              ),
              child: Column(
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Container(
                        width: 8,
                        height: 8,
                        decoration: BoxDecoration(
                          shape: BoxShape.circle,
                          color: isListening ? colors.primaryAccent : colors.textSecondary,
                        ),
                      ),
                      const SizedBox(width: 8),
                      Text(
                        isListening ? 'SPEECH DETECTION ACTIVE' : 'VOICE ENGINE READY',
                        style: TextStyle(
                          color: isListening ? colors.primaryAccent : colors.textSecondary,
                          fontSize: 11,
                          fontWeight: FontWeight.w700,
                          letterSpacing: 1.1,
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 8),
                  Text(
                    agentState.activePrompt ??
                        (isListening
                            ? 'Speak naturally. Kokoro neural voice & VAD will detect your voice...'
                            : 'Tap the orb or mic button below to start real-time duplex voice conversation.'),
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      color: colors.textPrimary,
                      fontSize: 13,
                      height: 1.4,
                    ),
                  ),
                ],
              ),
            ),

            const SizedBox(height: 28),

            // Floating Audio Control Bar
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                // Mic Mute Toggle
                _VoiceActionButton(
                  icon: voiceState.isMicMuted ? Icons.mic_off : Icons.mic,
                  label: voiceState.isMicMuted ? 'Muted' : 'Mic Active',
                  isActive: !voiceState.isMicMuted,
                  colors: colors,
                  onTap: () => voiceNotifier.toggleMute(),
                ),
                const SizedBox(width: 16),

                // Primary Listen / Cutoff Button
                _VoiceActionButton(
                  icon: isListening ? Icons.stop_rounded : Icons.graphic_eq_rounded,
                  label: isListening ? 'Cutoff' : 'Listen',
                  isActive: isListening,
                  isPrimary: true,
                  colors: colors,
                  onTap: () => voiceNotifier.toggleListening(),
                ),
                const SizedBox(width: 16),

                // Audio Output Toggle
                _VoiceActionButton(
                  icon: Icons.volume_up_rounded,
                  label: 'Speaker',
                  isActive: true,
                  colors: colors,
                  onTap: () {
                    ScaffoldMessenger.of(context).showSnackBar(
                      SnackBar(
                        content: const Text('Audio output: System speaker routing active'),
                        duration: const Duration(seconds: 1),
                        backgroundColor: colors.surfaceLight,
                        behavior: SnackBarBehavior.floating,
                      ),
                    );
                  },
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

class _VoiceActionButton extends StatelessWidget {
  final IconData icon;
  final String label;
  final bool isActive;
  final bool isPrimary;
  final PaletteColors colors;
  final VoidCallback onTap;

  const _VoiceActionButton({
    required this.icon,
    required this.label,
    required this.isActive,
    this.isPrimary = false,
    required this.colors,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    final bgColor = isPrimary
        ? (isActive ? Colors.redAccent : colors.primaryAccent)
        : colors.surface;
    final fgColor = isPrimary
        ? Colors.white
        : (isActive ? colors.primaryAccent : colors.textSecondary);

    return InkWell(
      onTap: onTap,
      borderRadius: BorderRadius.circular(16),
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
        decoration: BoxDecoration(
          color: bgColor,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(
            color: isPrimary ? Colors.transparent : colors.borderSubtle,
          ),
          boxShadow: isPrimary
              ? [
                  BoxShadow(
                    color: bgColor.withValues(alpha: 0.3),
                    blurRadius: 10,
                    offset: const Offset(0, 3),
                  ),
                ]
              : null,
        ),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(icon, size: 22, color: fgColor),
            const SizedBox(height: 4),
            Text(
              label,
              style: TextStyle(
                color: isPrimary ? Colors.white : colors.textPrimary,
                fontSize: 10.5,
                fontWeight: FontWeight.w600,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

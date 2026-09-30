import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'core/theme.dart';
import 'core/secure_storage.dart';
import 'providers/agent_chat_provider.dart';
import 'views/voice_orb_hud.dart';
import 'views/thought_carousel.dart';
import 'views/camera_vision_view.dart';
import 'views/remote_pairing_modal.dart';

void main() {
  runApp(
    const ProviderScope(
      child: MeridianMobileApp(),
    ),
  );
}

class MeridianMobileApp extends StatelessWidget {
  const MeridianMobileApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Meridian-X Mobile',
      debugShowCheckedModeBanner: false,
      theme: MeridianTheme.darkTheme,
      home: const MeridianHomeScreen(),
    );
  }
}

class MeridianHomeScreen extends ConsumerStatefulWidget {
  const MeridianHomeScreen({super.key});

  @override
  ConsumerState<MeridianHomeScreen> createState() => _MeridianHomeScreenState();
}

class _MeridianHomeScreenState extends ConsumerState<MeridianHomeScreen> {
  final TextEditingController _promptController = TextEditingController();
  bool _showVisionView = false;

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      _autoConnect();
    });
  }

  Future<void> _autoConnect() async {
    final savedUrl = await MeridianSecureStorage.getServerUrl();
    if (savedUrl == null || savedUrl.trim().isEmpty) {
      return;
    }
    final savedToken = await MeridianSecureStorage.getAuthToken();
    if (mounted) {
      await ref.read(agentChatProvider.notifier).connect(savedUrl, token: savedToken);
    }
  }

  void _openPairingModal() {
    showDialog(
      context: context,
      builder: (context) => const RemotePairingModal(),
    );
  }

  void _submitPrompt() {
    final text = _promptController.text;
    if (text.trim().isNotEmpty) {
      ref.read(agentChatProvider.notifier).sendPrompt(text);
      _promptController.clear();
    }
  }

  @override
  Widget build(BuildContext context) {
    final agentState = ref.watch(agentChatProvider);
    final telemetry = agentState.telemetry;

    return Scaffold(
      backgroundColor: MeridianTheme.background,
      appBar: AppBar(
        title: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Container(
              width: 10,
              height: 10,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: agentState.isConnected ? MeridianTheme.emeraldGreen : MeridianTheme.roseError,
                boxShadow: [
                  BoxShadow(
                    color: (agentState.isConnected ? MeridianTheme.emeraldGreen : MeridianTheme.roseError).withValues(alpha: 0.5),
                    blurRadius: 6,
                  )
                ],
              ),
            ),
            const SizedBox(width: 8),
            const Text(
              'MERIDIAN-X',
              style: TextStyle(
                fontWeight: FontWeight.w800,
                letterSpacing: 1.5,
                fontSize: 18,
              ),
            ),
          ],
        ),
        actions: [
          IconButton(
            onPressed: () => setState(() => _showVisionView = !_showVisionView),
            icon: Icon(
              Icons.camera_alt,
              color: _showVisionView ? MeridianTheme.cyanAccent : MeridianTheme.textSecondary,
            ),
            tooltip: 'Toggle Camera Vision',
          ),
          IconButton(
            onPressed: _openPairingModal,
            icon: const Icon(Icons.qr_code_2, color: MeridianTheme.purpleAccent),
            tooltip: 'Remote Pairing',
          ),
        ],
      ),
      body: SafeArea(
        child: Column(
          children: [
            // Telemetry Status Header
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
              margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
              decoration: BoxDecoration(
                color: MeridianTheme.surface,
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: MeridianTheme.surfaceLight),
              ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: [
                  _TelemetryBadge(
                    icon: Icons.memory,
                    label: 'CPU',
                    value: '${telemetry.cpuPercent.toInt()}%',
                    color: MeridianTheme.cyanAccent,
                  ),
                  _TelemetryBadge(
                    icon: Icons.speed,
                    label: 'PING',
                    value: '${telemetry.pingMs} ms',
                    color: MeridianTheme.purpleAccent,
                  ),
                  _TelemetryBadge(
                    icon: Icons.verified_user,
                    label: 'ANTI-HALLUCINATION',
                    value: telemetry.antiHallucinationActive ? 'ACTIVE' : 'OFF',
                    color: MeridianTheme.emeraldGreen,
                  ),
                ],
              ),
            ),

            // Vision Camera Scanner Viewport if active
            if (_showVisionView) const CameraVisionView(),

            // Voice Orb Visualizer HUD
            const Expanded(
              child: Center(
                child: SingleChildScrollView(
                  child: VoiceOrbHUD(),
                ),
              ),
            ),

            // Agent Thought Stream Carousel
            const ThoughtCarouselWidget(),

            // Interactive Quick Prompt Command Input
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: Row(
                children: [
                  Expanded(
                    child: TextField(
                      controller: _promptController,
                      onSubmitted: (_) => _submitPrompt(),
                      decoration: InputDecoration(
                        hintText: 'Ask Meridian agent or invoke action...',
                        hintStyle: const TextStyle(color: MeridianTheme.textSecondary, fontSize: 13),
                        filled: true,
                        fillColor: MeridianTheme.surface,
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(24),
                          borderSide: const BorderSide(color: MeridianTheme.surfaceLight),
                        ),
                        focusedBorder: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(24),
                          borderSide: const BorderSide(color: MeridianTheme.cyanAccent),
                        ),
                        contentPadding: const EdgeInsets.symmetric(horizontal: 20, vertical: 14),
                      ),
                      style: const TextStyle(color: MeridianTheme.textPrimary, fontSize: 14),
                    ),
                  ),
                  const SizedBox(width: 10),
                  FloatingActionButton.small(
                    onPressed: _submitPrompt,
                    backgroundColor: MeridianTheme.cyanAccent,
                    foregroundColor: Colors.black,
                    elevation: 4,
                    child: const Icon(Icons.send, size: 18),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _TelemetryBadge extends StatelessWidget {
  final IconData icon;
  final String label;
  final String value;
  final Color color;

  const _TelemetryBadge({
    required this.icon,
    required this.label,
    required this.value,
    required this.color,
  });

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Icon(icon, size: 14, color: color),
        const SizedBox(width: 6),
        Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(
              label,
              style: const TextStyle(color: MeridianTheme.textSecondary, fontSize: 9, fontWeight: FontWeight.bold),
            ),
            Text(
              value,
              style: const TextStyle(color: MeridianTheme.textPrimary, fontSize: 11, fontWeight: FontWeight.bold),
            ),
          ],
        ),
      ],
    );
  }
}

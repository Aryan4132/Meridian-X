import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'core/theme.dart';
import 'core/theme_engine.dart';
import 'core/model_engines.dart';
import 'core/secure_storage.dart';
import 'providers/agent_chat_provider.dart';
import 'views/chat_stream_view.dart';
import 'views/voice_mode_view.dart';
import 'views/model_hub_view.dart';
import 'views/settings_view.dart';
import 'views/bottom_nav_dock.dart';
import 'views/camera_vision_view.dart';
import 'views/remote_pairing_modal.dart';

void main() {
  runApp(
    const ProviderScope(
      child: MeridianMobileApp(),
    ),
  );
}

class MeridianMobileApp extends ConsumerWidget {
  const MeridianMobileApp({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final themeState = ref.watch(themeProvider);

    return MaterialApp(
      title: 'Meridian-X Mobile',
      debugShowCheckedModeBanner: false,
      theme: themeState.themeData,
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
  int _selectedTabIndex = 0;
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

  @override
  Widget build(BuildContext context) {
    final themeState = ref.watch(themeProvider);
    final colors = themeState.colors;
    final agentState = ref.watch(agentChatProvider);
    final engineState = ref.watch(engineManagerProvider);
    final telemetry = agentState.telemetry;

    return Scaffold(
      backgroundColor: colors.background,
      resizeToAvoidBottomInset: true,
      appBar: AppBar(
        backgroundColor: colors.background,
        elevation: 0,
        titleSpacing: 16,
        title: Row(
          children: [
            Container(
              width: 9,
              height: 9,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: agentState.isConnected ? MeridianTheme.emeraldGreen : MeridianTheme.roseError,
                boxShadow: [
                  BoxShadow(
                    color: (agentState.isConnected ? MeridianTheme.emeraldGreen : MeridianTheme.roseError)
                        .withValues(alpha: 0.6),
                    blurRadius: 8,
                    spreadRadius: 1,
                  ),
                ],
              ),
            ),
            const SizedBox(width: 8),
            const Text(
              'MERIDIAN-X',
              style: TextStyle(
                fontWeight: FontWeight.w800,
                letterSpacing: 1.4,
                fontSize: 16,
              ),
            ),
          ],
        ),
        actions: [
          // Active Model Quick Pill
          InkWell(
            onTap: () => setState(() => _selectedTabIndex = 2),
            borderRadius: BorderRadius.circular(16),
            child: Container(
              margin: const EdgeInsets.symmetric(vertical: 10),
              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
              decoration: BoxDecoration(
                color: colors.surface,
                borderRadius: BorderRadius.circular(16),
                border: Border.all(color: colors.borderSubtle),
              ),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Icon(Icons.auto_awesome, color: colors.primaryAccent, size: 12),
                  const SizedBox(width: 6),
                  Text(
                    engineState.activeModel.name,
                    style: TextStyle(
                      color: colors.textPrimary,
                      fontWeight: FontWeight.w700,
                      fontSize: 11,
                    ),
                  ),
                ],
              ),
            ),
          ),
          const SizedBox(width: 8),

          // Host Ping Pill
          Container(
            margin: const EdgeInsets.symmetric(vertical: 10),
            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
            decoration: BoxDecoration(
              color: colors.surfaceLight,
              borderRadius: BorderRadius.circular(12),
            ),
            child: Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                Icon(Icons.speed, size: 11, color: colors.secondaryAccent),
                const SizedBox(width: 4),
                Text(
                  '${telemetry.pingMs}ms',
                  style: TextStyle(
                    color: colors.textSecondary,
                    fontSize: 10,
                    fontWeight: FontWeight.w700,
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(width: 4),

          // Remote Pairing Shortcut
          IconButton(
            onPressed: _openPairingModal,
            icon: Icon(Icons.qr_code_2, color: colors.primaryAccent, size: 20),
            tooltip: 'Remote Pairing QR',
            visualDensity: VisualDensity.compact,
          ),
          const SizedBox(width: 8),
        ],
      ),
      body: SafeArea(
        child: Column(
          children: [
            // Camera Vision Scanner Viewport if toggled
            if (_showVisionView) ...[
              Container(
                margin: const EdgeInsets.fromLTRB(16, 0, 16, 8),
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(color: colors.primaryAccent.withValues(alpha: 0.5)),
                ),
                clipBehavior: Clip.antiAlias,
                child: Stack(
                  children: [
                    const CameraVisionView(),
                    Positioned(
                      top: 8,
                      right: 8,
                      child: InkWell(
                        onTap: () => setState(() => _showVisionView = false),
                        child: Container(
                          padding: const EdgeInsets.all(4),
                          decoration: const BoxDecoration(
                            color: Colors.black54,
                            shape: BoxShape.circle,
                          ),
                          child: const Icon(Icons.close, size: 16, color: Colors.white),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ],

            // Main Tab Viewport Stack (Preserves scroll & state)
            Expanded(
              child: IndexedStack(
                index: _selectedTabIndex,
                children: [
                  ChatStreamView(
                    onToggleVision: () => setState(() => _showVisionView = !_showVisionView),
                    isVisionActive: _showVisionView,
                  ),
                  const VoiceModeView(),
                  const ModelHubView(isEmbedded: true),
                  const SettingsView(),
                ],
              ),
            ),

            // Floating Frosted Glass Bottom Navigation Dock
            BottomNavDock(
              currentIndex: _selectedTabIndex,
              onSelectTab: (index) => setState(() => _selectedTabIndex = index),
              colors: colors,
            ),
          ],
        ),
      ),
    );
  }
}

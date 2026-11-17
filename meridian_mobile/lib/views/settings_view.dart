import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../core/theme.dart';
import '../core/theme_engine.dart';
import '../core/secure_storage.dart';
import '../providers/agent_chat_provider.dart';
import 'remote_pairing_modal.dart';

class SettingsView extends ConsumerStatefulWidget {
  const SettingsView({super.key});

  @override
  ConsumerState<SettingsView> createState() => _SettingsViewState();
}

class _SettingsViewState extends ConsumerState<SettingsView> {
  final TextEditingController _urlController = TextEditingController();
  bool _isLoading = false;

  @override
  void initState() {
    super.initState();
    _loadSavedUrl();
  }

  @override
  void dispose() {
    _urlController.dispose();
    super.dispose();
  }

  Future<void> _loadSavedUrl() async {
    final url = await MeridianSecureStorage.getServerUrl();
    if (url != null && mounted) {
      _urlController.text = url;
    }
  }

  Future<void> _saveAndConnect() async {
    final url = _urlController.text.trim();
    if (url.isEmpty) return;

    setState(() => _isLoading = true);
    await MeridianSecureStorage.saveServerUrl(url);
    final token = await MeridianSecureStorage.getAuthToken();
    if (mounted) {
      await ref.read(agentChatProvider.notifier).connect(url, token: token);
      setState(() => _isLoading = false);
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(
            content: Text('Connecting to Meridian-X backend...'),
            duration: Duration(seconds: 2),
            behavior: SnackBarBehavior.floating,
          ),
        );
      }
    }
  }

  void _openQrModal() {
    showDialog(
      context: context,
      builder: (context) => const RemotePairingModal(),
    );
  }

  @override
  Widget build(BuildContext context) {
    final themeState = ref.watch(themeProvider);
    final themeNotifier = ref.read(themeProvider.notifier);
    final colors = themeState.colors;
    final agentState = ref.watch(agentChatProvider);
    final telemetry = agentState.telemetry;

    return SingleChildScrollView(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Section 1: Themes & Aesthetics
          _SectionHeader(title: 'VISUAL DESIGN & THEME ENGINE', colors: colors),
          const SizedBox(height: 10),
          _ThemePaletteGrid(
            activePalette: themeState.palette,
            colors: colors,
            onSelect: (palette) => themeNotifier.setPalette(palette),
          ),
          const SizedBox(height: 16),

          // Custom Accent Color Swatches
          Text(
            'Luminescent Accent Tint',
            style: TextStyle(
              color: colors.textSecondary,
              fontSize: 12,
              fontWeight: FontWeight.w600,
            ),
          ),
          const SizedBox(height: 8),
          _AccentColorPicker(
            activeAccent: themeState.customAccent ?? colors.primaryAccent,
            onSelect: (color) => themeNotifier.setCustomAccent(color),
            onReset: () => themeNotifier.resetCustomAccent(),
            colors: colors,
          ),

          const SizedBox(height: 24),

          // Section 2: Remote Desktop Bridge & WebSocket
          _SectionHeader(title: 'DESKTOP PAIRING & SYNC', colors: colors),
          const SizedBox(height: 10),
          Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: colors.surface,
              borderRadius: BorderRadius.circular(16),
              border: Border.all(color: colors.borderSubtle),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Container(
                      width: 10,
                      height: 10,
                      decoration: BoxDecoration(
                        shape: BoxShape.circle,
                        color: agentState.isConnected
                            ? MeridianTheme.emeraldGreen
                            : MeridianTheme.roseError,
                      ),
                    ),
                    const SizedBox(width: 8),
                    Text(
                      agentState.isConnected ? 'CONNECTED TO DESKTOP' : 'DISCONNECTED / OFFLINE',
                      style: TextStyle(
                        color: agentState.isConnected
                            ? MeridianTheme.emeraldGreen
                            : MeridianTheme.roseError,
                        fontWeight: FontWeight.w700,
                        fontSize: 11.5,
                        letterSpacing: 0.8,
                      ),
                    ),
                    const Spacer(),
                    OutlinedButton.icon(
                      onPressed: _openQrModal,
                      icon: const Icon(Icons.qr_code_scanner, size: 14),
                      label: const Text('Scan QR', style: TextStyle(fontSize: 11)),
                      style: OutlinedButton.styleFrom(
                        foregroundColor: colors.primaryAccent,
                        side: BorderSide(color: colors.primaryAccent.withValues(alpha: 0.5)),
                        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                        visualDensity: VisualDensity.compact,
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 14),
                TextField(
                  controller: _urlController,
                  style: TextStyle(color: colors.textPrimary, fontSize: 13),
                  decoration: InputDecoration(
                    labelText: 'WebSocket URL',
                    labelStyle: TextStyle(color: colors.textSecondary, fontSize: 12),
                    hintText: 'ws://192.168.1.100:4132/ws',
                    hintStyle: TextStyle(color: colors.textSecondary.withValues(alpha: 0.5)),
                    filled: true,
                    fillColor: colors.surfaceLight,
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(12),
                      borderSide: BorderSide(color: colors.borderSubtle),
                    ),
                    contentPadding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
                  ),
                ),
                const SizedBox(height: 12),
                Row(
                  children: [
                    Expanded(
                      child: ElevatedButton(
                        onPressed: _isLoading ? null : _saveAndConnect,
                        style: ElevatedButton.styleFrom(
                          backgroundColor: colors.primaryAccent,
                          foregroundColor: Colors.black,
                          padding: const EdgeInsets.symmetric(vertical: 12),
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                        ),
                        child: _isLoading
                            ? const SizedBox(
                                width: 18,
                                height: 18,
                                child: CircularProgressIndicator(strokeWidth: 2, color: Colors.black),
                              )
                            : const Text('Connect Engine', style: TextStyle(fontWeight: FontWeight.w700)),
                      ),
                    ),
                    if (agentState.isConnected) ...[
                      const SizedBox(width: 8),
                      OutlinedButton(
                        onPressed: () => ref.read(agentChatProvider.notifier).disconnect(),
                        style: OutlinedButton.styleFrom(
                          foregroundColor: MeridianTheme.roseError,
                          side: const BorderSide(color: MeridianTheme.roseError),
                          padding: const EdgeInsets.symmetric(vertical: 12, horizontal: 16),
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                        ),
                        child: const Text('Disconnect'),
                      ),
                    ],
                  ],
                ),
              ],
            ),
          ),

          const SizedBox(height: 24),

          // Section 3: Hardware Diagnostics & Telemetry
          _SectionHeader(title: 'HARDWARE & RUNTIME METRICS', colors: colors),
          const SizedBox(height: 10),
          Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: colors.surface,
              borderRadius: BorderRadius.circular(16),
              border: Border.all(color: colors.borderSubtle),
            ),
            child: Column(
              children: [
                _TelemetryRow(
                  icon: Icons.memory,
                  label: 'Desktop Host CPU',
                  value: '${telemetry.cpuPercent.toInt()}%',
                  colors: colors,
                ),
                const Divider(height: 16, color: Color(0x1AFFFFFF)),
                _TelemetryRow(
                  icon: Icons.speed,
                  label: 'Latency / Ping',
                  value: '${telemetry.pingMs} ms',
                  colors: colors,
                ),
                const Divider(height: 16, color: Color(0x1AFFFFFF)),
                _TelemetryRow(
                  icon: Icons.security,
                  label: 'Encrypted Keystore',
                  value: 'AES-256 Enabled',
                  colors: colors,
                ),
                const Divider(height: 16, color: Color(0x1AFFFFFF)),
                _TelemetryRow(
                  icon: Icons.info_outline,
                  label: 'Mobile Engine Version',
                  value: 'v0.1.7 (Sprint 52)',
                  colors: colors,
                ),
              ],
            ),
          ),
          const SizedBox(height: 32),
        ],
      ),
    );
  }
}

class _SectionHeader extends StatelessWidget {
  final String title;
  final PaletteColors colors;

  const _SectionHeader({required this.title, required this.colors});

  @override
  Widget build(BuildContext context) {
    return Text(
      title,
      style: TextStyle(
        color: colors.primaryAccent,
        fontSize: 11,
        fontWeight: FontWeight.w800,
        letterSpacing: 1.2,
      ),
    );
  }
}

class _ThemePaletteGrid extends StatelessWidget {
  final AppThemePalette activePalette;
  final PaletteColors colors;
  final ValueChanged<AppThemePalette> onSelect;

  const _ThemePaletteGrid({
    required this.activePalette,
    required this.colors,
    required this.onSelect,
  });

  @override
  Widget build(BuildContext context) {
    return GridView.count(
      crossAxisCount: 2,
      shrinkWrap: true,
      physics: const NeverScrollableScrollPhysics(),
      crossAxisSpacing: 10,
      mainAxisSpacing: 10,
      childAspectRatio: 1.8,
      children: AppThemePalette.values.map((palette) {
        final isSelected = activePalette == palette;
        final previewColors = palette.colors;

        return InkWell(
          onTap: () => onSelect(palette),
          borderRadius: BorderRadius.circular(14),
          child: Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: previewColors.surface,
              borderRadius: BorderRadius.circular(14),
              border: Border.all(
                color: isSelected ? colors.primaryAccent : colors.borderSubtle,
                width: isSelected ? 1.5 : 1,
              ),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      palette.displayName,
                      style: TextStyle(
                        color: isSelected ? colors.primaryAccent : previewColors.textPrimary,
                        fontWeight: FontWeight.w700,
                        fontSize: 12,
                      ),
                    ),
                    if (isSelected)
                      Icon(Icons.check_circle, size: 14, color: colors.primaryAccent),
                  ],
                ),
                Row(
                  children: [
                    _ColorPip(color: previewColors.background),
                    const SizedBox(width: 4),
                    _ColorPip(color: previewColors.primaryAccent),
                    const SizedBox(width: 4),
                    _ColorPip(color: previewColors.secondaryAccent),
                  ],
                ),
              ],
            ),
          ),
        );
      }).toList(),
    );
  }
}

class _ColorPip extends StatelessWidget {
  final Color color;

  const _ColorPip({required this.color});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 14,
      height: 14,
      decoration: BoxDecoration(
        color: color,
        shape: BoxShape.circle,
        border: Border.all(color: Colors.white24, width: 0.5),
      ),
    );
  }
}

class _AccentColorPicker extends StatelessWidget {
  final Color activeAccent;
  final ValueChanged<Color> onSelect;
  final VoidCallback onReset;
  final PaletteColors colors;

  const _AccentColorPicker({
    required this.activeAccent,
    required this.onSelect,
    required this.onReset,
    required this.colors,
  });

  @override
  Widget build(BuildContext context) {
    final swatches = [
      const Color(0xFF00E5FF), // Cyan
      const Color(0xFF7C3AED), // Electric Violet
      const Color(0xFF10B981), // Emerald
      const Color(0xFFF59E0B), // Amber Gold
      const Color(0xFFF43F5E), // Rose Pink
      const Color(0xFF38BDF8), // Sky Blue
    ];

    return Row(
      children: [
        ...swatches.map((c) {
          final isSelected = activeAccent.toARGB32() == c.toARGB32();
          return Padding(
            padding: const EdgeInsets.only(right: 10),
            child: GestureDetector(
              onTap: () => onSelect(c),
              child: Container(
                width: 28,
                height: 28,
                decoration: BoxDecoration(
                  color: c,
                  shape: BoxShape.circle,
                  border: Border.all(
                    color: isSelected ? Colors.white : Colors.transparent,
                    width: 2,
                  ),
                  boxShadow: isSelected
                      ? [BoxShadow(color: c.withValues(alpha: 0.6), blurRadius: 8)]
                      : null,
                ),
              ),
            ),
          );
        }),
        const Spacer(),
        TextButton(
          onPressed: onReset,
          child: Text(
            'Reset',
            style: TextStyle(color: colors.textSecondary, fontSize: 12),
          ),
        ),
      ],
    );
  }
}

class _TelemetryRow extends StatelessWidget {
  final IconData icon;
  final String label;
  final String value;
  final PaletteColors colors;

  const _TelemetryRow({
    required this.icon,
    required this.label,
    required this.value,
    required this.colors,
  });

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Row(
          children: [
            Icon(icon, size: 16, color: colors.secondaryAccent),
            const SizedBox(width: 8),
            Text(label, style: TextStyle(color: colors.textSecondary, fontSize: 13)),
          ],
        ),
        Text(
          value,
          style: TextStyle(
            color: colors.textPrimary,
            fontWeight: FontWeight.w700,
            fontSize: 13,
          ),
        ),
      ],
    );
  }
}

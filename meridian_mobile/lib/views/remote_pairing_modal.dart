import 'dart:convert';
import 'package:crypto/crypto.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../core/secure_storage.dart';
import '../core/theme.dart';
import '../core/websocket_client.dart';
import '../core/lan_discovery.dart';
import '../providers/agent_chat_provider.dart';

class RemotePairingModal extends ConsumerStatefulWidget {
  const RemotePairingModal({super.key});

  @override
  ConsumerState<RemotePairingModal> createState() => _RemotePairingModalState();
}

class _RemotePairingModalState extends ConsumerState<RemotePairingModal> {
  final TextEditingController _hostController = TextEditingController();
  final TextEditingController _tokenController = TextEditingController();
  bool _isConnecting = false;
  bool _isScanningLan = false;
  String? _scanStatus;
  List<DiscoveredHost> _discoveredHosts = [];
  String? _errorText;

  @override
  void initState() {
    super.initState();
    _loadSavedConfig();
  }

  Future<void> _handleLanScan() async {
    setState(() {
      _isScanningLan = true;
      _scanStatus = 'Detecting local network interfaces...';
      _errorText = null;
    });

    try {
      final hosts = await LanDiscoveryService.scanForDesktopHosts(
        onProgress: (status) {
          if (mounted) setState(() => _scanStatus = status);
        },
      );

      if (!mounted) return;
      setState(() {
        _isScanningLan = false;
        _discoveredHosts = hosts;
        if (hosts.isNotEmpty) {
          _hostController.text = hosts.first.wsUrl;
          _scanStatus = 'Found ${hosts.length} desktop engine(s)! Selected: ${hosts.first.ip}:${hosts.first.port}';
        } else {
          _scanStatus = 'No desktop engine found. Ensure desktop Meridian-X is running and on same Wi-Fi.';
        }
      });
    } catch (e) {
      if (!mounted) return;
      setState(() {
        _isScanningLan = false;
        _scanStatus = 'Scan error: $e';
      });
    }
  }


  Future<void> _loadSavedConfig() async {
    final savedUrl = await MeridianSecureStorage.getServerUrl();
    final savedToken = await MeridianSecureStorage.getAuthToken();
    if (savedUrl != null && savedUrl.isNotEmpty) {
      _hostController.text = savedUrl;
    }
    if (savedToken != null) _tokenController.text = savedToken;
  }

  String _deriveAuthKey(String inputPassword) {
    final trimmed = inputPassword.trim();
    if (trimmed.isEmpty) return '';
    if (RegExp(r'^[a-fA-F0-9]{64}$').hasMatch(trimmed)) {
      return trimmed;
    }
    return sha256.convert(utf8.encode(trimmed)).toString();
  }

  Future<void> _handleConnect() async {
    setState(() {
      _isConnecting = true;
      _errorText = null;
    });

    final rawUrl = _hostController.text.trim();
    final rawPassword = _tokenController.text.trim();
    final encryptedKey = _deriveAuthKey(rawPassword);

    if (rawUrl.isEmpty) {
      setState(() {
        _isConnecting = false;
        _errorText = 'Enter the desktop WebSocket endpoint URL.';
      });
      return;
    }

    final initialUri = WebSocketClient.normalizeWsUri(rawUrl);
    final targetUrls = <String>[initialUri.toString()];

    // Auto-probe candidate ports: 4132 (Main Engine), 8765 (Companion Bridge), 4133
    const candidatePorts = [4132, 8765, 4133];
    for (final p in candidatePorts) {
      if (p != initialUri.port) {
        targetUrls.add(initialUri.replace(port: p).toString());
      }
    }

    bool linked = false;
    String successfulUrl = initialUri.toString();

    for (final candidate in targetUrls) {
      try {
        await ref.read(agentChatProvider.notifier).connect(candidate, token: encryptedKey).timeout(const Duration(seconds: 4));
      } catch (_) {}
      await Future<void>.delayed(const Duration(milliseconds: 1000));
      if (!mounted) return;
      if (ref.read(agentChatProvider).isConnected) {
        linked = true;
        successfulUrl = candidate;
        break;
      }
    }

    setState(() => _isConnecting = false);

    if (linked) {
      await MeridianSecureStorage.savePairingConfig(serverUrl: successfulUrl, token: encryptedKey);
      if (mounted) Navigator.of(context).pop();
    } else {
      setState(() => _errorText = 'No handshake from desktop engine (tried ${targetUrls.join(", ")}). Check WiFi network, desktop firewall, and password.');
    }
  }

  Widget _buildPresetChip(String label, String url) {
    return ActionChip(
      label: Text(label, style: const TextStyle(fontSize: 11, color: MeridianTheme.cyanAccent)),
      backgroundColor: MeridianTheme.surfaceLight,
      side: BorderSide(color: MeridianTheme.cyanAccent.withValues(alpha: 0.3)),
      padding: const EdgeInsets.symmetric(horizontal: 4, vertical: 0),
      onPressed: () {
        setState(() {
          _hostController.text = url;
          _errorText = null;
        });
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Dialog(
      backgroundColor: MeridianTheme.surface,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      child: SingleChildScrollView(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                const Icon(Icons.qr_code_2, color: MeridianTheme.cyanAccent),
                const SizedBox(width: 10),
                const Text(
                  'DESKTOP ENGINE PAIRING',
                  style: TextStyle(
                    color: MeridianTheme.textPrimary,
                    fontSize: 16,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const Spacer(),
                IconButton(
                  onPressed: () => Navigator.of(context).pop(),
                  icon: const Icon(Icons.close, color: MeridianTheme.textSecondary),
                ),
              ],
            ),
            const SizedBox(height: 12),
            const Text(
              'Quick Presets',
              style: TextStyle(color: MeridianTheme.textSecondary, fontSize: 11),
            ),
            const SizedBox(height: 6),
            Wrap(
              spacing: 6,
              runSpacing: 6,
              children: [
                _buildPresetChip('Emulator (4132)', 'ws://10.0.2.2:4132/ws'),
                _buildPresetChip('Localhost (4132)', 'ws://127.0.0.1:4132/ws'),
                _buildPresetChip('Bridge (8765)', 'ws://127.0.0.1:8765/ws'),
                _buildPresetChip('Bridge Alt (4133)', 'ws://127.0.0.1:4133/ws'),
              ],
            ),
            const SizedBox(height: 12),
            SizedBox(
              width: double.infinity,
              child: OutlinedButton.icon(
                onPressed: _isScanningLan ? null : _handleLanScan,
                icon: _isScanningLan
                    ? const SizedBox(
                        width: 14,
                        height: 14,
                        child: CircularProgressIndicator(strokeWidth: 2, color: MeridianTheme.cyanAccent),
                      )
                    : const Icon(Icons.radar, size: 16, color: MeridianTheme.cyanAccent),
                label: Text(
                  _isScanningLan ? 'SCANNING LOCAL NETWORK...' : 'AUTO-DISCOVER DESKTOP (LAN SCAN)',
                  style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold, letterSpacing: 0.5),
                ),
                style: OutlinedButton.styleFrom(
                  foregroundColor: MeridianTheme.cyanAccent,
                  side: BorderSide(color: MeridianTheme.cyanAccent.withValues(alpha: 0.5)),
                  padding: const EdgeInsets.symmetric(vertical: 10),
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                ),
              ),
            ),
            if (_scanStatus != null) ...[
              const SizedBox(height: 6),
              Text(
                _scanStatus!,
                style: TextStyle(
                  color: _discoveredHosts.isNotEmpty ? MeridianTheme.emeraldGreen : MeridianTheme.textSecondary,
                  fontSize: 11,
                ),
              ),
            ],
            if (_discoveredHosts.isNotEmpty) ...[
              const SizedBox(height: 8),
              Wrap(
                spacing: 6,
                runSpacing: 6,
                children: _discoveredHosts.map((host) {
                  return ActionChip(
                    avatar: const Icon(Icons.check_circle, size: 14, color: MeridianTheme.emeraldGreen),
                    label: Text(host.label, style: const TextStyle(fontSize: 11, color: MeridianTheme.emeraldGreen)),
                    backgroundColor: MeridianTheme.surfaceLight,
                    side: BorderSide(color: MeridianTheme.emeraldGreen.withValues(alpha: 0.5)),
                    onPressed: () {
                      setState(() {
                        _hostController.text = host.wsUrl;
                        _errorText = null;
                      });
                    },
                  );
                }).toList(),
              ),
            ],
            const SizedBox(height: 14),
            const Text(
              'WebSocket Endpoint URL',
              style: TextStyle(color: MeridianTheme.textSecondary, fontSize: 12),
            ),
            const SizedBox(height: 6),
            TextField(
              controller: _hostController,
              decoration: InputDecoration(
                filled: true,
                fillColor: MeridianTheme.surfaceLight,
                hintText: 'ws://192.168.1.X:4132/ws',
                border: OutlineInputBorder(borderRadius: BorderRadius.circular(8), borderSide: BorderSide.none),
                prefixIcon: const Icon(Icons.wifi, size: 18, color: MeridianTheme.cyanAccent),
              ),
              style: const TextStyle(color: MeridianTheme.textPrimary, fontSize: 13),
            ),
            const SizedBox(height: 14),
            const Text(
              'Connection Password / API Key (SHA-256 Encrypted)',
              style: TextStyle(color: MeridianTheme.textSecondary, fontSize: 12),
            ),
            const SizedBox(height: 6),
            TextField(
              controller: _tokenController,
              obscureText: true,
              decoration: InputDecoration(
                filled: true,
                fillColor: MeridianTheme.surfaceLight,
                hintText: 'Enter Custom Password (or leave empty if none)',
                border: OutlineInputBorder(borderRadius: BorderRadius.circular(8), borderSide: BorderSide.none),
                prefixIcon: const Icon(Icons.key, size: 18, color: MeridianTheme.purpleAccent),
              ),
              style: const TextStyle(color: MeridianTheme.textPrimary, fontSize: 13),
            ),
            if (_errorText != null) ...[
              const SizedBox(height: 12),
              Text(
                _errorText!,
                style: const TextStyle(color: MeridianTheme.roseError, fontSize: 12),
              ),
            ],
            const SizedBox(height: 20),
            SizedBox(
              width: double.infinity,
              child: ElevatedButton.icon(
                onPressed: _isConnecting ? null : _handleConnect,
                icon: _isConnecting
                    ? const SizedBox(width: 16, height: 16, child: CircularProgressIndicator(strokeWidth: 2))
                    : const Icon(Icons.link, size: 18),
                label: Text(_isConnecting ? 'CONNECTING...' : 'ESTABLISH PAIRING LINK'),
                style: ElevatedButton.styleFrom(
                  backgroundColor: MeridianTheme.cyanAccent,
                  foregroundColor: Colors.black,
                  padding: const EdgeInsets.symmetric(vertical: 14),
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

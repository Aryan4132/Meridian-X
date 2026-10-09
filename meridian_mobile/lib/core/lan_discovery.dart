import 'dart:async';
import 'dart:io';

class DiscoveredHost {
  final String ip;
  final int port;
  final String wsUrl;
  final String label;

  const DiscoveredHost({
    required this.ip,
    required this.port,
    required this.wsUrl,
    required this.label,
  });

  @override
  String toString() => '$label ($wsUrl)';
}

/// Service to automatically discover Meridian-X desktop engines on local network.
class LanDiscoveryService {
  /// Generate prioritized candidate IP addresses from a given local IPv4.
  static List<String> getCandidateIps(String? localIp) {
    final Set<String> candidates = {'10.0.2.2', '127.0.0.1'};

    if (localIp != null && localIp.isNotEmpty && localIp != '127.0.0.1') {
      final parts = localIp.split('.');
      if (parts.length == 4) {
        final prefix = '${parts[0]}.${parts[1]}.${parts[2]}';
        // Priority router/server addresses
        candidates.add('$prefix.1');
        candidates.add('$prefix.2');
        candidates.add('$prefix.100');
        candidates.add('$prefix.101');
        candidates.add('$prefix.102');
        candidates.add('$prefix.50');
        candidates.add(localIp);

        // Scan neighboring host IPs around the device
        final currentHost = int.tryParse(parts[3]) ?? 1;
        for (int offset = -10; offset <= 10; offset++) {
          final host = currentHost + offset;
          if (host > 1 && host < 255) {
            candidates.add('$prefix.$host');
          }
        }
      }
    }

    return candidates.toList();
  }

  /// Get the active local IPv4 address of the device.
  static Future<String?> getLocalIpAddress() async {
    try {
      final interfaces = await NetworkInterface.list(
        type: InternetAddressType.IPv4,
        includeLoopback: false,
      );
      for (final interface in interfaces) {
        for (final addr in interface.addresses) {
          if (!addr.isLoopback && !addr.address.startsWith('169.254')) {
            return addr.address;
          }
        }
      }
    } catch (_) {
      // Platform may disallow interface enumeration; fall back to null
    }
    return null;
  }

  /// Probe a single IP and port using non-blocking socket connect.
  static Future<bool> probeSocket(String ip, int port, {Duration timeout = const Duration(milliseconds: 350)}) async {
    try {
      final socket = await Socket.connect(ip, port, timeout: timeout);
      socket.destroy();
      return true;
    } catch (_) {
      return false;
    }
  }

  /// Scan local network for running Meridian desktop engine instances.
  static Future<List<DiscoveredHost>> scanForDesktopHosts({
    List<int> ports = const [4132, 8765],
    Duration probeTimeout = const Duration(milliseconds: 400),
    void Function(String message)? onProgress,
  }) async {
    onProgress?.call('Detecting local Wi-Fi IP address...');
    final localIp = await getLocalIpAddress();
    final candidates = getCandidateIps(localIp);

    onProgress?.call('Scanning ${candidates.length} local subnet endpoints...');

    final List<DiscoveredHost> found = [];
    final List<Future<void>> probes = [];

    for (final ip in candidates) {
      for (final port in ports) {
        probes.add(() async {
          final isReachable = await probeSocket(ip, port, timeout: probeTimeout);
          if (isReachable) {
            final wsUrl = 'ws://$ip:$port/ws';
            final label = ip == '10.0.2.2'
                ? 'Emulator Host ($port)'
                : ip == '127.0.0.1'
                    ? 'Localhost ($port)'
                    : 'LAN Host $ip ($port)';
            found.add(DiscoveredHost(
              ip: ip,
              port: port,
              wsUrl: wsUrl,
              label: label,
            ));
          }
        }());
      }
    }

    await Future.wait(probes);
    onProgress?.call('Scan complete. Found ${found.length} desktop engine(s).');
    return found;
  }
}

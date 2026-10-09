import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:meridian_mobile/models/thought_step.dart';
import 'package:meridian_mobile/models/telemetry.dart';
import 'package:meridian_mobile/providers/agent_chat_provider.dart';
import 'package:meridian_mobile/core/websocket_client.dart';
import 'package:meridian_mobile/core/lan_discovery.dart';

void main() {
  group('Models Unit Tests', () {
    test('ThoughtStep json deserialization', () {
      final json = {
        'id': 'step-101',
        'step_number': 3,
        'title': 'Memory Index Lookup',
        'detail': 'Querying embedding vector store...',
        'status': 'completed',
        'confidence_score': 0.95,
      };

      final step = ThoughtStep.fromJson(json);

      expect(step.id, 'step-101');
      expect(step.stepNumber, 3);
      expect(step.title, 'Memory Index Lookup');
      expect(step.status, ThoughtStatus.completed);
      expect(step.confidenceScore, 0.95);
    });

    test('TelemetryData json deserialization', () {
      final json = {
        'cpu_percent': 18.4,
        'memory_mb': 512.0,
        'ping_ms': 12,
        'anti_hallucination': true,
        'model': 'Meridian-X Core v2.0',
      };

      final telemetry = TelemetryData.fromJson(json);

      expect(telemetry.cpuPercent, 18.4);
      expect(telemetry.pingMs, 12);
      expect(telemetry.antiHallucinationActive, isTrue);
      expect(telemetry.activeModel, 'Meridian-X Core v2.0');
    });

    test('ThoughtStep tolerates malformed timestamp and numbers', () {
      final step = ThoughtStep.fromJson({
        'title': 'Bad payload',
        'status': 'weird-status',
        'timestamp': 'not-a-date',
        'step_number': 'three',
        'confidence_score': 'high',
      });

      expect(step.title, 'Bad payload');
      expect(step.status, ThoughtStatus.completed);
      expect(step.stepNumber, 1);
      expect(step.confidenceScore, 1.0);
    });

    test('TelemetryData coerces string numbers', () {
      final telemetry = TelemetryData.fromJson({
        'cpu_percent': '45.5',
        'memory_mb': '1024',
        'ping_ms': '30',
      });

      expect(telemetry.cpuPercent, 45.5);
      expect(telemetry.memoryMb, 1024.0);
      expect(telemetry.pingMs, 30);
    });
  });

  group('AgentChatNotifier offline behavior', () {
    test('sendPrompt while disconnected appends a notice, not a prompt', () {
      final container = ProviderContainer();
      addTearDown(container.dispose);

      final notifier = container.read(agentChatProvider.notifier);
      expect(container.read(agentChatProvider).isConnected, isFalse);

      notifier.sendPrompt('hello?');
      final state = container.read(agentChatProvider);

      expect(state.messages, hasLength(1));
      expect(state.messages.first['sender'], 'agent');
      expect(state.thoughtSteps, isEmpty);
    });
  });

  group('WebSocketClient URL normalization', () {
    test('converts http to ws and appends /ws', () {
      final uri = WebSocketClient.normalizeWsUri('http://192.168.1.55:4132');
      expect(uri.scheme, 'ws');
      expect(uri.host, '192.168.1.55');
      expect(uri.port, 4132);
      expect(uri.path, '/ws');
    });

    test('converts https to wss', () {
      final uri = WebSocketClient.normalizeWsUri('https://meridian.internal/api/ws/mobile');
      expect(uri.scheme, 'wss');
      expect(uri.host, 'meridian.internal');
      expect(uri.path, '/api/ws/mobile');
    });

    test('attaches token and deviceId cleanly without duplicate question marks', () {
      final uri = WebSocketClient.normalizeWsUri('ws://10.0.2.2:4132/ws?foo=bar', token: 'secret123', deviceId: 'test_phone');
      expect(uri.queryParameters['foo'], 'bar');
      expect(uri.queryParameters['token'], 'secret123');
      expect(uri.queryParameters['device_id'], 'test_phone');
      expect(uri.toString().contains('?foo=bar&token=secret123&device_id=test_phone'), isTrue);
    });

    test('defaults empty input to emulator localhost', () {
      final uri = WebSocketClient.normalizeWsUri('');
      expect(uri.toString(), 'ws://10.0.2.2:4132/ws');
    });
  });

  group('LanDiscoveryService Unit Tests', () {
    test('generates emulator and localhost candidates for empty/null IP', () {
      final candidates = LanDiscoveryService.getCandidateIps(null);
      expect(candidates, contains('10.0.2.2'));
      expect(candidates, contains('127.0.0.1'));
    });

    test('generates subnet candidates for active Wi-Fi LAN IP', () {
      final candidates = LanDiscoveryService.getCandidateIps('192.168.1.45');
      expect(candidates, contains('10.0.2.2'));
      expect(candidates, contains('127.0.0.1'));
      expect(candidates, contains('192.168.1.1'));
      expect(candidates, contains('192.168.1.2'));
      expect(candidates, contains('192.168.1.50'));
      expect(candidates, contains('192.168.1.100'));
      expect(candidates, contains('192.168.1.45'));
    });

    test('DiscoveredHost format and string representation', () {
      const host = DiscoveredHost(
        ip: '192.168.1.100',
        port: 4132,
        wsUrl: 'ws://192.168.1.100:4132/ws',
        label: 'LAN Host 192.168.1.100 (4132)',
      );
      expect(host.ip, '192.168.1.100');
      expect(host.port, 4132);
      expect(host.wsUrl, 'ws://192.168.1.100:4132/ws');
      expect(host.toString(), contains('LAN Host 192.168.1.100 (4132) (ws://192.168.1.100:4132/ws)'));
    });
  });
}


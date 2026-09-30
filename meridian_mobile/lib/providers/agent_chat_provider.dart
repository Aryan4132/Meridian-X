import 'dart:async';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../core/websocket_client.dart';
import '../models/thought_step.dart';
import '../models/telemetry.dart';

class AgentState {
  final bool isConnected;
  final String? deviceId;
  final TelemetryData telemetry;
  final List<ThoughtStep> thoughtSteps;
  final List<Map<String, dynamic>> messages;
  final String? activePrompt;

  const AgentState({
    this.isConnected = false,
    this.deviceId,
    this.telemetry = const TelemetryData(),
    this.thoughtSteps = const [],
    this.messages = const [],
    this.activePrompt,
  });

  AgentState copyWith({
    bool? isConnected,
    String? deviceId,
    TelemetryData? telemetry,
    List<ThoughtStep>? thoughtSteps,
    List<Map<String, dynamic>>? messages,
    String? activePrompt,
  }) {
    return AgentState(
      isConnected: isConnected ?? this.isConnected,
      deviceId: deviceId ?? this.deviceId,
      telemetry: telemetry ?? this.telemetry,
      thoughtSteps: thoughtSteps ?? this.thoughtSteps,
      messages: messages ?? this.messages,
      activePrompt: activePrompt ?? this.activePrompt,
    );
  }
}

class AgentChatNotifier extends StateNotifier<AgentState> {
  final WebSocketClient _wsClient = WebSocketClient();
  Timer? _pingTimer;
  int _stepCounter = 0;

  AgentChatNotifier() : super(const AgentState()) {
    _wsClient.stream.listen(_handleIncomingMessage);
  }

  Future<void> connect(String wsUrl, {String? token, String? deviceId}) async {
    final success = await _wsClient.connect(wsUrl, token: token, deviceId: deviceId ?? 'mobile_companion');
    if (!success) {
      _appendSystemMessage('Connection failed: could not open WebSocket to $wsUrl');
      return;
    }
    // Mark tentatively connected; handshake_ack from the server confirms.
    state = state.copyWith(isConnected: true, deviceId: deviceId ?? 'mobile_companion');
    _startPingLoop();
  }

  Future<void> disconnect() async {
    _pingTimer?.cancel();
    await _wsClient.disconnect();
    state = state.copyWith(isConnected: false);
  }

  void _startPingLoop() {
    _pingTimer?.cancel();
    _pingTimer = Timer.periodic(const Duration(seconds: 25), (_) {
      if (state.isConnected) {
        _wsClient.sendMessage({'type': 'ping'});
      }
    });
  }

  void sendPrompt(String text) {
    if (text.trim().isEmpty) return;
    if (!state.isConnected) {
      _appendSystemMessage('Not connected. Open Remote Pairing to link the desktop engine.');
      return;
    }

    final userMsg = {'sender': 'user', 'text': text, 'timestamp': DateTime.now().toIso8601String()};
    final newMessages = List<Map<String, dynamic>>.from(state.messages)..add(userMsg);

    _stepCounter += 1;
    final newStep = ThoughtStep(
      id: DateTime.now().millisecondsSinceEpoch.toString(),
      stepNumber: _stepCounter,
      title: 'Analyzing Prompt',
      detail: text,
      status: ThoughtStatus.running,
      timestamp: DateTime.now(),
    );

    state = state.copyWith(
      messages: newMessages,
      thoughtSteps: [newStep, ...state.thoughtSteps],
      activePrompt: text,
    );

    _wsClient.sendMessage({
      'type': 'user_prompt',
      'content': text,
    });
  }

  void _appendAgentMessage(String text) {
    final msg = {'sender': 'agent', 'text': text, 'timestamp': DateTime.now().toIso8601String()};
    final newMessages = List<Map<String, dynamic>>.from(state.messages)..add(msg);
    state = state.copyWith(messages: newMessages);
  }

  void _appendSystemMessage(String text) {
    _appendAgentMessage('⚙️ $text');
  }

  void _markDisconnected([String? reason]) {
    _pingTimer?.cancel();
    if (state.isConnected) {
      state = state.copyWith(isConnected: false);
    }
    if (reason != null) {
      _appendSystemMessage(reason);
    }
  }

  void _handleIncomingMessage(Map<String, dynamic> msg) {
    final type = msg['type'];
    if (type == 'telemetry') {
      state = state.copyWith(telemetry: TelemetryData.fromJson(msg['data'] ?? {}));
    } else if (type == 'thought_step') {
      final step = ThoughtStep.fromJson(msg['data'] ?? msg);
      final updatedSteps = List<ThoughtStep>.from(state.thoughtSteps)..insert(0, step);
      state = state.copyWith(thoughtSteps: updatedSteps);
    } else if (type == 'agent_reply') {
      _appendAgentMessage(msg['content']?.toString() ?? '');
    } else if (type == 'handshake_ack') {
      state = state.copyWith(
        isConnected: true,
        deviceId: msg['device_id']?.toString() ?? state.deviceId,
      );
      _startPingLoop();
    } else if (type == 'pong') {
      final telemetry = msg['telemetry'];
      if (telemetry is Map<String, dynamic>) {
        state = state.copyWith(telemetry: TelemetryData.fromJson(telemetry));
      }
    } else if (type == 'ack') {
      // Transport-level acknowledgement — no UI action needed.
    } else if (type == 'command_ack') {
      final response = msg['response'] ?? msg['message'] ?? msg['status'] ?? 'received';
      _appendAgentMessage('✅ Command ${msg['command'] ?? ''}: $response'.trim());
    } else if (type == 'command_error') {
      _markDisconnected();
      _appendSystemMessage('Pairing rejected: ${msg['error'] ?? 'unauthorized'}. Check the connection password.');
    } else if (type == 'backend_status') {
      _appendSystemMessage('Backend ${msg['status'] ?? 'unknown'}: ${msg['message'] ?? ''}'.trim());
    } else if (type == 'error') {
      _markDisconnected('Socket error: ${msg['message'] ?? 'unknown'}');
    } else if (type == 'disconnected' || type == 'raw') {
      if (type == 'disconnected') {
        _markDisconnected('Disconnected from desktop engine.');
      }
    }
  }

  @override
  void dispose() {
    _pingTimer?.cancel();
    _wsClient.dispose();
    super.dispose();
  }
}

final agentChatProvider = StateNotifierProvider<AgentChatNotifier, AgentState>((ref) {
  return AgentChatNotifier();
});

import 'dart:async';
import 'dart:convert';

import 'package:web_socket_channel/web_socket_channel.dart';

class WebSocketClient {
  WebSocketChannel? _channel;
  final StreamController<Map<String, dynamic>> _messageController = StreamController<Map<String, dynamic>>.broadcast();
  bool _isConnected = false;

  bool get isConnected => _isConnected;
  Stream<Map<String, dynamic>> get stream => _messageController.stream;

  /// Normalizes user-input URL strings into valid WebSocket URIs.
  /// Converts http(s) to ws(s), adds /ws path if omitted, and safely sets query params.
  static Uri normalizeWsUri(String inputUrl, {String? token, String? deviceId}) {
    String trimmed = inputUrl.trim();
    if (trimmed.isEmpty) {
      trimmed = 'ws://10.0.2.2:4132/ws';
    }

    // Convert HTTP schemas to WebSocket schemas
    if (trimmed.startsWith('https://')) {
      trimmed = 'wss://${trimmed.substring(8)}';
    } else if (trimmed.startsWith('http://')) {
      trimmed = 'ws://${trimmed.substring(7)}';
    } else if (!trimmed.startsWith('ws://') && !trimmed.startsWith('wss://')) {
      trimmed = 'ws://$trimmed';
    }

    Uri parsed = Uri.parse(trimmed);

    // If path is empty or root '/', default to '/ws'
    String path = parsed.path;
    if (path.isEmpty || path == '/') {
      path = '/ws';
    }

    final Map<String, String> queryParams = Map<String, String>.from(parsed.queryParameters);
    if (token != null && token.isNotEmpty) {
      queryParams['token'] = token;
    }
    if (deviceId != null && deviceId.isNotEmpty && !queryParams.containsKey('device_id')) {
      queryParams['device_id'] = deviceId;
    }

    return parsed.replace(
      path: path,
      queryParameters: queryParams.isNotEmpty ? queryParams : null,
    );
  }

  Future<bool> connect(String wsUrl, {String? token, String? deviceId}) async {
    try {
      await disconnect();
      final Uri uri = normalizeWsUri(wsUrl, token: token, deviceId: deviceId);
      _channel = WebSocketChannel.connect(uri);

      _channel!.stream.listen(
        (data) {
          try {
            final Map<String, dynamic> decoded = jsonDecode(data.toString());
            _messageController.add(decoded);
          } catch (e) {
            _messageController.add({'type': 'raw', 'content': data.toString()});
          }
        },
        onError: (error) {
          _isConnected = false;
          _messageController.add({'type': 'error', 'message': error.toString()});
        },
        onDone: () {
          _isConnected = false;
          _messageController.add({'type': 'disconnected'});
        },
      );

      // Verify connection handshake completion with timeout
      await _channel!.ready.timeout(const Duration(seconds: 4));
      _isConnected = true;
      return true;
    } catch (e) {
      _isConnected = false;
      await disconnect();
      return false;
    }
  }

  void sendMessage(Map<String, dynamic> message) {
    if (_channel != null && _isConnected) {
      _channel!.sink.add(jsonEncode(message));
    }
  }

  Future<void> disconnect() async {
    _isConnected = false;
    try {
      await _channel?.sink.close().timeout(const Duration(seconds: 2));
    } catch (_) {
      // Stale or half-open socket — safely drop it and continue.
    } finally {
      _channel = null;
    }
  }

  void dispose() {
    disconnect();
    _messageController.close();
  }
}

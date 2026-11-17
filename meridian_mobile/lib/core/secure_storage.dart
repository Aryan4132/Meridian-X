import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class MeridianSecureStorage {
  static const _storage = FlutterSecureStorage();
  static final Map<String, String> _memFallback = {};

  static const String _keyServerUrl = 'meridian_server_url';
  static const String _keyAuthToken = 'meridian_auth_token';

  static Future<void> savePairingConfig({required String serverUrl, String token = ''}) async {
    await write(_keyServerUrl, serverUrl);
    if (token.isNotEmpty) {
      await write(_keyAuthToken, token);
    } else {
      await delete(_keyAuthToken);
    }
  }

  static Future<void> saveServerUrl(String serverUrl) async {
    await write(_keyServerUrl, serverUrl);
  }

  static Future<String?> getServerUrl() async {
    return await read(_keyServerUrl);
  }

  static Future<String?> getAuthToken() async {
    return await read(_keyAuthToken);
  }

  static Future<void> clearPairingConfig() async {
    await delete(_keyServerUrl);
    await delete(_keyAuthToken);
  }

  static Future<void> write(String key, String value) async {
    _memFallback[key] = value;
    try {
      await _storage.write(key: key, value: value);
    } catch (_) {
      // Ignored for unit test environments
    }
  }

  static Future<String?> read(String key) async {
    try {
      final val = await _storage.read(key: key);
      if (val != null) return val;
    } catch (_) {
      // Ignored for unit test environments
    }
    return _memFallback[key];
  }

  static Future<void> delete(String key) async {
    _memFallback.remove(key);
    try {
      await _storage.delete(key: key);
    } catch (_) {
      // Ignored for unit test environments
    }
  }
}

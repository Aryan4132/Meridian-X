import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class MeridianSecureStorage {
  static const _storage = FlutterSecureStorage();

  static const String _keyServerUrl = 'meridian_server_url';
  static const String _keyAuthToken = 'meridian_auth_token';

  static Future<void> savePairingConfig({required String serverUrl, String token = ''}) async {
    await _storage.write(key: _keyServerUrl, value: serverUrl);
    if (token.isNotEmpty) {
      await _storage.write(key: _keyAuthToken, value: token);
    } else {
      await _storage.delete(key: _keyAuthToken);
    }
  }

  static Future<void> saveServerUrl(String serverUrl) async {
    await _storage.write(key: _keyServerUrl, value: serverUrl);
  }

  static Future<String?> getServerUrl() async {
    return await _storage.read(key: _keyServerUrl);
  }

  static Future<String?> getAuthToken() async {
    return await _storage.read(key: _keyAuthToken);
  }

  static Future<void> clearPairingConfig() async {
    await _storage.delete(key: _keyServerUrl);
    await _storage.delete(key: _keyAuthToken);
  }
}

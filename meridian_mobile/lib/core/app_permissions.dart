import 'package:permission_handler/permission_handler.dart';

/// Central runtime-permission gate for mic/camera features.
///
/// Fail-soft by design: any unexpected error returns `true` so desktop
/// flows keep working on platforms where the plugin is unavailable
/// (desktop/web builds), while a real user denial returns `false`.
class AppPermissions {
  static Future<bool> requestMicrophone() async {
    try {
      final status = await Permission.microphone.status;
      if (status.isGranted || status.isLimited) return true;
      final result = await Permission.microphone.request();
      return result.isGranted || result.isLimited;
    } catch (_) {
      return true;
    }
  }

  static Future<bool> requestCamera() async {
    try {
      final status = await Permission.camera.status;
      if (status.isGranted || status.isLimited) return true;
      final result = await Permission.camera.request();
      return result.isGranted || result.isLimited;
    } catch (_) {
      return true;
    }
  }
}

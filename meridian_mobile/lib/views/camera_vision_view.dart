import 'package:flutter/material.dart';
import '../core/theme.dart';

class CameraVisionView extends StatefulWidget {
  const CameraVisionView({super.key});

  @override
  State<CameraVisionView> createState() => _CameraVisionViewState();
}

class _CameraVisionViewState extends State<CameraVisionView> {
  bool _isAnalyzing = false;

  void _triggerVisionAnalysis() {
    setState(() => _isAnalyzing = true);
    Future.delayed(const Duration(seconds: 2), () {
      if (mounted) {
        setState(() => _isAnalyzing = false);
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(
            content: Text('Camera Vision Payload transmitted to Meridian Desktop Engine'),
            backgroundColor: MeridianTheme.emeraldGreen,
          ),
        );
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 220,
      margin: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.black,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: MeridianTheme.cyanAccent.withValues(alpha: 0.5), width: 1.5),
      ),
      child: Stack(
        children: [
          // Camera viewport placeholder frame
          Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(
                  Icons.qr_code_scanner,
                  size: 48,
                  color: MeridianTheme.cyanAccent.withValues(alpha: 0.7),
                ),
                const SizedBox(height: 12),
                const Text(
                  'VISION SCANNER VIEWPORT',
                  style: TextStyle(
                    color: MeridianTheme.textPrimary,
                    fontSize: 14,
                    fontWeight: FontWeight.bold,
                    letterSpacing: 1.1,
                  ),
                ),
                const SizedBox(height: 4),
                const Text(
                  'Point camera at whiteboard or server terminal',
                  style: TextStyle(
                    color: MeridianTheme.textSecondary,
                    fontSize: 12,
                  ),
                ),
              ],
            ),
          ),

          // Analysis overlay button
          Positioned(
            bottom: 12,
            right: 12,
            child: ElevatedButton.icon(
              onPressed: _isAnalyzing ? null : _triggerVisionAnalysis,
              icon: _isAnalyzing
                  ? const SizedBox(
                      width: 14,
                      height: 14,
                      child: CircularProgressIndicator(strokeWidth: 2, color: Colors.white),
                    )
                  : const Icon(Icons.camera_alt, size: 16),
              label: Text(_isAnalyzing ? 'ANALYZING...' : 'ANALYZE FRAME'),
              style: ElevatedButton.styleFrom(
                backgroundColor: MeridianTheme.cyanAccent,
                foregroundColor: Colors.black,
                padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

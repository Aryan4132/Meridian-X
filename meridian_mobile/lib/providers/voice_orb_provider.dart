import 'dart:async';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../core/app_permissions.dart';

enum OrbListeningState { idle, listening, processing, speaking }

class VoiceOrbState {
  final OrbListeningState state;
  final double amplitude;
  final bool isMicMuted;
  final bool permissionDenied;

  const VoiceOrbState({
    this.state = OrbListeningState.idle,
    this.amplitude = 0.3,
    this.isMicMuted = false,
    this.permissionDenied = false,
  });

  VoiceOrbState copyWith({
    OrbListeningState? state,
    double? amplitude,
    bool? isMicMuted,
    bool? permissionDenied,
  }) {
    return VoiceOrbState(
      state: state ?? this.state,
      amplitude: amplitude ?? this.amplitude,
      isMicMuted: isMicMuted ?? this.isMicMuted,
      permissionDenied: permissionDenied ?? this.permissionDenied,
    );
  }
}

class VoiceOrbNotifier extends StateNotifier<VoiceOrbState> {
  Timer? _animTimer;

  VoiceOrbNotifier() : super(const VoiceOrbState());

  void toggleListening() {
    if (state.state == OrbListeningState.idle) {
      startListening();
    } else {
      stopListening();
    }
  }

  void startListening() async {
    final granted = await AppPermissions.requestMicrophone();
    if (!granted) {
      state = state.copyWith(state: OrbListeningState.idle, permissionDenied: true);
      return;
    }
    state = state.copyWith(state: OrbListeningState.listening, permissionDenied: false);
    _animTimer?.cancel();
    _animTimer = Timer.periodic(const Duration(milliseconds: 100), (timer) {
      // Simulate live audio waveform amplitude response
      final double nextAmp = (state.amplitude + 0.15) % 0.85 + 0.15;
      state = state.copyWith(amplitude: nextAmp);
    });
  }

  void stopListening() {
    _animTimer?.cancel();
    state = state.copyWith(state: OrbListeningState.idle, amplitude: 0.3);
  }

  void toggleMute() {
    state = state.copyWith(isMicMuted: !state.isMicMuted);
  }

  @override
  void dispose() {
    _animTimer?.cancel();
    super.dispose();
  }
}

final voiceOrbProvider = StateNotifierProvider<VoiceOrbNotifier, VoiceOrbState>((ref) {
  return VoiceOrbNotifier();
});

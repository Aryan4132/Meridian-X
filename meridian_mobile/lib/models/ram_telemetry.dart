import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

enum SafetyLevel {
  optimal,
  tight,
  danger;

  String get label {
    switch (this) {
      case SafetyLevel.optimal:
        return 'Optimal';
      case SafetyLevel.tight:
        return 'Tight';
      case SafetyLevel.danger:
        return 'OOM Risk';
    }
  }

  Color get color {
    switch (this) {
      case SafetyLevel.optimal:
        return const Color(0xFF10B981);
      case SafetyLevel.tight:
        return const Color(0xFFF59E0B);
      case SafetyLevel.danger:
        return const Color(0xFFEF4444);
    }
  }
}

class RamTelemetry {
  final double totalRamMb;
  final double freeRamMb;
  final double osReserveMb;

  const RamTelemetry({
    this.totalRamMb = 6144.0, // Default 6GB phone
    this.freeRamMb = 3200.0,  // Default 3.2GB available
    this.osReserveMb = 1200.0, // 1.2GB reserved for OS & background services
  });

  double get usedRamMb => (totalRamMb - freeRamMb).clamp(0.0, totalRamMb);
  double get usableAiBudgetMb => (freeRamMb - osReserveMb).clamp(0.0, totalRamMb);

  double calculateRequiredRam({
    required double modelGgufMb,
    required int contextLength,
    double kvMultiplier = 0.28,
    double appOverheadMb = 250.0,
  }) {
    if (modelGgufMb <= 0) return 0.0; // Cloud models use 0MB local RAM
    final kvCacheMb = (contextLength * kvMultiplier);
    return modelGgufMb + kvCacheMb + appOverheadMb;
  }

  SafetyEvaluation evaluateModelSafety({
    required double modelGgufMb,
    required int contextLength,
    bool isCloud = false,
  }) {
    if (isCloud || modelGgufMb <= 0) {
      return const SafetyEvaluation(
        safetyLevel: SafetyLevel.optimal,
        requiredRamMb: 0.0,
        headroomMb: 99999.0,
        warningMessage: 'Cloud API: Zero on-device model RAM required',
      );
    }

    final requiredMb = calculateRequiredRam(
      modelGgufMb: modelGgufMb,
      contextLength: contextLength,
    );
    final remainingAfterModel = freeRamMb - requiredMb;
    final headroomMb = remainingAfterModel - osReserveMb;

    if (remainingAfterModel <= 200.0 || headroomMb < -300.0) {
      return SafetyEvaluation(
        safetyLevel: SafetyLevel.danger,
        requiredRamMb: requiredMb,
        headroomMb: headroomMb,
        warningMessage: 'Exceeds safe limits. Risk of OS killing the app (OOM).',
      );
    } else if (headroomMb < 300.0) {
      return SafetyEvaluation(
        safetyLevel: SafetyLevel.tight,
        requiredRamMb: requiredMb,
        headroomMb: headroomMb,
        warningMessage: 'Tight RAM. Background apps may reload.',
      );
    } else {
      return SafetyEvaluation(
        safetyLevel: SafetyLevel.optimal,
        requiredRamMb: requiredMb,
        headroomMb: headroomMb,
        warningMessage: 'Safe to run with optimal multitasking headroom.',
      );
    }
  }

  RamTelemetry copyWith({
    double? totalRamMb,
    double? freeRamMb,
    double? osReserveMb,
  }) {
    return RamTelemetry(
      totalRamMb: totalRamMb ?? this.totalRamMb,
      freeRamMb: freeRamMb ?? this.freeRamMb,
      osReserveMb: osReserveMb ?? this.osReserveMb,
    );
  }
}

class SafetyEvaluation {
  final SafetyLevel safetyLevel;
  final double requiredRamMb;
  final double headroomMb;
  final String warningMessage;

  const SafetyEvaluation({
    required this.safetyLevel,
    required this.requiredRamMb,
    required this.headroomMb,
    required this.warningMessage,
  });
}

class RamTelemetryState {
  final RamTelemetry telemetry;
  final int selectedContextLength; // 512, 1024, 2048, 4096

  const RamTelemetryState({
    this.telemetry = const RamTelemetry(),
    this.selectedContextLength = 2048,
  });

  RamTelemetryState copyWith({
    RamTelemetry? telemetry,
    int? selectedContextLength,
  }) {
    return RamTelemetryState(
      telemetry: telemetry ?? this.telemetry,
      selectedContextLength: selectedContextLength ?? this.selectedContextLength,
    );
  }
}

class RamTelemetryController extends StateNotifier<RamTelemetryState> {
  RamTelemetryController() : super(const RamTelemetryState());

  void setContextLength(int length) {
    state = state.copyWith(selectedContextLength: length.clamp(512, 8192));
  }

  void updateTelemetry({required double totalRamMb, required double freeRamMb}) {
    state = state.copyWith(
      telemetry: state.telemetry.copyWith(
        totalRamMb: totalRamMb,
        freeRamMb: freeRamMb,
      ),
    );
  }
}

final ramTelemetryProvider =
    StateNotifierProvider<RamTelemetryController, RamTelemetryState>((ref) {
  return RamTelemetryController();
});

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:meridian_mobile/models/ram_telemetry.dart';
import 'package:meridian_mobile/core/theme_engine.dart';
import 'package:meridian_mobile/core/model_engines.dart';
import 'package:meridian_mobile/core/mobile_tool_runner.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  group('RAM Telemetry & Hardware Safety Unit Tests', () {
    test('Calculates used RAM and usable AI budget correctly', () {
      const ram = RamTelemetry(
        totalRamMb: 8192.0,
        freeRamMb: 4096.0,
        osReserveMb: 1200.0,
      );

      expect(ram.usedRamMb, 4096.0);
      expect(ram.usableAiBudgetMb, 4096.0 - 1200.0);
    });

    test('calculateRequiredRam scales dynamically with context length', () {
      const ram = RamTelemetry();

      final ramAt512 = ram.calculateRequiredRam(modelGgufMb: 1000.0, contextLength: 512);
      final ramAt2048 = ram.calculateRequiredRam(modelGgufMb: 1000.0, contextLength: 2048);
      final ramAt4096 = ram.calculateRequiredRam(modelGgufMb: 1000.0, contextLength: 4096);

      expect(ramAt512, lessThan(ramAt2048));
      expect(ramAt2048, lessThan(ramAt4096));
      expect(ramAt2048, closeTo(1000.0 + (2048 * 0.28) + 250.0, 0.1));
    });

    test('evaluateModelSafety flags optimal, tight, and danger thresholds', () {
      // Phone with 3.5GB free, 1.2GB reserve -> 2.3GB budget
      const ram = RamTelemetry(totalRamMb: 8192, freeRamMb: 3500, osReserveMb: 1200);

      // Lightweight 400MB model -> Optimal
      final evalOptimal = ram.evaluateModelSafety(modelGgufMb: 400.0, contextLength: 1024);
      expect(evalOptimal.safetyLevel, SafetyLevel.optimal);

      // 1400MB model -> Tight (headroom between -300MB and +300MB)
      final evalTight = ram.evaluateModelSafety(modelGgufMb: 1400.0, contextLength: 2048);
      expect(evalTight.safetyLevel, SafetyLevel.tight);

      // Huge 4500MB model on 3.5GB free -> Danger (OOM Risk)
      final evalDanger = ram.evaluateModelSafety(modelGgufMb: 4500.0, contextLength: 4096);
      expect(evalDanger.safetyLevel, SafetyLevel.danger);
    });

    test('Cloud models consume zero local RAM and evaluate as optimal', () {
      const ram = RamTelemetry(totalRamMb: 2048, freeRamMb: 400, osReserveMb: 1200);
      final eval = ram.evaluateModelSafety(modelGgufMb: 0.0, contextLength: 4096, isCloud: true);

      expect(eval.safetyLevel, SafetyLevel.optimal);
      expect(eval.requiredRamMb, 0.0);
    });
  });

  group('Theme Engine & Design Tokens Unit Tests', () {
    test('All 4 curated theme palettes contain non-null colors', () {
      for (final palette in AppThemePalette.values) {
        final colors = ThemePalettes.getColors(palette);
        expect(colors.background, isNotNull);
        expect(colors.surface, isNotNull);
        expect(colors.primaryAccent, isNotNull);
        expect(colors.textPrimary, isNotNull);
      }
    });

    test('Custom accent override properly replaces primaryAccent', () {
      const state = ThemeState(palette: AppThemePalette.oledAbyss);
      expect(state.colors.primaryAccent, ThemePalettes.oledAbyss.primaryAccent);

      const customColor = Color(0xFFFF0055);
      final overridden = state.copyWith(customAccent: customColor);
      expect(overridden.colors.primaryAccent, customColor);

      final cleared = overridden.copyWith(clearCustomAccent: true);
      expect(cleared.colors.primaryAccent, ThemePalettes.oledAbyss.primaryAccent);
    });
  });

  group('Tri-Engine & Model Catalog Unit Tests', () {
    test('Catalog contains valid on-device and cloud models', () {
      expect(CuratedModelsCatalog.onDeviceModels.isNotEmpty, isTrue);
      expect(CuratedModelsCatalog.cloudModels.isNotEmpty, isTrue);
      expect(CuratedModelsCatalog.desktopBridgeModel.engineType, ModelEngineType.desktopBridge);

      for (final m in CuratedModelsCatalog.onDeviceModels) {
        expect(m.engineType, ModelEngineType.onDeviceLlama);
        expect(m.modelGgufMb, greaterThan(0));
      }

      for (final m in CuratedModelsCatalog.cloudModels) {
        expect(m.engineType, ModelEngineType.cloudApi);
        expect(m.modelGgufMb, 0.0);
      }
    });

    test('EngineManagerState builds correct engine instance', () {
      const state = EngineManagerState(
        activeModel: CuratedModelsCatalog.desktopBridgeModel,
        onDeviceModels: CuratedModelsCatalog.onDeviceModels,
        cloudModels: CuratedModelsCatalog.cloudModels,
        desktopModel: CuratedModelsCatalog.desktopBridgeModel,
      );

      final desktopEngine = state.buildEngine();
      expect(desktopEngine.engineType, ModelEngineType.desktopBridge);

      final onDeviceState = state.copyWith(activeModel: CuratedModelsCatalog.onDeviceModels.first);
      expect(onDeviceState.buildEngine().engineType, ModelEngineType.onDeviceLlama);

      final cloudState = state.copyWith(activeModel: CuratedModelsCatalog.cloudModels.first);
      expect(cloudState.buildEngine().engineType, ModelEngineType.cloudApi);
    });

    test('EngineManagerController downloads and cancels models properly', () async {
      final controller = EngineManagerController();
      final modelToDownload = CuratedModelsCatalog.onDeviceModels.firstWhere((m) => !m.isDownloaded);

      // Start download
      await controller.startDownload(modelToDownload.id);
      final downloadedModel = controller.state.onDeviceModels.firstWhere((m) => m.id == modelToDownload.id);
      expect(downloadedModel.isDownloaded, isTrue);
      expect(downloadedModel.downloadProgress, 1.0);

      // Cancel resets model state
      controller.cancelDownload(modelToDownload.id);
      final resetModel = controller.state.onDeviceModels.firstWhere((m) => m.id == modelToDownload.id);
      expect(resetModel.isDownloaded, isFalse);
      expect(resetModel.downloadProgress, 0.0);
    });
  });

  group('Mobile Tool Runner & Intent Router Unit Tests', () {
    test('Intent router separates PC automation from mobile local tasks', () {
      expect(MobileToolRunner.classifyTarget('commit changes and push git branch'), ToolTarget.desktopRemote);
      expect(MobileToolRunner.classifyTarget('run docker compose up in terminal'), ToolTarget.desktopRemote);
      expect(MobileToolRunner.classifyTarget('open browser_use to search flights'), ToolTarget.desktopRemote);

      expect(MobileToolRunner.classifyTarget('what is the weather today?'), ToolTarget.mobileLocal);
      expect(MobileToolRunner.classifyTarget('check phone battery and connectivity'), ToolTarget.mobileLocal);
      expect(MobileToolRunner.classifyTarget('summarize recent notes'), ToolTarget.mobileLocal);
    });

    test('executeSearch and getMobileDeviceStatus return valid outputs', () async {
      final searchRes = await MobileToolRunner.executeSearch('quantum computing');
      expect(searchRes.success, isTrue);
      expect(searchRes.output, contains('quantum computing'));

      final statusRes = await MobileToolRunner.getMobileDeviceStatus();
      expect(statusRes.success, isTrue);
      expect(statusRes.data?['battery_level'], 84);
    });
  });
}

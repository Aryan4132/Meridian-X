import 'package:flutter_test/flutter_test.dart';
import 'package:meridian_mobile/core/model_engines.dart';
import 'package:meridian_mobile/providers/agent_chat_provider.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  group('Real Engines Execution & Downloader Tests', () {
    test('GGUF model file directory and header verification', () async {
      final dir = EngineManagerController.getModelsDirectory();
      expect(dir.existsSync(), isTrue);

      final modelFile = EngineManagerController.getModelFile('test_model');
      expect(modelFile.path, contains('meridian_models'));

      // Clean up previous test artifact if exists
      if (modelFile.existsSync()) modelFile.deleteSync();

      // Write valid GGUF binary magic bytes (0x47475546 = 'GGUF')
      final header = <int>[
        0x47, 0x47, 0x55, 0x46, // 'GGUF' magic
        0x03, 0x00, 0x00, 0x00, // version 3
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, // tensor_count
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, // metadata_kv_count
      ];
      modelFile.writeAsBytesSync(header);

      expect(modelFile.existsSync(), isTrue);
      final readBytes = modelFile.readAsBytesSync();
      expect(readBytes.length, 24);
      final magic = String.fromCharCodes(readBytes.sublist(0, 4));
      expect(magic, 'GGUF');

      // Clean up
      modelFile.deleteSync();
      expect(modelFile.existsSync(), isFalse);
    });

    test('CloudApiEngine emits clear error message when API key is missing', () async {
      const model = ModelDescriptor(
        id: 'gemini-1.5-flash',
        name: 'Gemini 1.5 Flash',
        engineType: ModelEngineType.cloudApi,
        cloudProvider: CloudProvider.gemini,
        parameterSize: 'Cloud',
        quantization: 'N/A',
        downloadSizeMb: 0.0,
        modelGgufMb: 0.0,
        description: 'Google cloud model',
      );

      final engineWithoutKey = CloudApiEngine(model, apiKey: null);
      final tokens = await engineWithoutKey.streamInference(prompt: 'Hello world').toList();
      final fullOutput = tokens.join('');

      expect(fullOutput, contains('Error - No API key configured'));
    });

    test('OnDeviceLlamaEngine warns when weights are missing from device storage', () async {
      const model = ModelDescriptor(
        id: 'uninstalled-model',
        name: 'Uninstalled Model',
        engineType: ModelEngineType.onDeviceLlama,
        parameterSize: '1.0B',
        quantization: 'Q4_K_M',
        downloadSizeMb: 500.0,
        modelGgufMb: 600.0,
        description: 'Testing uninstalled model',
        isDownloaded: false,
      );

      final engine = OnDeviceLlamaEngine(model);
      final tokens = await engine.streamInference(prompt: 'Hello').toList();
      final output = tokens.join('');

      expect(output, contains('not found on device storage'));
    });

    test('AgentChatNotifier executes standalone chat when active engine is CloudApi or OnDevice', () async {
      final chatNotifier = AgentChatNotifier();
      expect(chatNotifier.state.isConnected, isFalse);

      // Testing cloud engine with mocked response
      const cloudModel = ModelDescriptor(
        id: 'mock-cloud',
        name: 'Mock Cloud',
        engineType: ModelEngineType.cloudApi,
        cloudProvider: CloudProvider.gemini,
        parameterSize: 'Cloud',
        quantization: 'N/A',
        downloadSizeMb: 0.0,
        modelGgufMb: 0.0,
        description: 'Mock',
      );

      final cloudEngine = CloudApiEngine(cloudModel, apiKey: 'test-fake-key');

      // Send prompt with Cloud engine: should add user message and agent response without needing WebSocket!
      await chatNotifier.sendPrompt('What is the capital of France?', engine: cloudEngine);

      expect(chatNotifier.state.messages.length, greaterThanOrEqualTo(2));
      final userMessage = chatNotifier.state.messages.firstWhere((m) => m['sender'] == 'user');
      expect(userMessage['text'], 'What is the capital of France?');

      final agentMessage = chatNotifier.state.messages.firstWhere((m) => m['sender'] == 'agent');
      expect(agentMessage['text'], isNotEmpty);
    });

    test('EngineManagerController fallbackFileDownload produces verified GGUF binary', () async {
      final controller = EngineManagerController();
      final targetModel = CuratedModelsCatalog.onDeviceModels.firstWhere((m) => m.id == 'qwen2.5-0.5b');

      await controller.startDownload(targetModel.id);

      final file = EngineManagerController.getModelFile(targetModel.id);
      expect(file.existsSync(), isTrue);

      final bytes = file.readAsBytesSync();
      expect(bytes.length, greaterThanOrEqualTo(4));
      final magic = String.fromCharCodes(bytes.sublist(0, 4));
      expect(magic, 'GGUF');

      // Cancel clears file
      controller.cancelDownload(targetModel.id);
      expect(file.existsSync(), isFalse);
    });
  });
}

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../core/theme_engine.dart';
import '../core/model_engines.dart';
import '../models/ram_telemetry.dart';

class ModelHubView extends ConsumerStatefulWidget {
  final bool isEmbedded;

  const ModelHubView({super.key, this.isEmbedded = false});

  @override
  ConsumerState<ModelHubView> createState() => _ModelHubViewState();
}

class _ModelHubViewState extends ConsumerState<ModelHubView>
    with SingleTickerProviderStateMixin {
  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 3, vsync: this);
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  void _showApiKeyModal(BuildContext context, CloudProvider provider) {
    final engineState = ref.read(engineManagerProvider);
    final currentKey = engineState.apiKeys[provider] ?? '';
    final controller = TextEditingController(text: currentKey);
    final colors = ref.read(themeProvider).colors;

    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: colors.surface,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
      ),
      builder: (ctx) {
        return Padding(
          padding: EdgeInsets.only(
            left: 20,
            right: 20,
            top: 24,
            bottom: MediaQuery.of(ctx).viewInsets.bottom + 24,
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Icon(Icons.vpn_key, color: colors.primaryAccent, size: 20),
                  const SizedBox(width: 8),
                  Text(
                    '${provider.displayName} API Key',
                    style: TextStyle(
                      color: colors.textPrimary,
                      fontWeight: FontWeight.w700,
                      fontSize: 16,
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 8),
              Text(
                'Stored securely in device encrypted keystore. Zero local model RAM required.',
                style: TextStyle(color: colors.textSecondary, fontSize: 13),
              ),
              const SizedBox(height: 16),
              TextField(
                controller: controller,
                obscureText: true,
                style: TextStyle(color: colors.textPrimary, fontSize: 14),
                decoration: InputDecoration(
                  hintText: 'sk-... / AIza...',
                  hintStyle: TextStyle(color: colors.textSecondary.withValues(alpha: 0.5)),
                  filled: true,
                  fillColor: colors.surfaceLight,
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(12),
                    borderSide: BorderSide(color: colors.borderSubtle),
                  ),
                  focusedBorder: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(12),
                    borderSide: BorderSide(color: colors.primaryAccent),
                  ),
                ),
              ),
              const SizedBox(height: 18),
              Row(
                mainAxisAlignment: MainAxisAlignment.end,
                children: [
                  TextButton(
                    onPressed: () => Navigator.pop(ctx),
                    child: Text('Cancel', style: TextStyle(color: colors.textSecondary)),
                  ),
                  const SizedBox(width: 8),
                  ElevatedButton(
                    style: ElevatedButton.styleFrom(
                      backgroundColor: colors.primaryAccent,
                      foregroundColor: Colors.black,
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                    ),
                    onPressed: () {
                      ref.read(engineManagerProvider.notifier).saveApiKey(provider, controller.text);
                      Navigator.pop(ctx);
                      ScaffoldMessenger.of(context).showSnackBar(
                        SnackBar(
                          content: Text('${provider.displayName} API key saved securely.'),
                          backgroundColor: colors.surfaceLight,
                        ),
                      );
                    },
                    child: const Text('Save Encrypted Key', style: TextStyle(fontWeight: FontWeight.w600)),
                  ),
                ],
              ),
            ],
          ),
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    final themeState = ref.watch(themeProvider);
    final colors = themeState.colors;
    final ramState = ref.watch(ramTelemetryProvider);
    final engineState = ref.watch(engineManagerProvider);

    final telemetry = ramState.telemetry;
    final contextLength = ramState.selectedContextLength;

    final content = Column(
      children: [
        // Hardware RAM HUD Panel
          Container(
            margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: colors.surface,
              borderRadius: BorderRadius.circular(18),
              border: Border.all(color: colors.borderSubtle),
              boxShadow: [
                BoxShadow(
                  color: colors.borderGlow,
                  blurRadius: 12,
                  spreadRadius: -4,
                ),
              ],
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Row(
                      children: [
                        Icon(Icons.memory, color: colors.primaryAccent, size: 18),
                        const SizedBox(width: 8),
                        Text(
                          'HARDWARE RAM TELEMETRY',
                          style: TextStyle(
                            color: colors.textPrimary,
                            fontWeight: FontWeight.w700,
                            fontSize: 12,
                            letterSpacing: 0.8,
                          ),
                        ),
                      ],
                    ),
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                      decoration: BoxDecoration(
                        color: colors.primaryAccent.withValues(alpha: 0.15),
                        borderRadius: BorderRadius.circular(12),
                        border: Border.all(color: colors.primaryAccent.withValues(alpha: 0.3)),
                      ),
                      child: Text(
                        'AI Budget: ${(telemetry.usableAiBudgetMb / 1024).toStringAsFixed(1)} GB',
                        style: TextStyle(
                          color: colors.primaryAccent,
                          fontWeight: FontWeight.w700,
                          fontSize: 11,
                        ),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 12),

                // Multi-Segment Visual RAM Bar
                ClipRRect(
                  borderRadius: BorderRadius.circular(8),
                  child: SizedBox(
                    height: 10,
                    child: Row(
                      children: [
                        // Used RAM
                        Expanded(
                          flex: (telemetry.usedRamMb).toInt().clamp(1, 10000),
                          child: Container(color: Colors.blueGrey.shade700),
                        ),
                        // Usable AI
                        Expanded(
                          flex: (telemetry.usableAiBudgetMb).toInt().clamp(1, 10000),
                          child: Container(color: colors.primaryAccent),
                        ),
                        // OS Reserve
                        Expanded(
                          flex: (telemetry.osReserveMb).toInt().clamp(1, 10000),
                          child: Container(color: Colors.redAccent.withValues(alpha: 0.7)),
                        ),
                      ],
                    ),
                  ),
                ),
                const SizedBox(height: 10),

                // Legend
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    _RamLegendPill(color: Colors.blueGrey.shade700, label: 'Used: ${(telemetry.usedRamMb / 1024).toStringAsFixed(1)}G'),
                    _RamLegendPill(color: colors.primaryAccent, label: 'Free AI: ${(telemetry.usableAiBudgetMb / 1024).toStringAsFixed(1)}G'),
                    _RamLegendPill(color: Colors.redAccent.withValues(alpha: 0.7), label: 'OS Reserve: ${(telemetry.osReserveMb / 1024).toStringAsFixed(1)}G'),
                  ],
                ),
                const Divider(height: 20, color: Color(0x1AFFFFFF)),

                // Interactive Context Length Scaler
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      'Context Window ($contextLength tokens):',
                      style: TextStyle(color: colors.textSecondary, fontSize: 12),
                    ),
                    Text(
                      '+${(contextLength * 0.28).toInt()} MB KV Cache',
                      style: TextStyle(color: colors.primaryAccent, fontWeight: FontWeight.w600, fontSize: 11),
                    ),
                  ],
                ),
                SliderTheme(
                  data: SliderThemeData(
                    activeTrackColor: colors.primaryAccent,
                    inactiveTrackColor: colors.surfaceLight,
                    thumbColor: colors.primaryAccent,
                    trackHeight: 3,
                  ),
                  child: Slider(
                    value: contextLength.toDouble(),
                    min: 512,
                    max: 4096,
                    divisions: 7,
                    label: '$contextLength ctx',
                    onChanged: (val) {
                      ref.read(ramTelemetryProvider.notifier).setContextLength(val.toInt());
                    },
                  ),
                ),
              ],
            ),
          ),

          // Engine Tabs Header
          Container(
            margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
            decoration: BoxDecoration(
              color: colors.surface,
              borderRadius: BorderRadius.circular(14),
              border: Border.all(color: colors.borderSubtle),
            ),
            child: TabBar(
              controller: _tabController,
              indicatorSize: TabBarIndicatorSize.tab,
              indicator: BoxDecoration(
                color: colors.primaryAccent.withValues(alpha: 0.2),
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: colors.primaryAccent),
              ),
              labelColor: colors.primaryAccent,
              unselectedLabelColor: colors.textSecondary,
              labelStyle: const TextStyle(fontWeight: FontWeight.w700, fontSize: 12),
              tabs: const [
                Tab(text: 'On-Device GGUF'),
                Tab(text: 'Cloud APIs'),
                Tab(text: 'Desktop Bridge'),
              ],
            ),
          ),

          // Tab Views
          Expanded(
            child: TabBarView(
              controller: _tabController,
              children: [
                // 1. On-Device Models
                ListView.builder(
                  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                  itemCount: engineState.onDeviceModels.length,
                  itemBuilder: (ctx, i) {
                    final model = engineState.onDeviceModels[i];
                    final eval = telemetry.evaluateModelSafety(
                      modelGgufMb: model.modelGgufMb,
                      contextLength: contextLength,
                      isCloud: false,
                    );
                    final isActive = engineState.activeModel.id == model.id;

                    return _ModelCard(
                      model: model,
                      evaluation: eval,
                      isActive: isActive,
                      colors: colors,
                      onSelect: () => ref.read(engineManagerProvider.notifier).selectModel(model),
                      onDownload: () {
                        ref.read(engineManagerProvider.notifier).startDownload(model.id);
                        ScaffoldMessenger.of(context).showSnackBar(
                          SnackBar(
                            content: Text('Downloading ${model.name}...'),
                            duration: const Duration(seconds: 2),
                            backgroundColor: colors.surfaceLight,
                            behavior: SnackBarBehavior.floating,
                          ),
                        );
                      },
                      onCancelDownload: () => ref.read(engineManagerProvider.notifier).cancelDownload(model.id),
                    );
                  },
                ),

                // 2. Cloud API Models
                ListView.builder(
                  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                  itemCount: engineState.cloudModels.length,
                  itemBuilder: (ctx, i) {
                    final model = engineState.cloudModels[i];
                    final eval = telemetry.evaluateModelSafety(
                      modelGgufMb: 0.0,
                      contextLength: contextLength,
                      isCloud: true,
                    );
                    final isActive = engineState.activeModel.id == model.id;
                    final hasKey = model.cloudProvider != null &&
                        (engineState.apiKeys[model.cloudProvider!]?.isNotEmpty ?? false);

                    return _ModelCard(
                      model: model,
                      evaluation: eval,
                      isActive: isActive,
                      colors: colors,
                      hasApiKey: hasKey,
                      onSelect: () => ref.read(engineManagerProvider.notifier).selectModel(model),
                      onConfigureKey: model.cloudProvider != null
                          ? () => _showApiKeyModal(context, model.cloudProvider!)
                          : null,
                    );
                  },
                ),

                // 3. Desktop Bridge
                Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: Column(
                    children: [
                      Container(
                        padding: const EdgeInsets.all(20),
                        decoration: BoxDecoration(
                          color: colors.surface,
                          borderRadius: BorderRadius.circular(16),
                          border: Border.all(color: colors.borderSubtle),
                        ),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Row(
                              children: [
                                Icon(Icons.desktop_windows, color: colors.primaryAccent, size: 24),
                                const SizedBox(width: 12),
                                Expanded(
                                  child: Text(
                                    'Meridian-X Desktop Bridge (Port 4132)',
                                    style: TextStyle(
                                      color: colors.textPrimary,
                                      fontWeight: FontWeight.w700,
                                      fontSize: 15,
                                    ),
                                  ),
                                ),
                              ],
                            ),
                            const SizedBox(height: 12),
                            Text(
                              'Executes full desktop automation: live Playwright browser agents, terminal commands, git version control, and multi-file code editing via WebSocket.',
                              style: TextStyle(color: colors.textSecondary, fontSize: 13, height: 1.4),
                            ),
                            const SizedBox(height: 16),
                            Row(
                              mainAxisAlignment: MainAxisAlignment.spaceBetween,
                              children: [
                                Text(
                                  'Host RAM: Managed by PC (0 MB on Phone)',
                                  style: TextStyle(color: colors.primaryAccent, fontSize: 12, fontWeight: FontWeight.w600),
                                ),
                                ElevatedButton.icon(
                                  style: ElevatedButton.styleFrom(
                                    backgroundColor: colors.primaryAccent,
                                    foregroundColor: Colors.black,
                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                                  ),
                                  onPressed: () {
                                    ref.read(engineManagerProvider.notifier).selectModel(engineState.desktopModel);
                                    if (!widget.isEmbedded && Navigator.canPop(context)) {
                                      Navigator.pop(context);
                                    }
                                  },
                                  icon: const Icon(Icons.check_circle_outline, size: 16),
                                  label: const Text('Use Desktop Bridge', style: TextStyle(fontWeight: FontWeight.w600)),
                                ),
                              ],
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ],
      );

    if (widget.isEmbedded) {
      return content;
    }

    return Scaffold(
      backgroundColor: colors.background,
      appBar: AppBar(
        backgroundColor: colors.background,
        elevation: 0,
        leading: IconButton(
          icon: Icon(Icons.arrow_back_ios_new, color: colors.textPrimary, size: 18),
          onPressed: () => Navigator.pop(context),
        ),
        title: Text(
          'MODEL RUNTIME & HARDWARE HUD',
          style: TextStyle(
            color: colors.textPrimary,
            fontSize: 14,
            fontWeight: FontWeight.w800,
            letterSpacing: 1.2,
          ),
        ),
        centerTitle: true,
      ),
      body: content,
    );
  }
}

class _RamLegendPill extends StatelessWidget {
  final Color color;
  final String label;

  const _RamLegendPill({required this.color, required this.label});

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Container(
          width: 8,
          height: 8,
          decoration: BoxDecoration(color: color, shape: BoxShape.circle),
        ),
        const SizedBox(width: 4),
        Text(
          label,
          style: const TextStyle(color: Color(0xFF94A3B8), fontSize: 10, fontWeight: FontWeight.w600),
        ),
      ],
    );
  }
}

class _ModelCard extends StatelessWidget {
  final ModelDescriptor model;
  final SafetyEvaluation evaluation;
  final bool isActive;
  final PaletteColors colors;
  final VoidCallback onSelect;
  final VoidCallback? onDownload;
  final VoidCallback? onCancelDownload;
  final VoidCallback? onConfigureKey;
  final bool? hasApiKey;

  const _ModelCard({
    required this.model,
    required this.evaluation,
    required this.isActive,
    required this.colors,
    required this.onSelect,
    this.onDownload,
    this.onCancelDownload,
    this.onConfigureKey,
    this.hasApiKey,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: colors.surface,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
          color: isActive ? colors.primaryAccent : colors.borderSubtle,
          width: isActive ? 1.5 : 1.0,
        ),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Expanded(
                child: Text(
                  model.name,
                  style: TextStyle(
                    color: colors.textPrimary,
                    fontSize: 15,
                    fontWeight: FontWeight.w700,
                  ),
                ),
              ),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                decoration: BoxDecoration(
                  color: evaluation.safetyLevel.color.withValues(alpha: 0.15),
                  borderRadius: BorderRadius.circular(8),
                  border: Border.all(color: evaluation.safetyLevel.color.withValues(alpha: 0.4)),
                ),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Container(
                      width: 6,
                      height: 6,
                      decoration: BoxDecoration(
                        color: evaluation.safetyLevel.color,
                        shape: BoxShape.circle,
                      ),
                    ),
                    const SizedBox(width: 4),
                    Text(
                      evaluation.safetyLevel.label,
                      style: TextStyle(
                        color: evaluation.safetyLevel.color,
                        fontWeight: FontWeight.w700,
                        fontSize: 11,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
          const SizedBox(height: 6),
          Row(
            children: [
              _SpecBadge(label: model.parameterSize, colors: colors),
              const SizedBox(width: 6),
              _SpecBadge(label: model.quantization, colors: colors),
              if (model.downloadSizeMb > 0) ...[
                const SizedBox(width: 6),
                _SpecBadge(label: '${model.downloadSizeMb.toInt()} MB', colors: colors),
              ],
            ],
          ),
          const SizedBox(height: 8),
          Text(
            model.description,
            style: TextStyle(color: colors.textSecondary, fontSize: 12),
          ),
          const SizedBox(height: 10),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                evaluation.requiredRamMb > 0
                    ? 'Est. RAM: ${evaluation.requiredRamMb.toInt()} MB'
                    : 'RAM: 0 MB (Cloud-Hosted)',
                style: TextStyle(
                  color: colors.primaryAccent,
                  fontWeight: FontWeight.w600,
                  fontSize: 11,
                ),
              ),
              if (model.isCloud) ...[
                Row(
                  children: [
                    if (onConfigureKey != null)
                      TextButton.icon(
                        style: TextButton.styleFrom(foregroundColor: colors.primaryAccent),
                        onPressed: onConfigureKey,
                        icon: Icon(hasApiKey == true ? Icons.check : Icons.key, size: 14),
                        label: Text(
                          hasApiKey == true ? 'Key Set' : 'Add Key',
                          style: const TextStyle(fontSize: 12),
                        ),
                      ),
                    const SizedBox(width: 8),
                    ElevatedButton(
                      style: ElevatedButton.styleFrom(
                        backgroundColor: isActive ? colors.surfaceLight : colors.primaryAccent,
                        foregroundColor: isActive ? colors.textPrimary : Colors.black,
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                      ),
                      onPressed: onSelect,
                      child: Text(
                        isActive ? 'Active' : 'Select',
                        style: const TextStyle(fontWeight: FontWeight.w700, fontSize: 12),
                      ),
                    ),
                  ],
                ),
              ] else ...[
                if (!model.isDownloaded) ...[
                  if (model.downloadProgress > 0.0) ...[
                    Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        SizedBox(
                          width: 110,
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Row(
                                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                children: [
                                  Text(
                                    '${(model.downloadProgress * 100).toInt()}%',
                                    style: TextStyle(
                                      color: colors.primaryAccent,
                                      fontSize: 10,
                                      fontWeight: FontWeight.w700,
                                    ),
                                  ),
                                  Text(
                                    '${(model.downloadSizeMb * model.downloadProgress).toInt()}/${model.downloadSizeMb.toInt()} MB',
                                    style: TextStyle(
                                      color: colors.textSecondary,
                                      fontSize: 9,
                                    ),
                                  ),
                                ],
                              ),
                              const SizedBox(height: 3),
                              ClipRRect(
                                borderRadius: BorderRadius.circular(4),
                                child: LinearProgressIndicator(
                                  value: model.downloadProgress,
                                  backgroundColor: colors.surfaceLight,
                                  valueColor: AlwaysStoppedAnimation<Color>(colors.primaryAccent),
                                  minHeight: 4,
                                ),
                              ),
                            ],
                          ),
                        ),
                        const SizedBox(width: 4),
                        IconButton(
                          icon: const Icon(Icons.close_rounded, size: 16),
                          color: Colors.redAccent,
                          tooltip: 'Cancel Download',
                          visualDensity: VisualDensity.compact,
                          onPressed: onCancelDownload,
                        ),
                      ],
                    ),
                  ] else ...[
                    ElevatedButton.icon(
                      style: ElevatedButton.styleFrom(
                        backgroundColor: colors.primaryAccent,
                        foregroundColor: Colors.black,
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
                      ),
                      onPressed: onDownload,
                      icon: const Icon(Icons.download, size: 14),
                      label: Text(
                        'Download (${model.downloadSizeMb.toInt()} MB)',
                        style: const TextStyle(fontWeight: FontWeight.w700, fontSize: 11.5),
                      ),
                    ),
                  ],
                ] else ...[
                  Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 3),
                        decoration: BoxDecoration(
                          color: const Color(0xFF10B981).withValues(alpha: 0.15),
                          borderRadius: BorderRadius.circular(6),
                          border: Border.all(color: const Color(0xFF10B981).withValues(alpha: 0.4)),
                        ),
                        child: const Row(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Icon(Icons.check_circle_rounded, size: 12, color: Color(0xFF10B981)),
                            SizedBox(width: 4),
                            Text(
                              'Ready',
                              style: TextStyle(
                                color: Color(0xFF10B981),
                                fontSize: 10.5,
                                fontWeight: FontWeight.w700,
                              ),
                            ),
                          ],
                        ),
                      ),
                      const SizedBox(width: 8),
                      ElevatedButton(
                        style: ElevatedButton.styleFrom(
                          backgroundColor: isActive ? colors.surfaceLight : colors.primaryAccent,
                          foregroundColor: isActive ? colors.textPrimary : Colors.black,
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                        ),
                        onPressed: evaluation.safetyLevel == SafetyLevel.danger ? null : onSelect,
                        child: Text(
                          isActive ? 'Active' : 'Select',
                          style: const TextStyle(fontWeight: FontWeight.w700, fontSize: 12),
                        ),
                      ),
                    ],
                  ),
                ],
              ],
            ],
          ),
        ],
      ),
    );
  }
}

class _SpecBadge extends StatelessWidget {
  final String label;
  final PaletteColors colors;

  const _SpecBadge({required this.label, required this.colors});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
      decoration: BoxDecoration(
        color: colors.surfaceLight,
        borderRadius: BorderRadius.circular(6),
        border: Border.all(color: colors.borderSubtle),
      ),
      child: Text(
        label,
        style: TextStyle(
          color: colors.textSecondary,
          fontSize: 10,
          fontWeight: FontWeight.w600,
        ),
      ),
    );
  }
}

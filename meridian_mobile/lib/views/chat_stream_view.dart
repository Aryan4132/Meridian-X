import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../core/theme.dart';
import '../core/theme_engine.dart';
import '../core/model_engines.dart';
import '../models/thought_step.dart';
import '../providers/agent_chat_provider.dart';

class ChatStreamView extends ConsumerStatefulWidget {
  final VoidCallback? onToggleVision;
  final bool isVisionActive;

  const ChatStreamView({
    super.key,
    this.onToggleVision,
    this.isVisionActive = false,
  });

  @override
  ConsumerState<ChatStreamView> createState() => _ChatStreamViewState();
}

class _ChatStreamViewState extends ConsumerState<ChatStreamView> {
  final TextEditingController _promptController = TextEditingController();
  final ScrollController _scrollController = ScrollController();
  bool _thoughtsExpanded = false;

  @override
  void dispose() {
    _promptController.dispose();
    _scrollController.dispose();
    super.dispose();
  }

  void _scrollToBottom() {
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (_scrollController.hasClients) {
        _scrollController.animateTo(
          _scrollController.position.maxScrollExtent,
          duration: const Duration(milliseconds: 300),
          curve: Curves.easeOutQuart,
        );
      }
    });
  }

  void _submitPrompt([String? presetText]) {
    final text = presetText ?? _promptController.text;
    if (text.trim().isNotEmpty) {
      final engine = ref.read(engineManagerProvider).buildEngine();
      ref.read(agentChatProvider.notifier).sendPrompt(text.trim(), engine: engine);
      if (presetText == null) {
        _promptController.clear();
      }
      _scrollToBottom();
    }
  }

  @override
  Widget build(BuildContext context) {
    final themeState = ref.watch(themeProvider);
    final colors = themeState.colors;
    final agentState = ref.watch(agentChatProvider);
    final messages = agentState.messages;
    final thoughtSteps = agentState.thoughtSteps;

    // Trigger auto-scroll on new message
    ref.listen<AgentState>(agentChatProvider, (prev, next) {
      if (prev?.messages.length != next.messages.length ||
          prev?.thoughtSteps.length != next.thoughtSteps.length) {
        _scrollToBottom();
      }
    });

    return Column(
      children: [
        // Optional Inline Thought Process Accordion
        if (thoughtSteps.isNotEmpty)
          _InlineThoughtAccordion(
            steps: thoughtSteps,
            isExpanded: _thoughtsExpanded,
            colors: colors,
            onToggle: () => setState(() => _thoughtsExpanded = !_thoughtsExpanded),
          ),

        // Chat Message List
        Expanded(
          child: messages.isEmpty
              ? _EmptyChatState(
                  colors: colors,
                  onSelectPrompt: (p) => _submitPrompt(p),
                )
              : ListView.builder(
                  controller: _scrollController,
                  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                  itemCount: messages.length,
                  itemBuilder: (context, index) {
                    final msg = messages[index];
                    final isUser = msg['sender'] == 'user';
                    final isSystem = msg['sender'] == 'system';
                    final text = (msg['text'] ?? msg['content'] ?? '').toString();
                    final time = msg['timestamp']?.toString();

                    return _MessageCard(
                      text: text,
                      isUser: isUser,
                      isSystem: isSystem,
                      timestamp: time,
                      colors: colors,
                    );
                  },
                ),
        ),

        // Sleek Integrated Prompt Input Dock
        Container(
          padding: const EdgeInsets.fromLTRB(16, 8, 16, 12),
          decoration: BoxDecoration(
            color: colors.background,
            border: Border(
              top: BorderSide(color: colors.borderSubtle.withValues(alpha: 0.5)),
            ),
          ),
          child: SafeArea(
            top: false,
            child: Row(
              children: [
                if (widget.onToggleVision != null)
                  IconButton(
                    onPressed: widget.onToggleVision,
                    icon: Icon(
                      widget.isVisionActive ? Icons.camera_alt : Icons.camera_alt_outlined,
                      color: widget.isVisionActive ? colors.primaryAccent : colors.textSecondary,
                      size: 20,
                    ),
                    tooltip: 'Camera Vision Scanner',
                  ),
                Expanded(
                  child: Container(
                    decoration: BoxDecoration(
                      color: colors.surface,
                      borderRadius: BorderRadius.circular(24),
                      border: Border.all(color: colors.borderSubtle),
                    ),
                    child: Row(
                      children: [
                        const SizedBox(width: 14),
                        Expanded(
                          child: TextField(
                            controller: _promptController,
                            onSubmitted: (_) => _submitPrompt(),
                            style: TextStyle(color: colors.textPrimary, fontSize: 14),
                            decoration: InputDecoration(
                              hintText: 'Ask Meridian agent or invoke tool...',
                              hintStyle: TextStyle(
                                color: colors.textSecondary.withValues(alpha: 0.7),
                                fontSize: 13,
                              ),
                              border: InputBorder.none,
                              isDense: true,
                              contentPadding: const EdgeInsets.symmetric(vertical: 12),
                            ),
                          ),
                        ),
                        if (_promptController.text.isNotEmpty)
                          IconButton(
                            icon: Icon(Icons.close, size: 16, color: colors.textSecondary),
                            onPressed: () => setState(() => _promptController.clear()),
                          ),
                        const SizedBox(width: 4),
                      ],
                    ),
                  ),
                ),
                const SizedBox(width: 8),
                InkWell(
                  onTap: _submitPrompt,
                  borderRadius: BorderRadius.circular(22),
                  child: Container(
                    width: 44,
                    height: 44,
                    decoration: BoxDecoration(
                      color: colors.primaryAccent,
                      shape: BoxShape.circle,
                      boxShadow: [
                        BoxShadow(
                          color: colors.primaryAccent.withValues(alpha: 0.35),
                          blurRadius: 10,
                          offset: const Offset(0, 2),
                        ),
                      ],
                    ),
                    child: const Icon(
                      Icons.arrow_upward_rounded,
                      color: Colors.black,
                      size: 22,
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ],
    );
  }
}

class _EmptyChatState extends StatelessWidget {
  final PaletteColors colors;
  final ValueChanged<String> onSelectPrompt;

  const _EmptyChatState({
    required this.colors,
    required this.onSelectPrompt,
  });

  @override
  Widget build(BuildContext context) {
    final suggestions = [
      'System status & telemetry',
      'Search latest AI research news',
      'What local models are loaded?',
      'Check active Git repository status',
    ];

    return Center(
      child: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              width: 60,
              height: 60,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: colors.primaryAccent.withValues(alpha: 0.12),
                border: Border.all(color: colors.primaryAccent.withValues(alpha: 0.3)),
              ),
              child: Icon(Icons.bolt_rounded, size: 32, color: colors.primaryAccent),
            ),
            const SizedBox(height: 16),
            Text(
              'Meridian-X Autonomous Core',
              style: TextStyle(
                color: colors.textPrimary,
                fontSize: 16,
                fontWeight: FontWeight.w700,
                letterSpacing: 0.5,
              ),
            ),
            const SizedBox(height: 6),
            Text(
              'Connected to Tri-Engine Runtime.\nAsk questions, automate tasks, or switch to Voice Mode.',
              textAlign: TextAlign.center,
              style: TextStyle(
                color: colors.textSecondary,
                fontSize: 13,
                height: 1.4,
              ),
            ),
            const SizedBox(height: 24),
            Wrap(
              spacing: 8,
              runSpacing: 8,
              alignment: WrapAlignment.center,
              children: suggestions.map((p) {
                return ActionChip(
                  label: Text(
                    p,
                    style: TextStyle(color: colors.textPrimary, fontSize: 12),
                  ),
                  backgroundColor: colors.surface,
                  side: BorderSide(color: colors.borderSubtle),
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
                  onPressed: () => onSelectPrompt(p),
                );
              }).toList(),
            ),
          ],
        ),
      ),
    );
  }
}

class _MessageCard extends StatelessWidget {
  final String text;
  final bool isUser;
  final bool isSystem;
  final String? timestamp;
  final PaletteColors colors;

  const _MessageCard({
    required this.text,
    required this.isUser,
    required this.isSystem,
    this.timestamp,
    required this.colors,
  });

  void _copyToClipboard(BuildContext context) {
    Clipboard.setData(ClipboardData(text: text));
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: const Text('Copied to clipboard'),
        duration: const Duration(seconds: 1),
        backgroundColor: colors.surfaceLight,
        behavior: SnackBarBehavior.floating,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    if (isSystem) {
      return Container(
        margin: const EdgeInsets.symmetric(vertical: 6),
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
        decoration: BoxDecoration(
          color: colors.surface.withValues(alpha: 0.6),
          borderRadius: BorderRadius.circular(10),
          border: Border.all(color: colors.borderSubtle.withValues(alpha: 0.4)),
        ),
        child: Row(
          children: [
            Icon(Icons.info_outline, size: 14, color: colors.secondaryAccent),
            const SizedBox(width: 8),
            Expanded(
              child: Text(
                text,
                style: TextStyle(color: colors.textSecondary, fontSize: 11),
              ),
            ),
          ],
        ),
      );
    }

    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 6),
      child: Row(
        mainAxisAlignment: isUser ? MainAxisAlignment.end : MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          if (!isUser) ...[
            Container(
              width: 28,
              height: 28,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: colors.primaryAccent.withValues(alpha: 0.15),
                border: Border.all(color: colors.primaryAccent.withValues(alpha: 0.3)),
              ),
              child: Icon(Icons.auto_awesome, size: 14, color: colors.primaryAccent),
            ),
            const SizedBox(width: 8),
          ],
          Flexible(
            child: Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: isUser
                    ? colors.primaryAccent.withValues(alpha: 0.15)
                    : colors.surface,
                borderRadius: BorderRadius.only(
                  topLeft: const Radius.circular(16),
                  topRight: const Radius.circular(16),
                  bottomLeft: Radius.circular(isUser ? 16 : 4),
                  bottomRight: Radius.circular(isUser ? 4 : 16),
                ),
                border: Border.all(
                  color: isUser
                      ? colors.primaryAccent.withValues(alpha: 0.3)
                      : colors.borderSubtle,
                ),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Text(
                        isUser ? 'YOU' : 'MERIDIAN-X',
                        style: TextStyle(
                          color: isUser ? colors.primaryAccent : colors.secondaryAccent,
                          fontSize: 10,
                          fontWeight: FontWeight.w800,
                          letterSpacing: 0.8,
                        ),
                      ),
                      const SizedBox(width: 8),
                      InkWell(
                        onTap: () => _copyToClipboard(context),
                        child: Icon(
                          Icons.copy_rounded,
                          size: 12,
                          color: colors.textSecondary.withValues(alpha: 0.6),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 6),
                  SelectableText(
                    text,
                    style: TextStyle(
                      color: colors.textPrimary,
                      fontSize: 13.5,
                      height: 1.45,
                    ),
                  ),
                ],
              ),
            ),
          ),
          if (isUser) ...[
            const SizedBox(width: 8),
            Container(
              width: 28,
              height: 28,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: colors.surfaceLight,
                border: Border.all(color: colors.borderSubtle),
              ),
              child: Icon(Icons.person_outline, size: 16, color: colors.textPrimary),
            ),
          ],
        ],
      ),
    );
  }
}

class _InlineThoughtAccordion extends StatelessWidget {
  final List<ThoughtStep> steps;
  final bool isExpanded;
  final PaletteColors colors;
  final VoidCallback onToggle;

  const _InlineThoughtAccordion({
    required this.steps,
    required this.isExpanded,
    required this.colors,
    required this.onToggle,
  });

  @override
  Widget build(BuildContext context) {
    final activeStep = steps.firstWhere(
      (s) => s.status == ThoughtStatus.running,
      orElse: () => steps.first,
    );

    return Container(
      margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
      decoration: BoxDecoration(
        color: colors.surface,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: colors.borderSubtle),
      ),
      child: Column(
        children: [
          InkWell(
            onTap: onToggle,
            borderRadius: BorderRadius.circular(12),
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
              child: Row(
                children: [
                  Icon(
                    activeStep.status == ThoughtStatus.running
                        ? Icons.sync
                        : Icons.psychology_outlined,
                    size: 16,
                    color: colors.secondaryAccent,
                  ),
                  const SizedBox(width: 8),
                  Expanded(
                    child: Text(
                      'Thinking: ${activeStep.title} (${steps.length} steps)',
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: TextStyle(
                        color: colors.textPrimary,
                        fontSize: 11.5,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ),
                  Icon(
                    isExpanded ? Icons.expand_less : Icons.expand_more,
                    size: 18,
                    color: colors.textSecondary,
                  ),
                ],
              ),
            ),
          ),
          if (isExpanded)
            Container(
              constraints: const BoxConstraints(maxHeight: 140),
              padding: const EdgeInsets.fromLTRB(12, 0, 12, 8),
              child: ListView.builder(
                shrinkWrap: true,
                itemCount: steps.length,
                itemBuilder: (context, i) {
                  final s = steps[i];
                  return Padding(
                    padding: const EdgeInsets.symmetric(vertical: 2),
                    child: Row(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          '${s.stepNumber}.',
                          style: TextStyle(
                            color: colors.secondaryAccent,
                            fontSize: 10,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                        const SizedBox(width: 6),
                        Expanded(
                          child: Text(
                            '${s.title}: ${s.detail}',
                            style: TextStyle(
                              color: colors.textSecondary,
                              fontSize: 11,
                            ),
                          ),
                        ),
                      ],
                    ),
                  );
                },
              ),
            ),
        ],
      ),
    );
  }
}

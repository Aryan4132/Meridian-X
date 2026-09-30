import 'package:flutter/material.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../core/theme.dart';
import '../models/thought_step.dart';
import '../providers/agent_chat_provider.dart';

class ThoughtCarouselWidget extends ConsumerWidget {
  const ThoughtCarouselWidget({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final agentState = ref.watch(agentChatProvider);
    final steps = agentState.thoughtSteps;

    if (steps.isEmpty) {
      return const SizedBox.shrink();
    }

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 8.0),
          child: Row(
            children: [
              const Icon(Icons.psychology, size: 16, color: MeridianTheme.cyanAccent),
              const SizedBox(width: 8),
              const Text(
                'AGENT THOUGHT STREAM',
                style: TextStyle(
                  color: MeridianTheme.cyanAccent,
                  fontSize: 12,
                  fontWeight: FontWeight.bold,
                  letterSpacing: 1.2,
                ),
              ),
              const Spacer(),
              Text(
                '${steps.length} Steps',
                style: const TextStyle(
                  color: MeridianTheme.textSecondary,
                  fontSize: 12,
                ),
              ),
            ],
          ),
        ),
        SizedBox(
          height: 110,
          child: ListView.builder(
            scrollDirection: Axis.horizontal,
            padding: const EdgeInsets.symmetric(horizontal: 12),
            itemCount: steps.length,
            itemBuilder: (context, index) {
              final step = steps[index];
              return _ThoughtCard(step: step, index: index);
            },
          ),
        ),
      ],
    );
  }
}

class _ThoughtCard extends StatelessWidget {
  final ThoughtStep step;
  final int index;

  const _ThoughtCard({required this.step, required this.index});

  Color _getStatusColor(ThoughtStatus status) {
    switch (status) {
      case ThoughtStatus.running:
        return MeridianTheme.cyanAccent;
      case ThoughtStatus.completed:
        return MeridianTheme.emeraldGreen;
      case ThoughtStatus.failed:
        return MeridianTheme.roseError;
      case ThoughtStatus.paused:
        return MeridianTheme.amberWarning;
    }
  }

  IconData _getStatusIcon(ThoughtStatus status) {
    switch (status) {
      case ThoughtStatus.running:
        return Icons.sync;
      case ThoughtStatus.completed:
        return Icons.check_circle_outline;
      case ThoughtStatus.failed:
        return Icons.warning_amber_rounded;
      case ThoughtStatus.paused:
        return Icons.pause_circle_outline;
    }
  }

  @override
  Widget build(BuildContext context) {
    final statusColor = _getStatusColor(step.status);

    return Container(
      width: 260,
      margin: const EdgeInsets.symmetric(horizontal: 6, vertical: 4),
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: MeridianTheme.surface,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(
          color: step.status == ThoughtStatus.running
              ? MeridianTheme.cyanAccent.withValues(alpha: 0.6)
              : MeridianTheme.surfaceLight,
        ),
        boxShadow: [
          if (step.status == ThoughtStatus.running)
            BoxShadow(
              color: MeridianTheme.cyanAccent.withValues(alpha: 0.15),
              blurRadius: 12,
              spreadRadius: 2,
            ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Row(
            children: [
              Container(
                padding: const EdgeInsets.all(4),
                decoration: BoxDecoration(
                  color: statusColor.withValues(alpha: 0.15),
                  shape: BoxShape.circle,
                ),
                child: Icon(_getStatusIcon(step.status), size: 14, color: statusColor),
              ),
              const SizedBox(width: 8),
              Expanded(
                child: Text(
                  'Step ${step.stepNumber}: ${step.title}',
                  style: const TextStyle(
                    color: MeridianTheme.textPrimary,
                    fontSize: 13,
                    fontWeight: FontWeight.w600,
                  ),
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                ),
              ),
            ],
          ),
          Text(
            step.detail,
            style: const TextStyle(
              color: MeridianTheme.textSecondary,
              fontSize: 11,
              height: 1.3,
            ),
            maxLines: 2,
            overflow: TextOverflow.ellipsis,
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                'Conf: ${(step.confidenceScore * 100).toInt()}%',
                style: TextStyle(
                  color: statusColor,
                  fontSize: 10,
                  fontWeight: FontWeight.bold,
                ),
              ),
              Text(
                '${step.timestamp.hour.toString().padLeft(2, '0')}:${step.timestamp.minute.toString().padLeft(2, '0')}:${step.timestamp.second.toString().padLeft(2, '0')}',
                style: TextStyle(
                  color: MeridianTheme.textSecondary.withValues(alpha: 0.7),
                  fontSize: 10,
                ),
              ),
            ],
          ),
        ],
      ),
    ).animate().fadeIn(duration: 300.ms).slideX(begin: 0.1, end: 0);
  }
}

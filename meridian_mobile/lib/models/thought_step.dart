enum ThoughtStatus { running, completed, failed, paused }

class ThoughtStep {
  final String id;
  final int stepNumber;
  final String title;
  final String detail;
  final ThoughtStatus status;
  final DateTime timestamp;
  final double confidenceScore;

  ThoughtStep({
    required this.id,
    required this.stepNumber,
    required this.title,
    required this.detail,
    required this.status,
    required this.timestamp,
    this.confidenceScore = 1.0,
  });

  factory ThoughtStep.fromJson(Map<String, dynamic> json) {
    ThoughtStatus parseStatus(String? statusStr) {
      switch (statusStr?.toLowerCase()) {
        case 'running':
          return ThoughtStatus.running;
        case 'completed':
        case 'done':
          return ThoughtStatus.completed;
        case 'failed':
        case 'error':
          return ThoughtStatus.failed;
        default:
          return ThoughtStatus.completed;
      }
    }

    final stepRaw = json['step_number'] ?? json['stepNumber'] ?? 1;
    final confRaw = json['confidence_score'] ?? json['confidence'] ?? 1.0;
    final tsRaw = json['timestamp'];
    return ThoughtStep(
      id: json['id']?.toString() ?? DateTime.now().millisecondsSinceEpoch.toString(),
      stepNumber: stepRaw is num ? stepRaw.toInt() : 1,
      title: json['title']?.toString() ?? 'Processing Step',
      detail: json['detail']?.toString() ?? json['content']?.toString() ?? '',
      status: parseStatus(json['status']?.toString()),
      timestamp: tsRaw != null ? DateTime.tryParse(tsRaw.toString()) ?? DateTime.now() : DateTime.now(),
      confidenceScore: confRaw is num ? confRaw.toDouble() : 1.0,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'step_number': stepNumber,
      'title': title,
      'detail': detail,
      'status': status.name,
      'timestamp': timestamp.toIso8601String(),
      'confidence_score': confidenceScore,
    };
  }
}

class TelemetryData {
  final double cpuPercent;
  final double memoryMb;
  final int pingMs;
  final bool antiHallucinationActive;
  final String activeModel;
  final String serverVersion;

  const TelemetryData({
    this.cpuPercent = 0.0,
    this.memoryMb = 0.0,
    this.pingMs = 0,
    this.antiHallucinationActive = true,
    this.activeModel = 'Meridian-X Core v1.0',
    this.serverVersion = '1.0.0',
  });

  factory TelemetryData.fromJson(Map<String, dynamic> json) {
    double asDouble(dynamic v, double fallback) {
      if (v is num) return v.toDouble();
      if (v is String) return double.tryParse(v) ?? fallback;
      return fallback;
    }

    int asInt(dynamic v, int fallback) {
      if (v is num) return v.toInt();
      if (v is String) return int.tryParse(v) ?? fallback;
      return fallback;
    }

    final ahRaw = json['anti_hallucination'];
    return TelemetryData(
      cpuPercent: asDouble(json['cpu_percent'] ?? json['cpuPercent'], 12.5),
      memoryMb: asDouble(json['memory_mb'] ?? json['memoryMb'], 256.0),
      pingMs: asInt(json['ping_ms'] ?? json['pingMs'], 24),
      antiHallucinationActive: ahRaw is bool ? ahRaw : true,
      activeModel: json['model']?.toString() ?? 'Meridian-X Core v1.0',
      serverVersion: json['version']?.toString() ?? '1.0.0',
    );
  }
}

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:meridian_mobile/main.dart';
import 'package:meridian_mobile/views/bottom_nav_dock.dart';
import 'package:meridian_mobile/views/chat_stream_view.dart';
import 'package:meridian_mobile/views/voice_mode_view.dart';
import 'package:meridian_mobile/views/settings_view.dart';

void main() {
  testWidgets('Executive Bottom Nav Dock renders 4 tabs and switches views', (WidgetTester tester) async {
    await tester.pumpWidget(
      const ProviderScope(
        child: MeridianMobileApp(),
      ),
    );
    await tester.pump(const Duration(milliseconds: 100));

    // Title and initial Chat tab present
    expect(find.text('MERIDIAN-X'), findsOneWidget);
    expect(find.byType(BottomNavDock), findsOneWidget);
    expect(find.byType(ChatStreamView), findsOneWidget);

    // Initial empty chat state suggestions
    expect(find.text('System status & telemetry'), findsOneWidget);

    // Tap Voice Tab (Index 1)
    await tester.tap(find.text('Voice'));
    await tester.pump(const Duration(milliseconds: 100));
    expect(find.byType(VoiceModeView), findsOneWidget);

    // Tap Settings Tab (Index 3)
    await tester.tap(find.text('Settings'));
    await tester.pump(const Duration(milliseconds: 100));
    expect(find.byType(SettingsView), findsOneWidget);
    expect(find.text('VISUAL DESIGN & THEME ENGINE'), findsOneWidget);

    // Tap Chat Tab (Index 0) to return
    await tester.tap(find.text('Chat'));
    await tester.pump(const Duration(milliseconds: 100));
    expect(find.byType(ChatStreamView), findsOneWidget);
  });
}

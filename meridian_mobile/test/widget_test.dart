import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:meridian_mobile/main.dart';

void main() {
  testWidgets('Meridian mobile app renders title smoke test', (WidgetTester tester) async {
    await tester.pumpWidget(
      const ProviderScope(
        child: MeridianMobileApp(),
      ),
    );
    await tester.pump(const Duration(milliseconds: 50));

    expect(find.text('MERIDIAN-X'), findsOneWidget);
  });
}

import 'package:flutter_test/flutter_test.dart';

import 'package:gym_app/detector.dart';
import 'package:gym_app/exercise_db.dart';
import 'package:gym_app/main.dart';
import 'package:gym_app/screens/result_screen.dart';

void main() {
  testWidgets(
      'home screen renders machines and tapping a chip opens its results',
      (WidgetTester tester) async {
    final db = ExerciseDb();
    await db.load();
    expect(db.all, isNotEmpty);

    await tester.pumpWidget(GymApp(db: db, detector: DemoDetector(['leg_press'])));

    expect(find.text('GymLens'), findsOneWidget);
    expect(find.text('What is this machine?'), findsOneWidget);

    await tester.tap(find.text('Leg Press Machine'));
    await tester.pumpAndSettle();

    expect(find.byType(ResultScreen), findsOneWidget);
    expect(find.text('Quads'), findsWidgets);
    expect(find.textContaining('Leg Press'), findsWidgets);
  });

  testWidgets('demo-mode banner shows when detector is in demo mode',
      (WidgetTester tester) async {
    final db = ExerciseDb();
    await db.load();

    await tester.pumpWidget(GymApp(db: db, detector: DemoDetector(['leg_press'])));

    expect(find.text('Demo mode'), findsOneWidget);
  });
}

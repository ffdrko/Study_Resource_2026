import 'package:flutter/material.dart';

import 'detector.dart';
import 'exercise_db.dart';
import 'screens/home_screen.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

  final db = ExerciseDb();
  await db.load();

  final detector = await createDetector(); // real YOLO if present, else demo

  runApp(GymApp(db: db, detector: detector));
}

class GymApp extends StatelessWidget {
  const GymApp({super.key, required this.db, required this.detector});

  final ExerciseDb db;
  final Detector detector;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'GymLens',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        brightness: Brightness.dark,
        colorSchemeSeed: Colors.deepOrange,
      ),
      home: HomeScreen(db: db, detector: detector),
    );
  }
}

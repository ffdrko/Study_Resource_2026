import 'package:flutter/material.dart';
import 'package:image/image.dart' as img;
import 'package:image_picker/image_picker.dart';

import '../exercise_db.dart';
import 'result_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key, required this.db, required this.detector});

  final ExerciseDb db;
  final dynamic detector; // Detector (kept dynamic to avoid extra import noise)

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  bool _busy = false;

  Future<void> _pickAndDetect(ImageSource source) async {
    if (_busy) return;
    setState(() => _busy = true);
    try {
      final picker = ImagePicker();
      final picked = await picker.pickImage(source: source, imageQuality: 85);
      if (picked == null || !mounted) return;

      final bytes = await picked.readAsBytes();
      final photo = img.decodeImage(bytes);
      if (photo == null || !mounted) {
        _snack('Could not read that image');
        return;
      }

      // ---- THE PIPELINE: photo -> label -> JSON lookup -> result screen ----
      final label = widget.detector.detect(photo); // e.g. "leg_press"
      final machine = widget.db.find(label);

      if (!mounted) return;
      if (machine == null) {
        _snack('Machine not recognized. Try a clearer / closer shot.');
        return;
      }
      Navigator.of(context).push(MaterialPageRoute(
        builder: (_) => ResultScreen(machine: machine),
      ));
    } catch (e) {
      _snack('Something went wrong: $e');
    } finally {
      if (mounted) setState(() => _busy = false);
    }
  }

  void _snack(String msg) {
    ScaffoldMessenger.of(context)
        .showSnackBar(SnackBar(content: Text(msg)));
  }

  @override
  Widget build(BuildContext context) {
    final machines = widget.db.all;
    return Scaffold(
      appBar: AppBar(
        title: const Text('GymLens'),
        centerTitle: true,
      ),
      body: Stack(
        children: [
          ListView(
            padding: const EdgeInsets.all(16),
            children: [
              if ((widget.detector as dynamic).isDemoMode == true)
                Card(
                  color: Colors.amber.shade900.withValues(alpha: .35),
                  child: const ListTile(
                    leading: Icon(Icons.science_outlined),
                    title: Text('Demo mode'),
                    subtitle: Text(
                        'No YOLO model found — detections are simulated. '
                        'Drop yolo_model.tflite into assets/model/ to go live.'),
                  ),
                ),
              const SizedBox(height: 8),
              Center(
                child: Column(
                  children: [
                    const Icon(Icons.fitness_center,
                        size: 72, color: Colors.deepOrangeAccent),
                    const SizedBox(height: 12),
                    Text('What is this machine?',
                        style: Theme.of(context).textTheme.headlineSmall),
                    const SizedBox(height: 4),
                    Text('Take a photo and get the exercises for it.',
                        style: Theme.of(context).textTheme.bodyMedium),
                  ],
                ),
              ),
              const SizedBox(height: 24),
              FilledButton.icon(
                onPressed: _busy ? null : () => _pickAndDetect(ImageSource.camera),
                icon: const Icon(Icons.camera_alt),
                label: const Padding(
                  padding: EdgeInsets.symmetric(vertical: 14),
                  child: Text('Take a Photo'),
                ),
              ),
              const SizedBox(height: 12),
              OutlinedButton.icon(
                onPressed: _busy ? null : () => _pickAndDetect(ImageSource.gallery),
                icon: const Icon(Icons.photo_library),
                label: const Padding(
                  padding: EdgeInsets.symmetric(vertical: 14),
                  child: Text('Pick from Gallery'),
                ),
              ),
              const Divider(height: 40),
              Text('Machines covered (${machines.length})',
                  style: Theme.of(context).textTheme.titleMedium),
              const SizedBox(height: 8),
              Wrap(
                spacing: 8,
                runSpacing: 8,
                children: [
                  for (final m in machines)
                    ActionChip(
                      label: Text(m.name),
                      onPressed: () => Navigator.of(context).push(
                        MaterialPageRoute(
                            builder: (_) => ResultScreen(machine: m)),
                      ),
                    ),
                ],
              ),
            ],
          ),
          if (_busy)
            Container(
              color: Colors.black54,
              alignment: Alignment.center,
              child: const Card(
                child: Padding(
                  padding: EdgeInsets.all(24),
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      CircularProgressIndicator(),
                      SizedBox(height: 16),
                      Text('Identifying machine...'),
                    ],
                  ),
                ),
              ),
            ),
        ],
      ),
    );
  }
}

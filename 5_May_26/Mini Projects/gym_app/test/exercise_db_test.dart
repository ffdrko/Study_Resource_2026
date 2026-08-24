import 'dart:convert';
import 'dart:io';

import 'package:flutter_test/flutter_test.dart';

void main() {
  final jsonFile = File('assets/data/exercises.json');
  final labelsFile = File('assets/model/labels.txt');

  test('exercises.json parses and every machine has exercises', () {
    expect(jsonFile.existsSync(), isTrue,
        reason: 'assets/data/exercises.json is missing');

    final data =
        jsonDecode(jsonFile.readAsStringSync()) as Map<String, dynamic>;
    final machines = data['machines'] as List;
    expect(machines, isNotEmpty);

    final ids = <String>{};
    for (final m in machines) {
      final id = m['id'] as String;
      expect(ids.add(id), isTrue, reason: 'Duplicate machine id: $id');
      expect(m['name'], isA<String>());
      expect(m['muscles'] as List, isNotEmpty);

      final exercises = m['exercises'] as List;
      expect(exercises, isNotEmpty,
          reason: 'Machine "$id" has no exercises');
      for (final e in exercises) {
        expect(e['name'], isA<String>(),
            reason: 'Exercise in "$id" missing name');
        expect(e['videoId'], isA<String>(),
            reason: 'Exercise "${e['name']}" missing videoId field');
      }
    }
  });

  test('every label in labels.txt exists in exercises.json', () {
    expect(labelsFile.existsSync(), isTrue,
        reason: 'assets/model/labels.txt is missing');
    expect(jsonFile.existsSync(), isTrue);

    final labels = labelsFile
        .readAsLinesSync()
        .map((l) => l.trim())
        .where((l) => l.isNotEmpty)
        .toSet();

    final data =
        jsonDecode(jsonFile.readAsStringSync()) as Map<String, dynamic>;
    final jsonIds = (data['machines'] as List)
        .map((m) => m['id'] as String)
        .toSet();

    for (final label in labels) {
      expect(jsonIds.contains(label), isTrue,
          reason: 'Model can predict "$label" but JSON has no such machine id');
    }

    // Warn-level: JSON entries the model was never trained on are fine,
    // they just won't be reachable via camera detection.
    // ignore: avoid_print
    print('JSON machines not in labels.txt: '
        '${jsonIds.difference(labels).join(', ')}');
  });
}

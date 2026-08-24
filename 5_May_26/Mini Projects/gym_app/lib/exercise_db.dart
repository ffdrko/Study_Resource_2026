import 'dart:convert';

import 'package:flutter/services.dart' show rootBundle;

import 'models.dart';

/// Loads assets/data/exercises.json and looks machines up by id.
/// The ids MUST match the lines in assets/model/labels.txt — that is
/// the bridge between "what the model sees" and "what the user gets".
class ExerciseDb {
  final Map<String, Machine> _byId = {};

  Future<void> load() async {
    final raw = await rootBundle.loadString('assets/data/exercises.json');
    final list = (jsonDecode(raw) as Map<String, dynamic>)['machines'] as List;
    for (final item in list) {
      final machine = Machine.fromJson(item as Map<String, dynamic>);
      _byId[machine.id] = machine;
    }
  }

  /// YOLO label -> Machine, e.g. find("leg_press")
  Machine? find(String? label) =>
      (label == null || !_byId.containsKey(label)) ? null : _byId[label];

  List<Machine> get all => _byId.values.toList();
}

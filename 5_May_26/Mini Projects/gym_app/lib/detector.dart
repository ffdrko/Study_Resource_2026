import 'dart:math';

import 'package:flutter/services.dart' show rootBundle;
import 'package:image/image.dart' as img;
import 'package:tflite_flutter/tflite_flutter.dart';

/// Common interface so the app works before your YOLO model is trained.
abstract class Detector {
  bool get isDemoMode;

  /// Returns a machine id (must match "id" fields in exercises.json),
  /// or null if nothing is recognized with enough confidence.
  String? detect(img.Image photo);
}

/// Builds the real detector if assets/model/yolo_model.tflite exists,
/// otherwise falls back to [DemoDetector] so you can develop the full
/// UI flow (photo -> label -> JSON -> video) right now.
Future<Detector> createDetector() async {
  final real = TFLiteDetector();
  try {
    await real.load();
    return real;
  } catch (_) {
    return DemoDetector(await rootBundle
        .loadString('assets/model/labels.txt')
        .then((s) => s.trim().split('\n').map((l) => l.trim()).toList()));
  }
}

class TFLiteDetector implements Detector {
  static const _confidenceThreshold = 0.60;

  late final Interpreter _interpreter;
  late final List<String> _labels;
  int _inputWidth = 640;
  int _inputHeight = 640;

  @override
  bool get isDemoMode => false;

  Future<void> load() async {
    _interpreter =
        await Interpreter.fromAsset('assets/model/yolo_model.tflite');

    final inputShape = _interpreter.getInputTensor(0).shape; // [1, H, W, 3]
    _inputHeight = inputShape[1];
    _inputWidth = inputShape[2];

    final raw = await rootBundle.loadString('assets/model/labels.txt');
    _labels = raw.trim().split('\n').map((l) => l.trim()).toList();
  }

  @override
  String? detect(img.Image photo) {
    final input = _preprocess(photo);
    final outputShape = _interpreter.getOutputTensor(0).shape;
    final output = [_allocateOutput(outputShape)];
    _interpreter.run(input, output);

    final best = _pickBest(output.first, outputShape);
    if (best == null || best.$2 < _confidenceThreshold) return null;
    return best.$1 < _labels.length ? _labels[best.$1] : null;
  }

  List<List<List<List<double>>>> _preprocess(img.Image photo) {
    final resized = img.copyResize(photo,
        width: _inputWidth,
        height: _inputHeight,
        interpolation: img.Interpolation.linear);
    return [
      List.generate(
        _inputHeight,
        (y) => List.generate(
          _inputWidth,
          (x) {
            final p = resized.getPixel(x, y);
            return [p.r / 255.0, p.g / 255.0, p.b / 255.0];
          },
        ),
      )
    ];
  }

  Object _allocateOutput(List<int> shape) {
    // Handles [1, N, C] and the transposed YOLOv8 export layout [1, C, N].
    if (shape.length == 3) {
      return List.generate(shape[1],
        (_) => List.filled(shape[2], 0.0), growable: false);
    }
    throw UnsupportedError('Unexpected model output shape: $shape');
  }

  /// Scans every box/class cell and returns (classIndex, score) of the best.
  ///
  /// Layout A (classic): [1][box][5 + classes] -> x,y,w,h,obj,class...
  /// Layout B (YOLOv8):  [1][4 + classes][box] -> needs transpose.
  (int, double)? _pickBest(Object rawOut, List<int> shape) {
    final out = rawOut as List;
    if (out.isEmpty || out.first is! List) return null;
    final rows = out.length;
    final cols = (out.first as List).length;
    final transposed = rows < cols; // e.g. [84][8400]

    var bestIdx = -1;
    var bestScore = 0.0;

    if (!transposed) {
      final numClasses = cols - 4 - 1; // minus xywh and objectness
      for (var b = 0; b < rows; b++) {
        final row = out[b] as List;
        for (var c = 0; c < numClasses; c++) {
          final s = (row[c + 5] as num).toDouble();
          if (s > bestScore) {
            bestScore = s;
            bestIdx = c;
          }
        }
      }
    } else {
      for (var n = 0; n < cols; n++) {
        for (var c = 4; c < rows; c++) {
          final s = ((out[c] as List)[n] as num).toDouble();
          if (s > bestScore) {
            bestScore = s;
            bestIdx = c - 4;
          }
        }
      }
    }
    return bestIdx >= 0 ? (bestIdx, bestScore) : null;
  }
}

/// Stand-in detector used until yolo_model.tflite is added to
/// assets/model/. Picks a machine deterministically from the photo's
/// pixels so the same image always gives the same result — good enough
/// to build and demo the entire pipeline end-to-end.
class DemoDetector implements Detector {
  DemoDetector(this._labels);

  final List<String> _labels;
  int _counter = 0;

  @override
  bool get isDemoMode => true;

  @override
  String? detect(img.Image photo) {
    if (_labels.isEmpty) return null;
    var hash = 0;
    final total = photo.width * photo.height;
    final step = max(1, total ~/ 5000);
    for (var i = 0; i < total; i += step) {
      final p = photo.getPixel(i % photo.width, i ~/ photo.width);
      hash += p.r.toInt() + p.g.toInt() + p.b.toInt();
    }
    // Mix in a counter so repeated taps cycle through machines.
    return _labels[(hash + _counter++) % _labels.length];
  }
}

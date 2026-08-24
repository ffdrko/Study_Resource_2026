class Exercise {
  final String name;
  final String sets;
  final String reps;
  final String tips;
  final String videoId;

  const Exercise({
    required this.name,
    required this.sets,
    required this.reps,
    required this.tips,
    required this.videoId,
  });

  factory Exercise.fromJson(Map<String, dynamic> j) => Exercise(
        name: j['name'] as String,
        sets: j['sets'] as String? ?? '',
        reps: j['reps'] as String? ?? '',
        tips: j['tips'] as String? ?? '',
        videoId: j['videoId'] as String? ?? '',
      );

  /// True if a curated YouTube video exists for this exercise.
  bool get hasVideo => videoId.isNotEmpty;
}

class Machine {
  final String id;
  final String name;
  final List<String> muscles;
  final List<Exercise> exercises;

  const Machine({
    required this.id,
    required this.name,
    required this.muscles,
    required this.exercises,
  });

  factory Machine.fromJson(Map<String, dynamic> j) => Machine(
        id: j['id'] as String,
        name: j['name'] as String,
        muscles: List<String>.from(j['muscles'] as List),
        exercises: (j['exercises'] as List)
            .map((e) => Exercise.fromJson(e as Map<String, dynamic>))
            .toList(),
      );
}

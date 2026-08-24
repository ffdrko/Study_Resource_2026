import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

import '../models.dart';
import 'video_screen.dart';

class ResultScreen extends StatelessWidget {
  const ResultScreen({super.key, required this.machine});

  final Machine machine;

  void _searchOnYoutube(String query) {
    launchUrl(
      Uri.parse(
          'https://www.youtube.com/results?search_query=${Uri.encodeComponent("$query proper form")}'),
      mode: LaunchMode.externalApplication,
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(machine.name)),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          Card(
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      const Icon(Icons.fitness_center,
                          color: Colors.deepOrangeAccent),
                      const SizedBox(width: 8),
                      Expanded(
                        child: Text(machine.name,
                            style: Theme.of(context).textTheme.titleLarge),
                      ),
                    ],
                  ),
                  const SizedBox(height: 8),
                  Wrap(
                    spacing: 6,
                    children: [
                      for (final m in machine.muscles) Chip(label: Text(m)),
                    ],
                  ),
                ],
              ),
            ),
          ),
          const SizedBox(height: 8),
          for (final ex in machine.exercises)
            Card(
              margin: const EdgeInsets.symmetric(vertical: 6),
              child: ListTile(
                title: Text(ex.name,
                    style: const TextStyle(fontWeight: FontWeight.bold)),
                subtitle: Text('${ex.sets} sets x ${ex.reps} reps\n${ex.tips}'),
                isThreeLine: true,
                trailing: Icon(
                  ex.hasVideo ? Icons.play_circle : Icons.travel_explore,
                  size: 32,
                  color: Colors.deepOrangeAccent,
                ),
                onTap: () {
                  if (ex.hasVideo) {
                    Navigator.of(context).push(MaterialPageRoute(
                      builder: (_) => VideoScreen(videoId: ex.videoId),
                    ));
                  } else {
                    // No curated video yet -> open a YouTube keyword search.
                    _searchOnYoutube(ex.name);
                  }
                },
              ),
            ),
        ],
      ),
    );
  }
}

# GymLens 🏋️

Snap a photo of a gym machine → the app tells you what it is → shows related
exercises (sets/reps/tips) → plays a how-to video.

**Current status:** full app pipeline works in **Demo mode** (simulated
detection). Add your trained YOLO model to go live.

## Pipeline

```
photo -> TFLite YOLO model -> label ("leg_press")
                                     |
                              exercises.json lookup (id == label)
                                     |
                        ResultScreen: exercises + sets + tips
                                     |
                     tap exercise -> embedded YouTube video
```

The bridge between camera and data is simple:
`assets/model/labels.txt` lines must equal the `"id"` fields in
`assets/data/exercises.json`.

## Setup

1. Install Flutter: https://docs.flutter.dev/get-started/install/windows
2. Generate platform folders (android/ios/web) inside this repo:

```bash
cd gym_app
flutter create . --org com.example --project-name gym_app
flutter pub get
flutter run
```

3. iOS only — add camera permissions to `ios/Runner/Info.plist`:

```xml
<key>NSCameraUsageDescription</key>
<string>Used to identify gym machines from photos.</string>
<key>NSPhotoLibraryUsageDescription</key>
<string>Pick a machine photo from your gallery.</string>
```

4. Android: `minSdkVersion 21+` is required by tflite_flutter.

## Train your own machine-detection model (free)

1. Collect ~150–300 photos per machine (your phone + Kaggle/Roboflow datasets).
2. Annotate boxes on https://roboflow.com (free tier), export **YOLOv8** format.
3. Train on Google Colab free GPU (~1 hour):

```python
!pip install ultralytics
from ultralytics import YOLO
model = YOLO('yolov8n.pt')
model.train(data='data.yaml', epochs=50, imgsz=640)
# Export for mobile:
model.export(format='tflite')
```

4. Copy the exported `yolo_model.tflite` into `assets/model/`.
   The app auto-switches from Demo mode to real detection.

> Note: `lib/detector.dart` output parsing supports both classic
> `[1][box][5+classes]` and YOLOv8 `[1][classes+4][boxes]` export layouts.
> If scores look wrong, print `_pickBest()` inputs and adjust once.

## Adding machines / videos

- New machine: add an entry to `assets/data/exercises.json` AND a matching
  line to `assets/model/labels.txt` (same string, same order as training).
- Videos: paste any YouTube URL's ID (the part after `watch?v=`) into
  `videoId`. Empty `videoId` = the app opens a YouTube keyword search
  instead (no API key needed).

## Tests

```bash
flutter test
```

Validates JSON structure and that every model label has a matching machine id.

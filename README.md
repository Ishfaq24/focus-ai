# FocusGuard AI 🎓👁️📱

FocusGuard AI is a real-time, AI-powered student monitoring system built with Python, OpenCV, Mediapipe, and YOLOv8. It ensures focus during study sessions or online exams by detecting mobile phone usage, drowsiness, and physical absence from the screen, accompanied by an intelligent audio alert system.

## Features

- **📱 Phone Detection**: Uses YOLOv8 to identify if a mobile device is held up to the screen.
- **😴 Drowsiness Detection**: Calculates Eye Aspect Ratio (EAR) via Mediapipe's precise facial landmarks to detect sleepiness.
- **🪑 Absence Detection**: Tracks if the user leaves the frame for an extended period.
- **🔊 Smart Audio Alerts**: Uses non-blocking audio cues with customizable cooldowns to prevent alarm spam.
- **⚙️ Highly Configurable**: Easily tweak thresholds, cooldowns, and feature toggles in `config.py`.

## Project Structure

```text
focusguard-ai/
├── main.py                # Main application loop
├── config.py              # Configuration and thresholds
├── requirements.txt       # Dependencies
├── detection/             # Modules for AI logic (YOLO, Mediapipe)
├── utils/                 # Helpers and Pygame audio logic
└── assets/audio/          # Place your MP3 files here
```

## Setup Instructions

### 1. Prerequisites
Ensure you have Python 3.8+ installed on your system.

### 2. Install Dependencies
Clone the repository and install the required Python packages:
```bash
pip install -r requirements.txt
```

### 3. Add Audio Files
Create an `assets/audio` folder in the root directory and add the following MP3 files (or adjust paths in `utils/constants.py`):
- `assets/audio/phone_alert.mp3`
- `assets/audio/sleep_alert.mp3`
- `assets/audio/absence_alert.mp3`

### 4. Run the Application
Start the monitoring system by running:
```bash
python main.py
```

## Configuration
Open `config.py` to customize the system:
- **`EAR_THRESHOLD`**: Adjust the eye-closing sensitivity (Default `0.25`).
- **`CONSECUTIVE_FRAMES_SLEEP`**: How long eyes must be closed to trigger an alert.
- **`ABSENCE_TIME_SECONDS`**: Seconds allowed away from the screen.
- **`DEBUG_MODE`**: Set to `True` to see bounding boxes and facial landmarks overlay.

## Troubleshooting
- **No Audio?** Ensure the MP3 files are named exactly as specified and placed in the correct `assets/audio/` directory.
- **Slow Performance?** Turn off `DEBUG_MODE` in `config.py` to stop drawing face meshes, which improves FPS significantly.# focus-ai

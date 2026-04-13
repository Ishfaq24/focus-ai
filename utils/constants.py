import os

# Base Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
AUDIO_DIR = os.path.join(ASSETS_DIR, "audio")
MODELS_DIR = os.path.join(BASE_DIR, "models")

# Audio Files
AUDIO_PHONE = os.path.join(AUDIO_DIR, "phone_alert.mp3")
AUDIO_SLEEP = os.path.join(AUDIO_DIR, "sleep_alert.mp3")
AUDIO_ABSENCE = os.path.join(AUDIO_DIR, "absence_alert.mp3")

# Colors (BGR for OpenCV)
COLOR_GREEN = (0, 255, 0)
COLOR_RED = (0, 0, 255)
COLOR_BLUE = (255, 0, 0)
COLOR_YELLOW = (0, 255, 255)
COLOR_WHITE = (255, 255, 255)

# Text Settings
FONT_SCALE = 0.7
FONT_THICKNESS = 2
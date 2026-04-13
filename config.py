# Configuration settings for FocusGuard AI

# Feature Toggles
ENABLE_PHONE_DETECTION = True
ENABLE_DROWSINESS_DETECTION = True
ENABLE_ABSENCE_DETECTION = True
DEBUG_MODE = True  # Shows landmarks and bounding boxes

# Thresholds
EAR_THRESHOLD = 0.25           # Eye Aspect Ratio threshold below which eyes are considered closed
CONSECUTIVE_FRAMES_SLEEP = 15  # Number of consecutive frames eyes must be closed to trigger alert
CONSECUTIVE_FRAMES_PHONE = 10  # Number of consecutive frames phone must be detected
ABSENCE_TIME_SECONDS = 5.0     # Seconds without face before triggering absence alert

# Audio Cooldowns (Seconds) to prevent spam
COOLDOWN_SLEEP = 5.0
COOLDOWN_PHONE = 5.0
COOLDOWN_ABSENCE = 5.0

# YOLO Settings
YOLO_MODEL_NAME = "yolov8n.pt" # Nano model for real-time performance
PHONE_CLASS_ID = 67            # COCO dataset class ID for 'cell phone'
YOLO_CONFIDENCE = 0.45         # Confidence threshold for phone detection
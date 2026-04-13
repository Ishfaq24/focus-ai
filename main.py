import cv2
import time
import logging

import config
from utils.audio_alert import AudioAlertSystem
from utils.helpers import FPSCounter, draw_text
from utils.constants import COLOR_RED, COLOR_YELLOW, COLOR_WHITE

from detection.face_detection import FaceDetector
from detection.drowsiness import DrowsinessDetector
from detection.phone_detection import PhoneDetector

def main():
    logging.info("Initializing FocusGuard AI...")
    
    # Initialize Detectors
    face_detector = FaceDetector()
    drowsiness_detector = DrowsinessDetector()
    phone_detector = PhoneDetector()
    audio_system = AudioAlertSystem()
    fps_counter = FPSCounter()

    # Video Capture
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        logging.error("Could not open webcam.")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    absence_start_time = None

    logging.info("System Ready. Press 'q' to quit.")

    while True:
        success, frame = cap.read()
        if not success:
            break

        # Flip frame horizontally for selfie-view display
        frame = cv2.flip(frame, 1)
        active_alerts = []

        # 1. Face & Drowsiness Detection
        results, landmarks = face_detector.process(frame)
        
        if landmarks:
            absence_start_time = None  # Reset absence timer
            
            if config.DEBUG_MODE:
                face_detector.draw_landmarks(frame, results)

            if config.ENABLE_DROWSINESS_DETECTION:
                is_drowsy, ear = drowsiness_detector.detect(landmarks)
                if is_drowsy:
                    active_alerts.append("DROWSINESS DETECTED")
                    audio_system.play_alert("sleep")
                
                if config.DEBUG_MODE:
                    draw_text(frame, f"EAR: {ear:.2f}", (10, 60), COLOR_WHITE)
        else:
            # Absence Detection
            if config.ENABLE_ABSENCE_DETECTION:
                if absence_start_time is None:
                    absence_start_time = time.time()
                elif time.time() - absence_start_time > config.ABSENCE_TIME_SECONDS:
                    active_alerts.append("NO FACE DETECTED")
                    audio_system.play_alert("absence")

        # 2. Phone Detection
        if config.ENABLE_PHONE_DETECTION:
            is_phone, phone_boxes = phone_detector.detect(frame)
            if config.DEBUG_MODE and phone_boxes:
                phone_detector.draw_boxes(frame, phone_boxes)
            
            if is_phone:
                active_alerts.append("PHONE DETECTED")
                audio_system.play_alert("phone")

        # 3. UI Overlays
        fps = fps_counter.update()
        draw_text(frame, f"FPS: {fps}", (10, 30), COLOR_YELLOW)

        # Draw Active Alerts
        y_pos = 100
        for alert in active_alerts:
            draw_text(frame, alert, (10, y_pos), COLOR_RED, font_scale=0.8, thickness=2)
            y_pos += 35

        # Show output
        cv2.imshow('FocusGuard AI', frame)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
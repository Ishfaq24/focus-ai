import numpy as np
import config

class DrowsinessDetector:
    def __init__(self):
        # Mediapipe eye landmarks indices
        self.LEFT_EYE = [33, 160, 158, 133, 153, 144]
        self.RIGHT_EYE = [362, 385, 387, 263, 373, 380]
        self.sleep_frame_counter = 0

    def calculate_ear(self, eye_landmarks):
        # Distance between vertical eye landmarks
        v1 = np.linalg.norm(np.array(eye_landmarks[1]) - np.array(eye_landmarks[5]))
        v2 = np.linalg.norm(np.array(eye_landmarks[2]) - np.array(eye_landmarks[4]))
        # Distance between horizontal eye landmarks
        h = np.linalg.norm(np.array(eye_landmarks[0]) - np.array(eye_landmarks[3]))
        
        # EAR calculation
        ear = (v1 + v2) / (2.0 * h)
        return ear

    def detect(self, landmarks):
        if not landmarks:
            self.sleep_frame_counter = 0
            return False, 0.0

        left_eye_pts = [landmarks[i] for i in self.LEFT_EYE]
        right_eye_pts = [landmarks[i] for i in self.RIGHT_EYE]

        left_ear = self.calculate_ear(left_eye_pts)
        right_ear = self.calculate_ear(right_eye_pts)

        avg_ear = (left_ear + right_ear) / 2.0

        is_drowsy = False
        if avg_ear < config.EAR_THRESHOLD:
            self.sleep_frame_counter += 1
            if self.sleep_frame_counter >= config.CONSECUTIVE_FRAMES_SLEEP:
                is_drowsy = True
        else:
            self.sleep_frame_counter = 0

        return is_drowsy, avg_ear
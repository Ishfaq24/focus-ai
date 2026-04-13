from ultralytics import YOLO
import cv2
import os
import config
from utils.constants import MODELS_DIR

class PhoneDetector:
    def __init__(self):
        os.makedirs(MODELS_DIR, exist_ok=True)
        model_path = os.path.join(MODELS_DIR, config.YOLO_MODEL_NAME)
        # Ultralytics will auto-download the model if not present in the current directory
        self.model = YOLO(config.YOLO_MODEL_NAME)
        self.phone_frame_counter = 0

    def detect(self, frame):
        # Run YOLO inference, looking only for the phone class (67)
        results = self.model(frame, classes=[config.PHONE_CLASS_ID], conf=config.YOLO_CONFIDENCE, verbose=False)
        
        boxes = []
        is_phone_detected = False

        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                boxes.append((x1, y1, x2, y2, conf))
        
        if boxes:
            self.phone_frame_counter += 1
            if self.phone_frame_counter >= config.CONSECUTIVE_FRAMES_PHONE:
                is_phone_detected = True
        else:
            self.phone_frame_counter = max(0, self.phone_frame_counter - 1)

        return is_phone_detected, boxes

    def draw_boxes(self, frame, boxes):
        for (x1, y1, x2, y2, conf) in boxes:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(frame, f"Phone: {conf:.2f}", (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
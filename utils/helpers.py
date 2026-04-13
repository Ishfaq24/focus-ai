import cv2
import time
from utils.constants import COLOR_GREEN, FONT_SCALE, FONT_THICKNESS

class FPSCounter:
    def __init__(self):
        self.pTime = 0

    def update(self):
        cTime = time.time()
        fps = 1 / (cTime - self.pTime) if (cTime - self.pTime) > 0 else 0
        self.pTime = cTime
        return int(fps)

def draw_text(img, text, position, color=COLOR_GREEN, font_scale=FONT_SCALE, thickness=FONT_THICKNESS):
    """Utility to draw text with a black background outline for better visibility."""
    x, y = position
    # Draw outline
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 0), thickness + 2)
    # Draw text
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)
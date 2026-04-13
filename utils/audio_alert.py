import pygame
import time
import os
import logging
from utils.constants import AUDIO_PHONE, AUDIO_SLEEP, AUDIO_ABSENCE
import config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class AudioAlertSystem:
    def __init__(self):
        # Initialize the mixer for audio
        pygame.mixer.init()
        self.last_played = {
            "sleep": 0,
            "phone": 0,
            "absence": 0
        }
        
        # Store file paths instead of pre-loading them
        self.audio_paths = {
            "phone": AUDIO_PHONE,
            "sleep": AUDIO_SLEEP,
            "absence": AUDIO_ABSENCE
        }

    def play_alert(self, alert_type):
        current_time = time.time()
        
        # Determine cooldown based on alert type
        cooldown = 5.0
        if alert_type == "sleep": cooldown = config.COOLDOWN_SLEEP
        elif alert_type == "phone": cooldown = config.COOLDOWN_PHONE
        elif alert_type == "absence": cooldown = config.COOLDOWN_ABSENCE

        # Check cooldown to prevent spamming the audio
        if current_time - self.last_played.get(alert_type, 0) > cooldown:
            path = self.audio_paths.get(alert_type)
            
            # Verify the file actually exists
            if path and os.path.exists(path):
                try:
                    # Using mixer.music is much more reliable for MP3 files on Windows
                    pygame.mixer.music.load(path)
                    pygame.mixer.music.play()
                    logging.info(f"🔊 Triggered Audio Alert: {alert_type.upper()}")
                    self.last_played[alert_type] = current_time
                except Exception as e:
                    logging.error(f"Error playing sound {alert_type}: {e}")
            else:
                logging.warning(f"⚠️ Audio file missing at: {path}")
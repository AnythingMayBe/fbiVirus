from playsound import playsound
import time
import random

class Virus:
    def __init__(self):
        self.config = {
            "audioPath": "audio.mp3", # The video you want to ear,
            "minTimeToWait": 10, # The minimum time in seconds you want to wait before you can ear the sound
            "maxTimeToWait": 30 # The maximum time in seconds you want to wait before you can ear the sound
        }
    
    def earAudio(self):
        playsound(self.config["audioPath"])
    
    def waitBeforeEaring(self):
        time.sleep(random.randint(self.config["minTimeToWait"], self.config["minTimeToWait"]))
        self.earAudio()

if __name__ == "__main__":
    instance = Virus()
    instance.waitBeforeEaring()
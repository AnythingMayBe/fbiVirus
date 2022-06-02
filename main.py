from playsound import playsound
import time
import random
import os
import requests

class Virus:
    def __init__(self):
        self.config = {
            "audioPath": "audio.mp3", # The video you want to ear,
            "minTimeToWait": 10, # The minimum time in seconds you want to wait before you can ear the sound
            "maxTimeToWait": 30, # The maximum time in seconds you want to wait before you can ear the sound
            "audioRecover": "http://localhost:8000/audio.mp3" # The URL you want to download on if the file is not found
        }
    
    def earAudio(self):
        if os.path.exists(self.config["audioPath"]): playsound(self.config["audioPath"])
        else:
            r = requests.get(self.config["audioRecover"])
            with open(self.config["audioPath"], "wb") as file:
                file.write(r.content)
                file.close()
            playsound(self.config["audioPath"])

    def waitBeforeEaring(self):
        time.sleep(random.randint(self.config["minTimeToWait"], self.config["minTimeToWait"]))
        self.earAudio()

if __name__ == "__main__":
    instance = Virus()
    instance.waitBeforeEaring()
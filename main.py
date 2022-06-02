from playsound import playsound

class Virus:
    def __init__(self):
        self.config = {
            "audioPath": "audio.mp3" # The video you want to ear
        }
    
    def earAudio(self):
        playsound(self.config["audioPath"])

if __name__ == "__main__":
    instance = Virus()
    instance.earAudio()
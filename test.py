
from gtts import gTTS
import os
file = open("text.txt", "r").readline().replace("\n", " ")

language = 'en'

speech = gTTS(text = str(file), lang = 'language', slow = False)

speech.save("voice.mp3")

os.system("start voice.mp3")
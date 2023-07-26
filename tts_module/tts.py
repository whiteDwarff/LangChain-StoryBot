from gtts import gTTS
from playsound import playsound

def tts(text):
    tts = gTTS(text, lang='ko')
    tts.save("./mp3/role_response.mp3")
    return playsound("./mp3/role_response.mp3")

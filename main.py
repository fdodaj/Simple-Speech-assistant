import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            john_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            john_speak("Sorry try again")
        except sr.RequestError:
            john_speak("My services are down")
        return voice_data

def john_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1,1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'who are you' in voice_data:
        john_speak("My name is John")
    if 'what time is it' in voice_data:
        john_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        john_speak('here is what i found for ' + search)
    if 'find this place' in voice_data:
        location = record_audio('What is the location')
        url = 'https://www.google.nl/maps/place/=' + location + '/&amp;'
        webbrowser.get().open(url)
        john_speak('here is the location of ' + location)
    if 'bye' in voice_data:
        exit()


time.sleep(1)
john_speak("Ask me anything")
while 1:
    voice_data = record_audio()
    respond(voice_data)
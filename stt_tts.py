import random 
import speech_recognition as sr
import pyttsx3
import datetime
import csv
import time

print("welcome\n")

stt = input("stt? : ")
tts = input("tts? : ")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voices", voices[0].id)
engine.setProperty("rate", 178)

def talk(audio):  #tts func to make our program say something
    engine.say(audio)
    engine.runAndWait()

def listen():  #stt func to get input from the user's mic
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=3)
        print("Listening . . ")
        audio = r.listen(source)

    data = " "

    try:
        data = r.recognize_google(audio,language='en')
        print("You said " + data)

    except sr.UnknownValueError:
        print("Sorry, could not understand that.")
    except sr.RequestError as ex:
        print("Request Error from Google Speech Recognition" + ex)

    return data

if "yes" in stt.lower():
    print("\n now say say smtg: ")
    stt_response = listen()

time.sleep(1)

# print(f"\n u said {stt_response} .")

if "yes" in tts.lower():
    tts_sample_text = input("here: ")

    talk(tts_sample_text) 
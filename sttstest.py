import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
import random 
import speech_recognition as sr
import pyttsx3
import time
class TestClass(Widget):

    stt_response= StringProperty("")
    tts_sample_text=StringProperty("")
    

    def welcome(self):
        print("welcome\n")

        self.stt = input("stt? : ")
        self.tts = input("tts? : ")

    

    def talk(audio):  #tts func to make our program say something
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty("voices", voices[0].id)
        engine.setProperty("rate", 178)
        engine.say(audio)
        engine.runAndWait()

    def listen(self):  #stt func to get input from the user's mic
        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=3)
            print("Listening . . ")
            self.audio = r.listen(source)

        self.data = " "

        try:
            self.data = r.recognize_google(self.audio,language='en')
            print("You said " + self.data)

        except sr.UnknownValueError:
            print("Sorry, could not understand that.")
        except sr.RequestError as ex:
            print("Request Error from Google Speech Recognition" + ex)

        return self.data

    def use_stt(self):
        if "yes" in self.stt.lower():
            print("\n now say say smtg: ")
            self.stt_response = self.listen()
            time.sleep(1)


    # print(f"\n u said {stt_response} .")

    def use_tts(self):
        if "yes" in self.tts.lower():
            self.tts_sample_text = input("here: ")

            self.talk(self.tts_sample_text)

class TestApp(App):
    def build(self):
        return(Builder.load_file("my.kv")) 

if __name__=="__main__":
    TestApp().run()
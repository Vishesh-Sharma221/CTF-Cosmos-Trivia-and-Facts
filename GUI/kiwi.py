from re import A
import kivy
from kivy.metrics import dp
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty

#window size
wfac=3
Window.size=(dp((40-wfac)*9), dp((40-wfac)*16))

#requirements
import csv
from os import extsep
import random
import pyttsx3
import speech_recognition as sr
import time

ques_file=open("questions.csv")
read_ques_file=csv.reader(ques_file)
ques=[]         # 1-Q, 2-O1, 3-O2, 4-O3, 5-O4, 6-A
for x in read_ques_file:
    ques.append(x)

looplist=[]
class Home(Screen):
    pass

class Setting(Screen):
    pass

class GameMode(Screen):
    pass
r=random.randint(1,len(ques)-1)
quiz_score = 0
check=""

class QuizQues1(Screen):
    global quiz_score
    global ques
    global looplist
    global r
    global check
    
    A=0
    B=0
    C=0
    D=0
    ans=StringProperty(f"{check}")

    #functions
    r=random.randint(1,len(ques)-1)
    ans1,ans2,ans3,ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]
    question=StringProperty(f"\nQuestion 1: {ques[r][1]}")
    opt1=StringProperty(f"1.    {ques[r][2]}")
    opt2=StringProperty(f"2.    {ques[r][3]}")
    opt3=StringProperty(f"3.    {ques[r][4]}")
    opt4=StringProperty(f"4.    {ques[r][5]}")
    
    # removing the used ques for this quiz
    looplist.insert(0, ques.pop(r))

    if len(ques)==1:
        for i in range(len(looplist)):
            ques.insert(1, looplist.pop(i))

    def inputA(self, button):
        self.A="1"
    def inputB(self, button):
        self.A="2"
    def inputC(self, button):
        self.A="3"
    def inputD(self, button):
        self.A="4"
    def check_quiz_ans(self):
        global quiz_score
        global check
        if (self.A=="1" and self.ans1==ques[r][6]) or (self.A=="2" and self.ans2==ques[r][6])\
        or (self.A=="3" and self.ans3==ques[r][6]) or (self.A=="4" and self.ans4==ques[r][6]):
            quiz_score += 1
            check="true"
        else:
            check="false"
        
        self.ans=StringProperty(f"{check}")

class QuizQues2(Screen):
    global quiz_score
    global ques
    global looplist
    global r

    #functions
    r=random.randint(1,len(ques)-1)
    ans1,ans2,ans3,ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]
    question=StringProperty(f"\nQuestion 2: {ques[r][1]}")
    opt1=StringProperty(f"1.    {ques[r][2]}")
    opt2=StringProperty(f"2.    {ques[r][3]}")
    opt3=StringProperty(f"3.    {ques[r][4]}")
    opt4=StringProperty(f"4.    {ques[r][5]}")
     
    # removing the used ques for this quiz
    looplist.insert(0, ques.pop(r))

    if len(ques)==1:
        for i in range(len(looplist)):
            ques.insert(1, looplist.pop(i))

class QuizQues3(Screen):
    global quiz_score
    global ques
    global looplist
    global r
    
    #functions
    r=random.randint(1,len(ques)-1)
    ans1,ans2,ans3,ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]
    question=StringProperty(f"\nQuestion 3: {ques[r][1]}")
    opt1=StringProperty(f"1.    {ques[r][2]}")
    opt2=StringProperty(f"2.    {ques[r][3]}")
    opt3=StringProperty(f"3.    {ques[r][4]}")
    opt4=StringProperty(f"4.    {ques[r][5]}")
     
    # removing the used ques for this quiz
    looplist.insert(0, ques.pop(r))

    if len(ques)==1:
        for i in range(len(looplist)):
            ques.insert(1, looplist.pop(i))

class QuizQues4(Screen):
    global quiz_score
    global ques
    global looplist
    global r
    
    #functions
    r=random.randint(1,len(ques)-1)
    ans1,ans2,ans3,ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]
    question=StringProperty(f"\nQuestion 4: {ques[r][1]}")
    opt1=StringProperty(f"1.    {ques[r][2]}")
    opt2=StringProperty(f"2.    {ques[r][3]}")
    opt3=StringProperty(f"3.    {ques[r][4]}")
    opt4=StringProperty(f"4.    {ques[r][5]}")
     
    # removing the used ques for this quiz
    looplist.insert(0, ques.pop(r))

    if len(ques)==1:
        for i in range(len(looplist)):
            ques.insert(1, looplist.pop(i))

class QuizQues5(Screen):
    global quiz_score
    global ques
    global looplist
    global r

    #functions
    r=random.randint(1,len(ques)-1)
    ans1,ans2,ans3,ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]
    question=StringProperty(f"\nQuestion 5: {ques[r][1]}")
    opt1=StringProperty(f"1.    {ques[r][2]}")
    opt2=StringProperty(f"2.    {ques[r][3]}")
    opt3=StringProperty(f"3.    {ques[r][4]}")
    opt4=StringProperty(f"4.    {ques[r][5]}")
     
    # removing the used ques for this quiz
    looplist.insert(0, ques.pop(r))

    if len(ques)==1:
        for i in range(len(looplist)):
            ques.insert(1, looplist.pop(i))

    quiz_score=0

class RapidFire(Screen):
    pass

class Facts(Screen):
    pass

class SolarFacts(Screen):
    pass

class Result(Screen):
    pass

class EndScreen(Screen):
    pass



class WindowManager(ScreenManager):
    pass

#misc requirements
class WrappedLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            width=lambda *x:
            self.setter('text_size')(self, (self.width, None)),
            texture_size=lambda *x: self.setter('height')(self, self.texture_size[1]))

kv = Builder.load_file("mymain.kv")

class CTFApp(App):
    title="CTF - Cosmos Trivia and Facts"
    icon="images/appicon.ico"
    def build(self):
        return kv

if __name__ == "__main__":
    CTFApp().run()
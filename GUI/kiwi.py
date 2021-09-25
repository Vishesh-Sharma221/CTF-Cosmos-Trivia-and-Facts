import kivy
from kivy.metrics import dp
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty

#window size
wfac=3
Window.size=(dp((40-wfac)*9), dp((40-wfac)*16))

#other requirements
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
r=random.randint(0,len(ques)-1)
loopques=[]

fact_file=open("facts.txt")
facts=fact_file.readlines()
rf=random.randint(1,len(facts)-1)
loopfact=[]


class Home(Screen):
    pass

class Setting(Screen):
    pass

class Info(Screen):
    file=open("GUI/info.txt")
    info=file.read()
    infos = StringProperty(f"{info}")

class GameMode(Screen):
    pass

class Quiz(Screen):
    global ques
    global loopques
    global r
    
    if len(ques)==1:
        for i in range(len(loopques)):
            ques.insert(1, loopques.pop(i))

    #default vals
    quiz_score = StringProperty("0")
    check=StringProperty("")
    ques_no=1

    #variables    
    A=StringProperty("0")
    B=StringProperty("0")
    C=StringProperty("0")
    D=StringProperty("0")
    ans=StringProperty(f"{check}")
    nexttohome=StringProperty("Next")
    
    r=random.randint(1,len(ques)-1)
    ans1,ans2,ans3,ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]
    question=StringProperty(f"\nQuestion {int(ques_no)}:\n{ques[r][1]}")
    opt1=StringProperty(f"1.    {ques[r][2]}")
    opt2=StringProperty(f"2.    {ques[r][3]}")
    opt3=StringProperty(f"3.    {ques[r][4]}")
    opt4=StringProperty(f"4.    {ques[r][5]}")

    # removing the used ques for this quiz
    loopques.insert(0, ques.pop(r))

    

    def start_quiz_ques(self, buttonnext, buttonhome):
        global ques
        global loopques
        global r
        
        if len(ques)==1:
            for i in range(len(loopques)):
                ques.insert(1, loopques.pop(i))

        #functions
        self.ques_no+=1
        r=random.randint(1,len(ques)-1)
        self.ans1,self.ans2,self.ans3,self.ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]
        self.question=f"\nQuestion {int(self.ques_no)}: {ques[r][1]}"
        self.opt1=f"1.    {ques[r][2]}"
        self.opt2=f"2.    {ques[r][3]}"
        self.opt3=f"3.    {ques[r][4]}"
        self.opt4=f"4.    {ques[r][5]}"
        
        # removing the used ques for this quiz
        loopques.insert(0, ques.pop(r))

        

        if self.ques_no==5:
            self.ques_no=1
            buttonhome.disabled = False
            buttonnext.disabled = True

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
            self.quiz_score += 1
            check="true"
        else:
            check="false"
        
        self.ans=f"{check}"

class RapidFire(Screen):
    pass

class Facts(Screen):
    global facts
    global loopfact
    global rf
    
    if len(facts)==0:
        for i in range(len(loopfact)):
            facts.insert(1, loopfact.pop(i))

    rf=random.randint(0,len(facts)-1)
    fact=StringProperty(f"Click on the button below to load a space fact.")
    morefact=StringProperty("Click For Space Facts")
    diduno=StringProperty("")
    
    loopfact.insert(0, facts.pop(rf))

    

    def show_more_facts(self, button):
        global facts
        global loopfact
        global rf
        
        if len(facts)==0:
            for i in range(len(loopfact)):
                facts.insert(1, loopfact.pop(i))
        
        rf=random.randint(0,len(facts)-1)
        self.fact=f"{facts[rf]}"
        self.morefact="One More Fact"

        self.diduno="Did you know?"

        loopfact.insert(0, facts.pop(rf))

        




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
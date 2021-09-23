import kivy
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

Window.size=(600,500)

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
class GameMode(Screen):
    pass


class Quiz(Screen):
    
    #functions
    score = 0
    ques_no=1
    r=random.randint(1,len(ques)-1)
    ans1,ans2,ans3,ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]
    question=StringProperty(f"\nQuestion {str(ques_no)}: {ques[r][1]}")
    opt1=StringProperty(f"1.    {ques[r][2]}")
    opt2=StringProperty(f"2.    {ques[r][3]}")
    opt3=StringProperty(f"3.    {ques[r][4]}")
    opt4=StringProperty(f"4.    {ques[r][5]}")
     
    # removing the used ques for this quiz
    looplist.insert(0, ques.pop(r))

    if len(ques)==1:
        for i in range(len(looplist)):
            ques.insert(1, looplist.pop(i))

    

    def check_quiz_ans(self, answer,r,ans1,ans2,ans3,ans4):
    
        if (answer=="1" and ans1!=ques[r][6]) or (answer=="2" and ans2!=ques[r][6])\
        or (answer=="3" and ans3!=ques[r][6]) or (answer=="4" and ans4!=ques[r][6] or answer==" "):
            checked=f"\nYour answer is incorrect.\nThe correct answer to this question is {ques[r][6]}."
            

        else:
            Quiz.score += 1

            



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

class MyMainApp(App):
    title="Space"
    icon="black-hole-icon.ico"
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()
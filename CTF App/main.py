import kivy
from kivy.metrics import dp
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty

#App Version
__version__="00.00.10"

#window size
Wfac=3
WindowWidth= (40-Wfac)*9
WindowHeight= (40-Wfac)*16
Window.size=(dp(WindowWidth), dp(WindowHeight))

#other requirements
import csv
from os import extsep
import random
import pyttsx3
# import speech_recognition as sr
import time

info_content='''Developers:

    -> Vishesh Sharma
    -> Yugam Sehgal
    -> Anshuman Khatri'''

ques_content='''Q NO.,Question,Option 1,Option 2,Option 3,Option 4,Answer
1,Which is the smallest planet within our solar system?,Mercury,Uranus,Mars,Venus,Mercury
2,Which is the second smallest planet within our solar system?,Neptune,Mercury,Venus,Mars,Mars
3,The moon called Titan orbits which planet?,Saturn,Jupiter,Venus,Mars,Saturn
4,Which is the brightest planet in the night's sky?,Neptune,Mercury,Jupiter,Venus,Venus
5,Which is the largest planet within our solar system?,Uranus,Saturn,Jupiter,Neptune,Jupiter
6,Uranus has only been visited by what spacecraft?,Curiosity,The Voyager 2,Sputnik 1,The Voyager 1,The Voyager 2
7,Which is the only planet not named after Greek gods or goddesses?,Neptune,Earth,Saturn,Jupiter,Earth
8,There have been more missions to this planet versus any other planet. What planet is it?,Mercury,Venus,Mars,Jupiter,Mars
9,Which planet has the most moons?,Saturn,Jupiter,Uranus,Neptune,Saturn
10,Which planet has the fastest rotation?,Neptune,Mercury,Jupiter,Venus,Jupiter
11,How long is a single Earth year on Jupiter?,12,8,2,15,12
12,What phenomena keeps the planets in steady orbit around the sun?,Spaghettification,Solar winds,Vacuum of space,Gravity,Gravity
13,Which is the largest star within our solar system?,Sun,Moon,Sirius,Polaris,Sun
14,How many stars are in the Milky Way?,More than 2 million,More than 20 million,More than 10 billion,More than 100 billion,More than 100 billion
15,How old is the sun? (roughly),4 Billion,4.6 Billion,6 Billion,6.2 Billion,4.6 Billion
16,How long does it take the sun rays to reach Earth? (minutes),10,8,12,15,8
17,How long does a solar eclipse last? (minutes),10,6.5,7.5,5,7.5
18,Where is the Asteroid Belt located?,Between Mars and Jupiter,Between Venus and Mercury,Between Uranus and Neptune,Between Saturn and Jupiter,Between Mars and Jupiter
19,What color is Mars's sunset?,Red,Pink,Blue,White,Blue
20,Name the spacecraft that carried the first astronauts to the moon,Apollo 11,The Voyager 2,Sputnik 1,The Voyager 1,Apollo 11
21,How much of the universe is composed of dark matter?,0.10%,5%,27%,55%,27%
22,How many moons are currently in our solar system?,95,125,181,2,181
23,What has an incredibly strong gravitational pull that light can't even escape?,Sun,Stars,Black Hole,Nebula,Black Hole
24,Who was the first person to step on moon?,Buzz Aldrin,Neil Armstrong,Michael Collins,Rick Astley,Neil Armstrong
25,How old is the universe (in billion years)?,20.5,10.4,16.2,13.8,13.8
26,How is the distance between the sun and Earth measured?,Kilometres,Light Years,Miles,Astronomical Units,Astronomical Units
27,What protects Earth from meteoroids and radiation from the sun?,Magnetic Field,Clouds,Atmosphere,Orbit,Atmosphere
28,How many of solar system's planets can be seen without a telescope?,2,5,4,3,5
29,Which planet is closest in size to Earth?,Mercury,Venus,Mars,Neptune,Venus
30,Which is the oldest planet in our solar system?,Saturn,Mars,Jupiter,Uranus,Jupiter'''

fact_content='''Uranus is tilted on its side
Jupiter's moon Io has towering volcanic eruptions
Mars has the biggest volcano (that we know of)
Mars also has the longest valley
Venus has super-powerful winds
There is water ice everywhere
Spacecraft have visited every planet
There could be life in the solar system, somewhere
Mercury is still shrinking
There are mountains on Pluto
Footprints on the moon will stay for millions of years
Some planets have no surface to land on
Pieces of the same metal will permanently merge in space
There are interstellar objects passing through our solar system
Saturn would float in water
Jupiter has at least 79 moons
The hottest planet in our solar system is 450° C
Halley's comet passes through Earth's vicinity every 75 years
Neutron stars can spin  600 times per second
1 day on Venus is longer than 1 earthly year
In 3.75 billion years the Milky Way and Andromeda galaxies will collide
Largest known asteroid is 965 km wide
The Sun's mass takes up 99.86% of the solar system
A volcano on mars is 3 times the size of Mt.Everest
It would take 9.5 years to walk to moon
Temperature of outer space is close to absolute zero
Around 6000 satellites are currently orbiting our Earth
There are more stars in the Universe than grains of sands on Earth
Sunset on Mars appears blue
The hottest planet in our solar system is 450° C
Humanity have found around 60 potentially habitable exoplanets as of 2021
The nearest habitable planet is estimated to be 12 light years away'''

# Ques File
ques_file=open("questions.csv","w+")
ques_file.write(ques_content)
ques_file.close()
ques_file=open("questions.csv")
read_ques_file=csv.reader(ques_file)
ques=[]         # 1-Q, 2-O1, 3-O2, 4-O3, 5-O4, 6-A
for x in read_ques_file:
    ques.append(x)
r=random.randint(0,len(ques)-1)
loopques=[]

# Fact File
fact_file=open("facts.txt","w+")
fact_file.write(fact_content)
fact_file.close()

fact_file=open("facts.txt")
facts=fact_file.readlines()
rf=random.randint(1,len(facts)-1)
loopfact=[]

# Info File
infofile=open("info.txt","w+")
infofile.write(info_content)
infofile.close()

infofile=open("info.txt")
info=infofile.read()

class Home(Screen):
    pass

# class Setting(Screen):
#     pass

class Info(Screen):
    infos = StringProperty(f"{info}")

class GameMode(Screen):
    pass

class Quiz(Screen, object):
    global ques
    global loopques
    global r
    
    if len(ques)==1:
        for i in range(len(loopques)):
            ques.insert(1, loopques.pop(i))

    #default vals
    Quiz_Score = StringProperty("0")
    SCORE=0
    check=StringProperty("")
    ques_no=1

    #variables    
    ans=StringProperty("false")
    nexttohome=StringProperty("Next")
    quizcheck=StringProperty("")
    
    r=random.randint(1,len(ques)-1)
    ans1,ans2,ans3,ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]
    question_number=StringProperty(f"{int(ques_no)}")
    question=StringProperty(f"Ques: {ques[r][1]}")
    answer=StringProperty(f"{ques[r][6]}")
    opt1=StringProperty(f"1.    {ques[r][2]}")
    opt2=StringProperty(f"2.    {ques[r][3]}")
    opt3=StringProperty(f"3.    {ques[r][4]}")
    opt4=StringProperty(f"4.    {ques[r][5]}")
    talkquestion=f"Question {str(ques_no)}: {ques[r][1]}\nThe options are:\n first, {ques[r][2]}\n second, {ques[r][3]}\n third, {ques[r][4]}\n and fourth, {ques[r][5]}"
    
    # removing the used ques for this quiz
    loopques.insert(0, ques.pop(r))

    

    def start_quiz_ques(self, buttonnext, buttonhome):
        global ques
        global loopques
        global r

        self.ids.btnquizcheck.disabled=True
        self.ids.btnopt1.disabled=False
        self.ids.btnopt2.disabled=False
        self.ids.btnopt3.disabled=False
        self.ids.btnopt4.disabled=False

        if len(ques)==1:
            for i in range(len(loopques)):
                ques.insert(1, loopques.pop(i))

        #functions
        self.ques_no+=1
        r=random.randint(1,len(ques)-1)
        self.ans1,self.ans2,self.ans3,self.ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]
        self.question_number=f"{self.ques_no}"
        self.question=f"Ques: {ques[r][1]}"
        self.answer=ques[r][6]
        self.opt1=f"1.    {ques[r][2]}"
        self.opt2=f"2.    {ques[r][3]}"
        self.opt3=f"3.    {ques[r][4]}"
        self.opt4=f"4.    {ques[r][5]}"
        self.talkquestion=f"\nQuestion {str(self.ques_no)}: {ques[r][1]}\nThe options are:\n first, {ques[r][2]}\n second, {ques[r][3]}\n third, {ques[r][4]}\n and fourth, {ques[r][5]}"
        self.quizcheck=""
        
        # removing the used ques for this quiz
        loopques.insert(0, ques.pop(r))

        # if self.ques_no==1:
        #     self.Quiz_Score="0"
        if self.ques_no==5:
            self.ques_no=0
            buttonnext.bind(on_release=self.gotoresult)
            # buttonnext.bind(on_state=self.resultbutton,on_release=self.gotoresult)
        # if self.ques_no==4:
        #     buttonnext.disabled = False
        #     self.ids.imagenextquiz.source = "images/buttons/resultdark.png"
        
        self.ids.btnquiznextques.disabled=True
    
    # def resultbutton(self):
    #     if self.ids.btnquiznextques.state == "down":
    #         self.ids.imagenextquiz.source = "images/buttons/resultlight.png"
    #     else:
    #         self.ids.imagenextquiz.source = "images/buttons/resultdark.png"

    def gotoresult(self, quiznextparent):
        self.parent.current = "quizresult"
        self.ids.btnquiznextques.unbind(on_release=self.gotoresult)

    def inputA(self, button):
        if self.ans1==self.answer:
            self.ans="true"
        else:
            self.ans="false"
        
        self.ids.btnopt2.state='normal'
        self.ids.btnopt3.state='normal'
        self.ids.btnopt4.state='normal'
        self.ids.imageopt2.source="images/buttons/optiondark.png"
        self.ids.imageopt3.source="images/buttons/optiondark.png"
        self.ids.imageopt4.source="images/buttons/optiondark.png"
    
    def inputB(self, button):
        if self.ans2==self.answer:
            self.ans="true"
        else:
            self.ans="false"
        
        self.ids.btnopt1.state='normal'
        self.ids.btnopt3.state='normal'
        self.ids.btnopt4.state='normal'
        self.ids.imageopt1.source="images/buttons/optiondark.png"
        self.ids.imageopt3.source="images/buttons/optiondark.png"
        self.ids.imageopt4.source="images/buttons/optiondark.png"

    def inputC(self, button):
        if self.ans3==self.answer:
            self.ans="true"
        else:
            self.ans="false"
        
        self.ids.btnopt1.state='normal'
        self.ids.btnopt2.state='normal'
        self.ids.btnopt4.state='normal'
        self.ids.imageopt1.source="images/buttons/optiondark.png"
        self.ids.imageopt2.source="images/buttons/optiondark.png"
        self.ids.imageopt4.source="images/buttons/optiondark.png"
            
    def inputD(self, button):
        if self.ans4==self.answer:
            self.ans="true"
        else:
            self.ans="false"
        
        self.ids.btnopt1.state='normal'
        self.ids.btnopt2.state='normal'
        self.ids.btnopt3.state='normal'
        self.ids.imageopt1.source="images/buttons/optiondark.png"
        self.ids.imageopt2.source="images/buttons/optiondark.png"
        self.ids.imageopt3.source="images/buttons/optiondark.png"

    def check_quiz_ans(self):

        if self.ans=="true":
            Quiz.SCORE += 1
            self.Quiz_Score = str(int(self.Quiz_Score) + 1)
            self.quizcheck="Your Answer is Correct!!"
        else:
            self.quizcheck=f"Your Answer is Wrong, The Correct Answer To This Ques is {self.answer}."
        
        self.ids.btnquizcheck.disabled=True
        self.ids.btnopt1.disabled=True
        self.ids.btnopt2.disabled=True
        self.ids.btnopt3.disabled=True
        self.ids.btnopt4.disabled=True

        self.ids.btnquiznextques.disabled=False

    def exitquiz(self):
        self.ids.btnquiznextques.disabled=True
        
        self.ids.btnquizcheck.disabled=False
        self.ids.btnopt1.disabled=False
        self.ids.btnopt2.disabled=False
        self.ids.btnopt3.disabled=False
        self.ids.btnopt4.disabled=False
        self.quizcheck=""

        self.ques_no=1
        self.Quiz_Score = "0"
        self.question_number=f"{self.ques_no}"

class RapidFire(Screen, object):
    #stt func to get input from the user's mic
    # def listen():
    #     rec = sr.Recognizer()

    #     with sr.Microphone() as source:
    #         rec.adjust_for_ambient_noise(source, duration=3)
    #         print("Listening . . ")
    #         audio = rec.listen(source)

    #     data = " "

    #     try:
    #         data = rec.recognize_google(audio,language='en')
    #         print("You said " + data)

    #     except sr.UnknownValueError:
    #         print("Sorry, could not understand that.")
    #     except sr.RequestError as ex:
    #         print("Request Error from Google Speech Recognition" + ex)

    #     return data

    global ques
    global loopques
    global r
    
    if len(ques)==1:
        for i in range(len(loopques)):
            ques.insert(1, loopques.pop(i))

    #default vals
    Rapid_Score = StringProperty("4")
    SCORE=0
    ques_no=1

    #variables    
    A=StringProperty("0")
    rapidcheck=StringProperty("")

    ans=StringProperty("false")
    nexttohome=StringProperty("Next")
    
    r=random.randint(1,len(ques)-1)
    ans1,ans2,ans3,ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]
    question_number=StringProperty(f"{int(ques_no)}")
    question=StringProperty(f"Ques: {ques[r][1]}")
    answer=StringProperty(f"{ques[r][6]}")

    # removing the used ques for this quiz
    loopques.insert(0, ques.pop(r))

    def start_rapid_ques(self, buttonnext, buttonhome):
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
        self.question_number=f"{self.ques_no}"
        self.question=f"Ques: {ques[r][1]}"
        self.answer=ques[r][6]
        
        # removing the used ques for this quiz
        loopques.insert(0, ques.pop(r))

        self.ids.inprapidans.text="Enter Your Answer Here"
        if self.ques_no==1:
            # self.SCORE=0
            self.Rapid_Score="0"
        if self.ques_no==5:
            self.ques_no=1
            buttonnext.text="Result"  #change to Result button image here
            buttonnext.bind(on_release=self.gotoresult)

        self.ids.btnrapidnextques.disabled=True
        self.ids.btnrapidcheck.disabled=False

    def gotoresult(self, quiznextparent):
        self.parent.current = "rapidresult"
        self.ids.btnrapidnextques.text="Next"
        self.ids.btnrapidnextques.unbind(on_release=self.gotoresult)

    def check_rapid_ans(self, buttonnext):
        self.A=self.ids.inprapidans.text
        if (self.A == self.answer) :#or (self.A in ques[r][6]):
            # RapidFire.SCORE+=1
            self.Rapid_Score = str(int(self.Rapid_Score) + 1)
            self.ans="true"
            self.rapidcheck="Your Answer is Correct!!"
        else:
            self.ans="false"
            self.rapidcheck=f"Your Answer is Wrong, The Correct Answer To This Ques is {self.answer}."
        
        self.ids.btnrapidnextques.disabled=False
        self.ids.btnrapidcheck.disabled=True
        
        # def __init__(self):
        #     if RapidFire.ans == "true":
        #         RapidFire.SCORE+=1

    def exitrapid(self):
        self.ids.btnrapidnextques.disabled=True
        
        self.ids.btnrapidcheck.disabled=False
        self.rapidcheck=""
        self.ids.inprapidans.text="Enter Your Answer Here"

        self.ques_no=1
        self.Rapid_Score = "0"
        self.question_number = f"{int(self.ques_no)}"

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

class QuizResult(Quiz, Screen):
    # if __name__=="__main__":
    #     Quiz.SCORE=int(str(Quiz.Quiz_Score))
    
    # quizclass=Quiz()
    # print(quizclass.SCORE)

    
    finalquizscore=StringProperty(f"{Quiz.SCORE}")

class RapidResult(RapidFire, Screen):
    finalrapidscore=StringProperty(f"{RapidFire.SCORE}")
    
    # def result(self):
    #     # self.finalrapidscore = RapidFire.SCORE
    #     return RapidFire.SCORE

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



class CTFApp(App):
    
    
    global WindowWidth
    global WindowHeight
    windowwidth= StringProperty(str(int(dp(WindowWidth))))
    windowheight = StringProperty(str(int(dp(WindowHeight))))
    
    def build(self):
        kvfile = Builder.load_file("mymain.kv")
        self.title="CTF - Cosmos Trivia and Facts"
        self.icon="images/appicon.ico"
        return kvfile
    
    #tts func to make our program say something
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty("voices", voices[0].id)
    engine.setProperty("rate", 178)
    
    def talk(self,audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    appversion=StringProperty(f"{__version__}")

if __name__ == "__main__":
    CTFApp().run()
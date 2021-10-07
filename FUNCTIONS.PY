# this is where all the funcs needed for main.py will be

import csv
from os import extsep
import random
import pyttsx3
import speech_recognition as sr
import time
from threading import Timer

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voices", voices[0].id)
engine.setProperty("rate", 178)

# Files Needed To Be Read

ques_file=open("questions.csv")
read_ques_file=csv.reader(ques_file)
ques=[]         # 1-Q, 2-O1, 3-O2, 4-O3, 5-O4, 6-A
for x in read_ques_file:
    ques.append(x)

looplist=[]

print("\n\nCOSMOS TRIVIA AND FACTS") #intro
print("\n WELCOME TO CTF! CHOOSE THE SETTINGS BEFORE YOU START PLAYING THE GAME!")

# taking input to check if the user wants additional functionalities or not
tts = input("\n\n Do you want to use text-to-speech to read questions? (yes/no): ")
stt = input("\n\n Do you want to use microphone to answer questions? (yes/no): ")

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

def quiz():      # Function To Start Another Quiz
    print("Do you want to start the quiz? (Yes/No): ")           # Ask If Want To Take One More Quiz Or Not
        
    if "yes" in tts.lower():
        talk("Do you want to start the quiz? (Yes or No)")
    else:
        pass
        
    if "yes" in stt.lower():
        inp = listen().upper()
    else:
        inp=input().upper()

    if "Y" in inp or "YES" in inp:
        for ques_no in range(1,6):      # Number Of Questions To Be Asked In Each Quiz
            r=random.randint(1,(len(ques)-1))   # Random Questions From The List (Also, Set The Range)
            ans1,ans2,ans3,ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]     # Assigning Variables To All The Options

            print(f"\nQuestion {str(ques_no)}: {ques[r][1]}\n 1. {ques[r][2]}\n 2. {ques[r][3]}\n 3. {ques[r][4]}\n 4. {ques[r][5]}")    # Displaying Question Along With Options
            if "yes" in tts.lower():
                talk(f"\nQuestion {str(ques_no)}: {ques[r][1]}\nThe options are:\n first, {ques[r][2]}\n second, {ques[r][3]}\n third, {ques[r][4]}\n and fourth, {ques[r][5]}")
            else:
                pass
                        
            check_quiz_ans(answer="",r=r,ans1=ans1,ans2=ans2,ans3=ans3,ans4=ans4,ques_no=ques_no)  # Calling Function To Check The Answer
            
            # removing the used ques for this quiz
            looplist.insert(0, ques.pop(r))

        if len(ques)==1:
            for i in range(len(looplist)):
                ques.insert(1, looplist.pop(i))
        else:
            pass
        
        if "yes" in stt.lower():
            print("Do you want to start another quiz? (Yes/No): ")
            again = listen()
        else:
            again=input("Do you want to start another quiz? (Yes/No): ").upper()
        if "Y" in again or "YES" in again:
            quiz()
        else:
            home()
    
    else:
        home()  # FOR NOW Exit

score = 0

def check_quiz_ans(answer,r,ans1,ans2,ans3,ans4,ques_no):    # Function To Take And Check The Answer
    global score
    print("\nEnter you answer (option 1, 2, 3, or 4) or enter 'stop' to exit the trivia.")
    print("Answer: ", end="")
    if "yes" in tts.lower():
        talk("Enter the correct option number ")
    else:
        pass

    if "yes" in stt.lower():
        answer=str(listen().lower())
    else:
        answer=input()

    try:
        if (("1" in answer or str(ques[r][6]).lower() in answer) and ques[r][6] in ans1) or (("2" in answer or str(ques[r][6]).lower() in answer) and ques[r][6] in ans2)\
        or (("3" in answer or str(ques[r][6]).lower() in answer) and ques[r][6] in ans3) or (("4" in answer or str(ques[r][6]).lower() in answer) and ques[r][6] in ans4):       # If Answer Wrong
            print("\nYour answer is correct!")    # If Answer Right
            score += 1
            time.sleep(1)
            print(f"\n Current Score: {score}" if ques_no<5 else f"\n Your final score is: {score}")
            if "yes" in tts.lower():
                talk("Your answer is CORRECT!")
                talk(f"\n Current Score: {score}" if ques_no<5 else f"\n Your final score is: {score}")
            else:
                pass

        elif "stop" in answer.lower():
            home()

        else:
            print(f"\nYour answer is incorrect.\nThe correct answer to this question is {ques[r][6]}.")
            time.sleep(1)
            print(f"\n Current Score: {score}" if ques_no<5 else f"\n Your final score is: {score}")
            if "yes" in tts.lower():
                talk(f"\nYour answer is incorrect.\nThe correct answer to this question is; {ques[r][6]}.")
                talk(f"\n Current Score: {score}" if ques_no<5 else f"\n Your final score is: {score}")
            else:
                pass
        if ques_no==5 and score>3:
            mesage=f"Well played!!"
            print(mesage)
            if "yes" in tts.lower():
                talk(mesage)
        if ques_no==5 and score==2:
            mesage=f"Not bad! Nice played!"
            print(mesage)
            if "yes" in tts.lower():
                talk(mesage)
        if ques_no==5 and score<2:
            mesage=f"Better luck next time!"
            print(mesage)
            if "yes" in tts.lower():
                talk(mesage)

    except:
        if (answer=="1" and ans1!=ques[r][6]) or (answer=="2" and ans2!=ques[r][6])\
        or (answer=="3" and ans3!=ques[r][6]) or (answer=="4" and ans4!=ques[r][6] or answer==" "):       # If Answer Wrong
            print(f"\nYour answer is incorrect.\nThe correct answer to this question is {ques[r][6]}.")
            print(f"\n Current Score: {score}" if ques_no<5 else f"\n Your final score is: {score}")
            if "yes" in tts.lower():
                talk(f"\nYour answer is incorrect.\nThe correct answer to this question is; {ques[r][6]}.")
                talk(f"\n Current Score: {score}" if ques_no<5 else f"\n Your final score is: {score}")
            else:
                pass
    
        elif "stop" in answer.lower():
            home()

        else:
            score += 1
            print("\nYour answer is correct!")    # If Answer Right
            print(f"\n Current Score: {score}" if ques_no<5 else f"\n Your final score is: {score}")
            if "yes" in tts.lower():
                talk("Your answer is CORRECT!")
                talk(f"\n Current Score: {score}" if ques_no<5 else f"\n Your final score is: {score}")
            else:
                pass
        if ques_no==5 and score>3:
            mesage=f"Well played!!"
            print(mesage)
            if "yes" in tts.lower():
                talk(mesage)
        if ques_no==5 and score==2:
            mesage=f"Not bad! Nice played!"
            print(mesage)
            if "yes" in tts.lower():
                talk(mesage)
        if ques_no==5 and score<2:
            mesage=f"Better luck next time!"
            print(mesage)
            if "yes" in tts.lower():
                talk(mesage)
    
rapid_fire_score = 0

def rapid_fire():
    if stt.lower() == "yes":
        print("Do you want to start a Rapid Fire Questionnaire? (Yes/No): ")
        if tts.lower() == "yes":
            talk("Do you want to start a rapid fire questionnaire?")
        else:
            pass
        inp = listen().upper()
    else:
        inp=input("Do you want to start a Rapid Fire Questionnaire? (Yes/No): ").upper()
    if inp=="Y" or inp=="YES":
        for ques_no in range(1,6):      # Number Of Questions To Be Asked In Each Quiz
            r=random.randint(1,len(ques)-1)   # Random Questions From The List (Also, Set The Range)
    
            quess=f"\nQuestion {str(ques_no)}: {ques[r][1]}"       # Displaying Question Along With Options
            print(quess)
            if tts.lower() == "yes":
                talk(quess)
            else:
                pass
            
            check_rapid_ans(answer="",r=r)  # Calling Function To Check The Answer
    else:
        home()  

def check_rapid_ans(answer,r):
    t = 10
    global rapid_fire_score
    if stt.lower() == "yes":
        print("Answer: ")
        answer = listen().upper()
    else:
        from pytimedinput import timedInput
    
        userText, timedOut = timedInput("Answer: ",10)

        if(timedOut):
            print("Time up!")
            answer = userText
        else:
            answer = userText


    if str(ques[r][6]).upper() in answer:
        rapid_fire_score += 1
        print("\nYour answer is correct!")    # If Answer Right
        print(f"\nCurrent Score : {rapid_fire_score}")
        if tts.lower() == "yes":
            talk("Your answer is correct!")
            talk(f"\nCurrent Score : {rapid_fire_score}")
        else:
            pass
    else:
        result = f"\nYour answer is incorrect.\nThe correct answer to this question is {ques[r][6]}." # If Answer Wrong
        print(result)
        print(f"\nCurrent Score : {rapid_fire_score}")
        if tts.lower() == "yes":
            talk(result)
            talk(f"\nCurrent Score : {rapid_fire_score}")
        else:
            pass
# ANSHUMAN'S FUNCTIONS

def facts():                         #Defining facts function
    with open("facts.txt") as fact_file:
        facts=fact_file.readlines()
        
        lis = ["Quite Amazing isn't it?","WOW!","Wow that's so cool!","Woah!","Haha nice","I love this one","This is actually crazy!"]
        fact = random.choice(facts)
        print("Did you know? " + fact + ".")
        if tts.lower() == "yes":
            talk("Did you know? " + fact)
        else:
            pass
        var = random.choice(lis)
        if tts.lower() == "yes":
            talk(var)
        else:
            pass
        print(var)


def space_facts():
    while True:
        if "yes" in tts.lower():
            talk("Press enter to load your space fact or type anything to exit")
        else:
            pass
        answer = input("Press enter to load your space fact or type anything to exit: ")

        if answer == "":
            facts()
        else:
            home()

def pl_fax():                         #Defining func
    inpt=input("Would you like to know info about specific solar system bodies? (y/n) : ").lower()               #Asking user would they like to know facts about a specific planet
    if "y" in inpt:
        
        print("--Our solar system's celestial bodies list is below (from closest to farthest from the centre)--\n0. Sun\n1. Mercury\n2. Venus\n3. Earth\n4. Moon\n5. Mars\n6. Jupiter\n7. Saturn\n8. Uranus\n9. Neptune ")
        inx=int(input("Select the corresponding serial no. of celestial body's info you would you like to know : "))  #asking user to select a body
        with open("space.txt","r") as f:

            lines = [inx]
            for spfax, line in enumerate(f):
                if spfax in lines:
                    lncount=0
                    decor=len(line)
                    print("-"*decor)
                    print(line)
                    print("-"*decor)

    elif "n" in inpt:                                                                                            #if denied
        print("Hope you try it later :)")                             
        exit()
    else:                                                                                                      #if input invalid
        print("Your input is invalid, try again :)")
        exit()
   
def home():
    print("\n Welcome to the home page! Choose a game mode to start with!")
    if "yes" in tts.lower():
        talk("Welcome to the home page! Choose a game mode to start with!")
    else:
        pass
    print("\n SPACE QUIZ \n RAPID FIRE \n SPACE FACTS \n\n EXIT")
    if "yes" in tts.lower():
        talk("Type in a game mode you want to play!")
    else:
        pass

    if "yes" in stt.lower():
        game_mode = listen()
    else:
        game_mode = input("Type in the game mode you want to play!: ")

    if "space quiz" in game_mode.lower():
        quiz()
    elif "rapid fire" in game_mode.lower():
        rapid_fire()
    elif "space facts" in game_mode.lower():
        space_facts()
    elif "exit" in game_mode.lower():
        exit()
    else:
        print("Please enter a valid game mode!")
        if "yes" in tts.lower():
            talk("Please enter a valid game mode!")
            
        else:
            pass
        exit()

home()
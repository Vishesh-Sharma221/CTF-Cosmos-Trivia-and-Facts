# this is where all the funcs needed for main.py will be

import csv
from os import extsep
import random
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
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
        
    if tts.lower() == "yes":
        talk("Do you want to start the quiz? (Yes or No)")
    else:
        pass
        
    if stt.lower() == "yes":
        inp = listen().upper()
    else:
        inp=input().upper()

    if inp=="Y" or inp=="YES":
        for ques_no in range(1,6):      # Number Of Questions To Be Asked In Each Quiz
            r=random.randint(1,(len(ques)-1))   # Random Questions From The List (Also, Set The Range)
            ans1,ans2,ans3,ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]     # Assigning Variables To All The Options

            print(f"\nQuestion {str(ques_no)}: {ques[r][1]}\n 1. {ques[r][2]}\n 2. {ques[r][3]}\n 3. {ques[r][4]}\n 4. {ques[r][5]}")    # Displaying Question Along With Options
            if tts.lower == "yes":
                talk(f"\nQuestion {str(ques_no)}: {ques[r][1]}\nThe options are:\n first, {ques[r][2]}\n second, {ques[r][3]}\n third, {ques[r][4]}\n and fourth, {ques[r][5]}")
            else:
                pass
                        
            check_quiz_ans(answer="",r=r,ans1=ans1,ans2=ans2,ans3=ans3,ans4=ans4)  # Calling Function To Check The Answer
            
            # removing the used ques for this quiz
            looplist.insert(0, ques.pop(r))

        if len(ques)==1:
            for i in range(len(looplist)):
                ques.insert(1, looplist.pop(i))
        else:
            pass
        
        if stt.lower() == "yes":
            print("Do you want to start another quiz? (Yes/No): ")
            again = listen()
        else:
            again=input("Do you want to start another quiz? (Yes/No): ").upper()
        if again=="Y" or again=="YES":
            quiz()
        else:
            home()
    
    else:
        home()  # FOR NOW Exit



def check_quiz_ans(answer,r,ans1,ans2,ans3,ans4):    # Function To Take And Check The Answer
    print("\nEnter you answer (option 1, 2, 3, or 4) or enter 'stop' to exit the trivia: ")
    if tts.lower == "yes":
        talk("Enter the correct option number ")
    else:
        pass

    if stt.lower()=="yes":
        answer=str(listen().lower())
    else:
        answer=input()

    try:
        if ((answer=="1" or answer==str(ques[r][6]).lower()) and ans1==ques[r][6]) or ((answer=="2" or answer==str(ques[r][6]).lower()) and ans2==ques[r][6])\
        or ((answer=="3" or answer==str(ques[r][6]).lower()) and ans3==ques[r][6]) or ((answer=="4" or answer==str(ques[r][6]).lower()) and ans4==ques[r][6]):       # If Answer Wrong
            print("\nYour answer is correct!")    # If Answer Right
            if tts.lower == "yes":
                talk("Your answer is CORRECT!")
            else:
                pass

        elif answer.lower() == "stop":
            home()

        else:
            print(f"\nYour answer is incorrect.\nThe correct answer to this question is {ques[r][6]}.")
            if tts.lower == "yes":
                talk(f"\nYour answer is incorrect.\nThe correct answer to this question is; {ques[r][6]}.")
            else:
                pass
        
    except:
        if (answer=="1" and ans1!=ques[r][6]) or (answer=="2" and ans2!=ques[r][6])\
        or (answer=="3" and ans3!=ques[r][6]) or (answer=="4" and ans4!=ques[r][6] or answer==" "):       # If Answer Wrong
            print(f"\nYour answer is incorrect.\nThe correct answer to this question is {ques[r][6]}.")
            if tts.lower == "yes":
                talk(f"\nYour answer is incorrect.\nThe correct answer to this question is; {ques[r][6]}.")
            else:
                pass
    
        elif answer.lower() == "stop":
            home()

        else:
            print("\nYour answer is correct!")    # If Answer Right
            if tts.lower == "yes":
                talk("Your answer is CORRECT!")
            else:
                pass
    
def rapid_fire():
    if tts.lower == "yes":
        talk("Do you want to start a rapid fire questionare?")
    else:
        pass

    if stt.lower() == "yes":
        print("Do you want to start a Rapid Fire Questionnaire? (Yes/No): ")
        inp = listen().upper()
    else:
        inp=input("Do you want to start a Rapid Fire Questionnaire? (Yes/No): ").upper()

    if inp=="Y" or inp=="YES":
        for ques_no in range(1,6):      # Number Of Questions To Be Asked In Each Quiz
            r=random.randint(1,(len(ques)-1))   # Random Questions From The List (Also, Set The Range)
    
            ans1,ans2,ans3,ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]     # Assigning Variables To All The Options
    
            quess=f"\nQuestion {str(ques_no)}: {ques[r][1]}"       # Displaying Question Along With Options
            print(quess)
            if tts.lower == "yes":
                talk(quess)
            else:
                pass
    
            check_rapid_ans(answer="",r=r,ans1=ans1,ans2=ans2,ans3=ans3,ans4=ans4)  # Calling Function To Check The Answer
    else:
        home()  

def check_rapid_ans(answer,r):
    if stt.lower == "yes":
        print("Answer: ")
        answer = listen().upper()
    else:
        answer = input("Answer: ").upper()


    if answer!=str(ques[r][6]).upper():
        result = f"\nYour answer is incorrect.\nThe correct answer to this question is {ques[r][6]}." # If Answer Wrong
        print(result)
        if tts.lower == "yes":
            talk(result)
        else:
            pass
    else:
        print("\nYour answer is correct!")    # If Answer Right
        if tts.lower == "yes":
            talk("Your answer is correct!")
        else:
            pass

# ANSHUMAN'S FUNCTIONS

def facts():                         #Defining facts function
    with open("facts.txt") as fact_file:
        facts=fact_file.readlines()
        
        lis = ["Quite Amazing isn't it?","WOW!","Wow that's so cool!","Woah!","Haha nice","I love this one","This is actually crazy!"]
        fact = random.choice(facts)
        print("Did you know? " + fact + ".")
        if tts.lower == "yes":
            talk("Did you know? " + fact)
        else:
            pass
        var = random.choice(lis)
        if tts.lower == "yes":
            talk(var)
        else:
            pass
        print(var)


def space_facts():
    while True:
        if tts.lower == "yes":
            talk("Press enter to load your space fact or type anything to exit")
        else:
            pass
        answer = input("Press enter to load your space fact or type anything to exit: ")

        if answer == "":
            facts()
        else:
            home()

dct1={'1':'Mercury : Mercury is the smallest and nearest planet to the sun',    #making dict for planet's data
'2':'Venus : Venus is the second closest planet to the sun',
'3':'Earth : Earth is the only habitable planet in our solar system',
'4':'Mars : Mars is the fourth closest planet to the sun',
'5':'Jupiter : Jupiter  is the fifth closest planet to the sun ',
'6':'Saturn : Saturn  is the sixth closest planet to the sun',
'7':'Uranus : Uranus is the seventh closest planet to the sun',
'8':'Neptune : Neptune  is the eighth closest planet to the sun'}

def pl_fax():                         #Defining func
    inpt=input("Would you like to know detailed info about specific planets? (y/n) : ").lower()               #Asking user would they like to know facts about a specific planet
    if inpt=="y":

        print("--Our solar system's planet's list is below (from closest to farthest from the Sun)--\n1. Mercury\n2. Venus\n3. Earth\n4. Mars\n5. Jupiter\n6. Saturn\n7. Uranus\n8. Neptune")
        inx=input("Select the corresponding serial no. of which planet's info you would you like to know : ")  #asking user to select a planet
        print(dct1[inx])
         
    elif inpt=="n":
        print("Hope you try it later :)")                             
        exit()
    else:                                                                                                      #if input invalid
        print("Your input is invalid, try again :)")
        exit()
   
def home():
    print("\n Welcome to the home page! Choose a game mode to start with!")
    if tts.lower == "yes":
        talk("Welcome to the home page! Choose a game mode to start with!")
    else:
        pass
    print("\n SPACE QUIZ \n RAPID FIRE \n SPACE FACTS")
    if tts.lower == "yes":
        talk("Type in a game mode you want to play!")
    else:
        pass

    if stt.lower() == "yes":
        game_mode = listen()
    else:
        game_mode = input("Type in the game mode you want to play!: ")

    if game_mode.lower() == "space quiz":
        quiz()
    elif game_mode.lower() == "rapid fire":
        rapid_fire()
    elif game_mode.lower() == "space facts":
        space_facts()
    else:
        print("Please enter a valid game mode!")
        if tts.lower == "yes":
            talk("Please enter a valid game mode!")
            
        else:
            pass
        exit()

home()
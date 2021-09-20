import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty

kv = Builder.load_file("mymain.kv")

class Home(Screen):
    pass
class GameMode(Screen):
    pass
class Quiz(Screen):
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
                            
                check_quiz_ans(answer="",r=r,ans1=ans1,ans2=ans2,ans3=ans3,ans4=ans4)  # Calling Function To Check The Answer
                
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

    def check_quiz_ans(answer,r,ans1,ans2,ans3,ans4):    # Function To Take And Check The Answer
        
        global score
        print("\nEnter you answer (option 1, 2, 3, or 4) or enter 'stop' to exit the trivia: ")
        

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
                print("\n Current Score: ", score)
                if "yes" in tts.lower():
                    talk("Your answer is CORRECT!")
                    talk(f"\n Current Score: {score}")
                else:
                    pass

            elif "stop" in answer.lower():
                home()

            else:
                print(f"\nYour answer is incorrect.\nThe correct answer to this question is {ques[r][6]}.")
                time.sleep(1)
                print("\n Current Score: ", score)
                if "yes" in tts.lower():
                    talk(f"\nYour answer is incorrect.\nThe correct answer to this question is; {ques[r][6]}.")
                    talk(f"\n Current Score: {score}")
                else:
                    pass
            
        except:
            if (answer=="1" and ans1!=ques[r][6]) or (answer=="2" and ans2!=ques[r][6])\
            or (answer=="3" and ans3!=ques[r][6]) or (answer=="4" and ans4!=ques[r][6] or answer==" "):       # If Answer Wrong
                print(f"\nYour answer is incorrect.\nThe correct answer to this question is {ques[r][6]}.")
                print("\n Current Score: ", score)
                if "yes" in tts.lower():
                    talk(f"\nYour answer is incorrect.\nThe correct answer to this question is; {ques[r][6]}.")
                    talk(f"\n Current Score: {score}")
                else:
                    pass
        
            elif "stop" in answer.lower():
                home()

            else:
                score += 1
                print("\nYour answer is correct!")    # If Answer Right
                print("\n Current Score: ", score)
                if "yes" in tts.lower():
                    talk("Your answer is CORRECT!")
                    talk("\n Current Score: ", score)
                else:
                    pass
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

class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()
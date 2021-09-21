import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.clock import Clock
import random
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.core.window import Window

Window.size=(600,500)
kv = Builder.load_file("mymain.kv")

class Home(Screen):
    pass
class GameMode(Screen):
    pass
class Quiz(Screen):
    o=1
    global ok
    ok=f"nice th{o}s worked"

    textin=StringProperty(f"{ok}")

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
    title="Space"
    icon="black-hole-icon.ico"
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()
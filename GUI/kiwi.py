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
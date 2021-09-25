from typing import Text
import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class TheGrid(GridLayout):
    def __init__(self, **kwargs):
        super(TheGrid, self).__init__(**kwargs)
        self.cols = 2



class AppGui(App):
    def build(self):
        return TheGrid()

if __name__=="__main__":
    AppGui().run()
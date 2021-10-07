import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

class TestClass(Widget):
    #all functions goes in this class
    pass

class TestApp(App):
    def build(self):
        return(Builder.load_file("my.kv"))

if __name__=="__main__":
    TestApp().run()
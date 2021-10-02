import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scatter import Scatter
from kivy.graphics import Rectangle, Color
from kivy.uix.widget import Widget


class canvaswidget(Widget):
    def __init__(self, **kwargs):
        super(canvaswidget, self).__init__(**kwargs)
        with self.canvas:
            Color(.52,.52,.52)
            self.rect=Rectangle(pos=self.pos, source="images/infobutton.png")

    

class MyApp(App):
    def build(self):
        b=BoxLayout(orientation="vertical")
        t=TextInput(font_size=150, 
                    size_hint_y=None,
                    height=200)
        l=Label(text="nice", 
                font_size=150,
                pos=(200,10),
                font_name="fonts/righteous.ttf")
        file=open("C:\\Users\\yugam\\Documents\\Yugam4254\\ATL\\Test\\textfiles\\info.txt")
        # file=open("\textfiles\info.txt")
        lines=file.readlines()
    
        l2=Label(text=lines[3])
        f=FloatLayout()
        s=Scatter(pos= (200,200))

        t.bind(text=l2.setter("text"))

        f.add_widget(s)
        s.add_widget(canvaswidget())
        s.add_widget(l2)

        b.add_widget(t)
        b.add_widget(f)

        return b

if __name__=="__main__":
    MyApp().run()
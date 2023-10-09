from kivy.app import App
from kivy.uix.label import Label

class HelloWorldApp(App):
    def build(self):
        return Label(text="Oi Mundo. Bem vindo ao Kivy")
    
HelloWorldApp().run()
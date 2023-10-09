from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Tela(BoxLayout):
    pass

class IntroducaoApp(App):
    def build(self):
        return Tela()

meu_app = IntroducaoApp()

meu_app.run()
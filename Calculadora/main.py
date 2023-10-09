from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class Tela(BoxLayout):
    def calcular(self, op, v1, v2):

        if op == '+':
            result = int(v1) + int(v2)
        elif op == '-':
            result = int(v1) - int(v2)
        elif op == 'x':
            result = int(v1) * int(v2)
        elif op == '÷':
            result = int(v1) / int(v2)

        self.ids.resp.text = str(result)

class CalculadoraApp(App):
    def build(self):
        Window.size = (300, 400)
        self.title = "Calculadora"
        return Tela()
    
CalculadoraApp().run()
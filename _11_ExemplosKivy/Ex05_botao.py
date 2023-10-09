#-- coding: latin-1 --
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
# Classe definindo o layout do aplicativo (no respectivo arquivo .kv).
class Quadro(BoxLayout):
    def botao_msg(self): 
        # Para que o negrito funcione, tem que por markup=True no .kv.
        # '\' permite que o comando continue na próxima linha.
        self.ids.msg.text= \
        '[b][color=#DAA520]O botao funcionou!! Parabens!![/color][/b]'
# Classe da app.
class BotaoApp(App):
    def build(self):
        return Quadro()
# Cria o objeto App e o ativa.
bot = BotaoApp()
bot.run()
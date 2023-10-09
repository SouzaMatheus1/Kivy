#-- coding: latin-1 --
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
# Classe definindo o layout do aplicativo (no respectivo arquivo .kv).
class Quadro(BoxLayout):
    def uneNomes(self):
        # Entrada de dados.
        nome  = self.ids.nome1.text
        sobre = self.ids.sobr1.text
        # Une o 'Ola' com o nome e com o sobrenome fornecidos.
        resp = 'Ola '+nome+' '+sobre
        # Saida.
        self.ids.resultado.text = resp

# Subclasse que define o aplicativo e que herda as 
# caracteristicas do App do Kivy.
class textinputApp(App):
    def build(self):
        # Chama a classe Quadro que esta definida no arquivo 
        # .kv e representa a tela do aplicativo com todos os 
        # respectivos elementos graficos.
        return Quadro()  

# Cria o objeto App e o ativa.
nomes = textinputApp()
nomes.run()

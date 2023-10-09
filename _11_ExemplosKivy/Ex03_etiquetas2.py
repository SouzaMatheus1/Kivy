#-- coding: latin-1 --
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
# Classe definindo o layout do aplicativo (no respectivo arquivo .kv).
class Quadro(BoxLayout):
   # Metodo construtor: obrigatorio com **kwargs devido 
   # a superclasse BoxLayout.
   def __init__(self,**kwargs):   
      # Chama o construtor da superclasse BoxLayout.
      super().__init__(**kwargs)  
      # Define o tamanho da janela do aplicativo.
      Window.size = (400, 100) 
class etiquetas2App(App): # O arquivo .kv deve ter nome Oi.kv.
   def build(self):
      return Quadro()
# Cria o objeto App e o ativa.
e1=etiquetas2App()
e1.run()
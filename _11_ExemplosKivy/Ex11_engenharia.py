#-- coding: latin-1 --
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
class CampoAtuacaoEngenharia:
    def __init__(self):
        self.opcoes = ['','']
    def armazenaOpcoes(self,posicao,escolha):
        self.opcoes[posicao] = escolha
# Classe definindo o layout do aplicativo (no respectivo arquivo .kv).
class Quadro(BoxLayout):
    def __init__(self, **kwargs):    
        super().__init__(**kwargs)
        # Define o tamanho da tela.
        Window.size = (700,300)
    def selAtuacao(self,campo):
        # Quarda na lista a opcao de botao.
        minhaEscolha.armazenaOpcoes(1, campo)  
    def geraResultado(self):
        curso = self.ids.nomeP.text
        # Guarda na lista o conteudo do TextInput.
        minhaEscolha.armazenaOpcoes(0,curso) 
        final="Estou cursando atualmente Engenharia {} na PUCPR" \
              " e seu principal \nramo de atuacao ocorre na(o) {}." \
              .format(minhaEscolha.opcoes[0],minhaEscolha.opcoes[1])
        self.ids.resultado.text = final
    def sair(self):
        App.get_running_app().stop()
        
class engenhariaApp(App): # arquivo .kv tem nome Exemplo.kv
    def build(self):
        self.title= 'Exemplo Usando Botoes....'
        return Quadro()

minhaEscolha = CampoAtuacaoEngenharia()
meuApp = engenhariaApp()
meuApp.run()
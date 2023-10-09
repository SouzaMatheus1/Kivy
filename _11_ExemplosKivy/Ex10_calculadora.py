#-- coding: latin-1 --
from kivy.app           import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window   import Window
# Classe definindo o layout do aplicativo (no respectivo arquivo .kv).
class Quadro(BoxLayout):  
    # Metodo construtor obrigatorio com **kwargs devido a superclasse BoxLayout
    def __init__(self,**kwargs):    
        super().__init__(**kwargs)  # Chama o construtor da superclasse BoxLayout.
        Window.size = (400, 300)    # Define o tamanho da janela do aplicativo.
        self.limpar()  # chama o metodo limpar() para iniciar os componentes da calculadora.
    # Metodo executado quando o botao CE for pressionado.
    def limpar(self): 
        self.ids.mensagem.text  = ' '
        self.ids.op1.text       = ' ' 
        self.ids.op2.text       = ' '
        self.ids.resultado.text = ' '
    # Metodo executado quando o botao OFF for pressionado.
    def sair(self):           
        App.get_running_app().stop()    

    # Explicação sobre try/except.
    # Serve para tratamento de execeções ("erros"). Se ocorre um erro,
    # a execucao do bloco de comandos pertencentes ao "try" dá uma parada
    # e a execucao é transferida para o bloco except abaixo, no qual a
    # exceção é tratada.
    # Metodo executado quando o botao + for pressionado.
    def somar(self): 
        try: # Testa se deu erro na conversao para  float.
            o1 = float(self.ids.op1.text)
            o2 = float(self.ids.op2.text)
            # Converte o string retornado para float (porque tudo eh string no kv)
            self.ids.resultado.text = str(o1+o2)  
        except:     
            # Captura (trata) o erro do try (se houver) e apresenta uma mensagem 
            # de erro em vermelho (valor em Hexadecimal => #FF0000).
            self.ids.mensagem.text = \
            '[color=#FF0000] Favor fornecer os operandos corretamente!![/color]'
    # Metodo executado quando o botao - for pressionado
    def subtrair(self):      
        try:       
            o1 = float(self.ids.op1.text)
            o2 = float(self.ids.op2.text)
            self.ids.resultado.text = str(o1-o2) 
        except:     
            self.ids.mensagem.text = \
            '[color=#FF0000] Favor fornecer os operandos corretamente!![/color]'
    # Metodo executado quando o botao x for pressionado.
    def multiplicar(self):    
        try:
            o1 = float(self.ids.op1.text)
            o2 = float(self.ids.op2.text)
            self.ids.resultado.text = str(o1*o2)   
        except:    
            self.ids.mensagem.text = \
             '[color=#FF0000] Favor fornecer os operandos corretamente!![/color]'
    # Metodo executado quando o botao / for pressionado.
    def dividir(self):  
        try:   
            o1 = float(self.ids.op1.text)
            o2 = float(self.ids.op2.text)
            if o2 == 0:
                self.ids.mensagem.text = '[color=#FF0000] ERRO: Divisao por 0![/color]'
            else:
                self.ids.resultado.text = str(round(o1/o2,2))   
        except:    
            self.ids.mensagem.text = \
            '[color=#FF0000] Favor fornecer os operandos corretamente!![/color]'
class CalculadoraApp(App): # Arquivo .kv deve ter nome calculadora.kv

    def build(self):
        self.title = 'Calculadora 1.0'
        return Quadro()
# Cria o objeto App e o ativa.
meuApp = CalculadoraApp()
meuApp.run()



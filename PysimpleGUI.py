import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #Layout
        layout = [
       [sg.Text("Cadastre-se",size=(15,0))],
       [sg.Text("Nome",size=(10,0))],
       [sg.Input(size=(20,0))],
       [sg.Text("E-mail \ Login",size=(20,0))],
       [sg.Input(size=(20,0))],
       [sg.Text("Senha",size=(10,0))],
       [sg.Input(size=(20,0))],
       [sg.Button("Enviar",size=(7,0))]
        ]
        #Janela
        janela = sg.Window("Dados do usuario").layout(layout)

        #Extrair os dados da tela
        self.button, self.values = janela.Read() 

    def Iniciar(self):
        print(self.values)

tela = TelaPython()
tela.Iniciar()


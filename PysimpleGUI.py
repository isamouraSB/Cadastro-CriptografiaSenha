import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #Layout
        layout = [
           [sg.Text("Cadastre-se",size=(15,0))],
           [sg.Text("E-mail \ Login",size=(20,0))],
           [sg.Input(size=(20,0),key="login")],
           [sg.Text("Nome",size=(10,0))],
           [sg.Input(size=(20,0),key="nome")],
           [sg.Text("Gênero",size=(10,0))],
           [sg.Checkbox("F",key="feminino"),sg.Checkbox("M",key="masculino"),sg.Checkbox("Prefiro não dizer",key="nulo")],
           [sg.Text("Senha",size=(10,0))],
           [sg.Input(size=(20,0),key="senha")],
           [sg.Button("Enviar",size=(7,0))]
        ]
        #Janela
        self.janela = sg.Window("Dados do usuario").layout(layout)
        
        

    def Iniciar(self):
        while True:
            #Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            login = self.values["login"]
            nome = self.values["nome"]
            genero_F = self.values["feminino"]
            genero_M = self.values["masculino"]
            genero_nulo = self.values["nulo"]
            senha = self.values["senha"]
            print(f"login: {login}")
            print(f"nome: {nome}")
            print(f"genero_F: {genero_F}")
            print(f"genero_M: {genero_M}")
            print(f"genero_nulo: {genero_nulo}")
            print(f"senha: {senha}") 
        



tela = TelaPython()
tela.Iniciar()


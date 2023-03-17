#cadastro usuario:
import PySimpleGUI as sg

from codificação import codificar
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
           [sg.Input(size=(20,0),key='senha', password_char='*')],
           [sg.Checkbox('Salvar Login?')],
           [sg.Button("Enviar",size=(7,0))]
           
        ]
        #Janela
        self.janela = sg.Window("Dados do usuario").layout(layout)

    def codificar(input): 
        chave = input 

        senha = "" 
        for letra in chave:
            if letra in "Aa": senha = senha + "!"
            elif letra in "Bb": senha = senha + "&"
            elif letra in "Cc": senha = senha + "3"
            elif letra in "Dd": senha = senha + "¢"
            elif letra in "Ee": senha = senha + "?"
            elif letra in "Ff": senha = senha + "1"
            elif letra in "Ii": senha = senha + "&"
            elif letra in "Mm": senha = senha + "%"
            elif letra in "Rr": senha = senha + "@"
            elif letra in "Ss": senha = senha + "7"
            elif letra in "Uu": senha = senha + "5"
            else: senha = senha + letra
        return senha


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

            codificado = codificar(senha)

            print(f"senha: {codificado}") 


    



tela = TelaPython()
tela.Iniciar()


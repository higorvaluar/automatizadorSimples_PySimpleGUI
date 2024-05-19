import PySimpleGUI as sg

sg.theme('reddit') # Você escolhe qual tema será utilizado

janela_principal = [ # janela_principal é o layout do aplicativo, e cada lista dessa é uma linha que irá aparece na janela.
    [sg.Text("E-mail"), sg.Input(key = "email")],
    [sg.Text("Senha"), sg.Input(key = "senha", password_char = "*")], # 'password_char=' substitui o que será visto quando escrever.
    [sg.FolderBrowse("Escolha a pasta dos anexos", target = "anexos"), sg.Input(key = "anexos")],
    [sg.FolderBrowse("Escolha a pasta das planilhas", target = "planilhas"), sg.Input(key = "planilhas")],
    [sg.Button("Salvar")]
]

# É fácil entender as funções pois elas fazem basicamente o que a tradução literal fala.

window = sg.Window("Salvador de anexos e planilhas", layout = janela_principal) # 'window' é uma variável, 'sg.Window()' é o que atribui o nome para a janela, o parâmetro 'layout =' puxa o layout que será exibido na janela, que configurei acima.

while True: # Para funcionar precisamos de um loop.
    event, values = window.read() # O 'window.read' guarda e captura o próximo evento na interface gráfica, ele bloqueia a execução até um evento iniciar, ao ocorrer ele retorna uma tupla contendo as informações 'event' e 'values'.
    if event == sg.WIN_CLOSED:
        break
    elif event == "Salvar":
        email = values["email"]
        senha = values["senha"]
        anexos = values["anexos"]
        planilhas = values["planilhas"]
        print(f"O e-mail digitado foi {email}")
        print(f"A senha digitada foi {senha}") # É só um exemplo, isso não saíria para o usuário kkkkk
        print(f"O caminho dos anexos especificado foi {anexos}")
        print(f"O o caminho das planilhas especificado foi {planilhas}")
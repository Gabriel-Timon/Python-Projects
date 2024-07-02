import PySimpleGUI as pyGui
import re
from time import sleep


def validar_email(mail):
    padrao = r'^[a-zA-z0-9._%+-]+@[a-zA-Z0-9.-]+[a-zA-Z]{2,}$'
    return re.match(padrao, mail) is not None


pyGui.theme('reddit')

janela_principal = \
    [
        [pyGui.Text('E-mail')],
        [pyGui.Input(key='email')],
        [pyGui.Text('Senha')],
        [pyGui.Input(key='senha', password_char='*')],
        [pyGui.Text('Confirmar senha')],
        [pyGui.Input(key='confirmar_senha', password_char='*')],
        [pyGui.FolderBrowse('Escolher pasta anexos', target='input_anexos'), pyGui.Input(key='input_anexos')],
        [pyGui.FolderBrowse('Escolher pasta planilha', target='input_planilha'), pyGui.Input(key='input_planilha')],
        [pyGui.Button('Salvar')]
    ]

janela = pyGui.Window('Principal', layout=janela_principal)

while True:
    event, values = janela.read()
    if event == pyGui.WIN_CLOSED:
        break
    elif event == 'Salvar':
        email = values["email"]
        senha = values["senha"]
        confirmar_senha = values["confirmar_senha"]
        caminho_pasta_anexos = values["input_anexos"]
        caminho_pasta_planilha = values["input_planilha"]

        if senha != confirmar_senha:
            pyGui.popup('Erro! As senhas não coincidem, por favor, coloque a mesma senha nos dois campos',
                        text_color='red',
                        background_color='white',
                        title='SENHAS DIFERENTES',
                        no_titlebar=False,
                        keep_on_top=True)
        elif not validar_email(email):
            pyGui.popup('Erro!',
                        'E-mail inválido. Por favor coloque um e-mail válido',
                        text_color='red',
                        background_color='white',
                        title='EMAIL INCORRETO',
                        no_titlebar=False,
                        keep_on_top=True)
        else:
            # Print apenas para mostrar o que foi digitado, por vias de confirmação
            print(f'O e-mail digitado foi: {email}\n'
                  f'A senha digitada foi {senha}\n'
                  f'A confirmação da senha foi {confirmar_senha}\n'
                  f'O caminho para os anexos foi: {caminho_pasta_anexos}\n'
                  f'O caminho para as planilhas foi {caminho_pasta_planilha}')
            sleep(0.6)
            janela.close()

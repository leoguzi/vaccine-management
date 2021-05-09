import os
import PySimpleGUI as sg

class TelaPaciente:

    def __init__(self):
        self.__window = None

    def opcoes_paciente(self):
        layout = [
                [sg.Txt('Controle de pacientes. Clique na opção desejada: ', justification='center')],
                [sg.ReadButton('Cadastrar novo paciente', size = (30, 1), key = 1)],
                [sg.ReadButton('Excluir paciente', size = (30, 1), key = 2)],
                [sg.ReadButton('Editar paciente', size = (30, 1), key = 3)],
                [sg.ReadButton('Listar pacientes', size = (30, 1), key = 4)],
                [sg.ReadButton('Voltar', size = (30, 1), key = 0)]
            ]
        self.__window = sg.Window('PACIENTES', size = (400, 230), element_justification='c').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        opcao = button
        return opcao
    
    def le_dados(self, dados_atuais = None):
        if dados_atuais == None:
            layout = [
                [sg.Txt('Nome: ', justification='center'), sg.InputText(key = '-nome-')],
                [sg.Txt('Idade: ', justification='center'), sg.InputText(key = '-idade-')],
                [sg.ReadButton('Cadastrar', size = (20, 1)), sg.ReadButton('Voltar', size = (20, 1))]
            ]
        else: #preenche o campo de texto com os dados atuais em caso de edição.
            layout = [
                [sg.Txt('Nome: ', justification='center'), sg.InputText(dados_atuais['nome'], key = '-nome-')],
                [sg.Txt('Idade: ', justification='center'), sg.InputText(dados_atuais['idade'], key = '-idade-')],
                [sg.ReadButton('Cadastrar', size = (10, 1)), sg.ReadButton('Voltar', size = (10, 1))]
            ]
        self.__window = sg.Window('Cadastro de Paciente', element_justification = 'c').Layout(layout)
        button, values = self.__window.Read()
        retorno = {}
        if button == 'Cadastrar': #retorna o valor digitado ou '' se a pessoa clicar em cadastrar.
            retorno['nome'] = values['-nome-']
            retorno['idade'] = values['-idade-']
        if button == 'Voltar' or button == sg.WIN_CLOSED: #retorna none se a pessoa fechar a janela ou clicar em voltar. deve ser tratado onde essa função for utilizada.
            retorno = None
        self.__window.Close()
        return retorno
        
    def combo_box_pacientes(self, lista_pacientes): #cria um combobox com todos os pacientes cadastrados atravez de uma lista de dicionarios recebida do controlador e retorna um dicionario com o paciente selecionado. 
        if lista_pacientes is not None: #só cria a combobox se existirem pacientes
            codigos_nomes = []
            for paciente in lista_pacientes:
                codigos_nomes.append(str(paciente['codigo']) + ' - ' + str(paciente['nome']))
            layout = [
                [sg.InputCombo(codigos_nomes, key = '-codigo_nome-')],
                [sg.ReadButton('Selecionar', size = (20, 1)), sg.ReadButton('Voltar', size = (20, 1))]
            ]
            self.__window = sg.Window("Seleção de Paciente").Layout(layout)
            button, values = self.__window.Read()
            self.__window.Close()
            if button == 'Selecionar':
                if values['-codigo_nome-'] == '': #clicou em selecionar sem selecionar nenhum paciente
                    selecionado = values['-codigo_nome-']  # retorna '' (string vazia), tratar onde esta função for utilizada.
                else: 
                    selecionado = int(values['-codigo_nome-'].split(' ')[0]) #pega o código selecionado
            if button == 'Voltar' or button == sg.WIN_CLOSED: #retorna none se a pessoa fechar a janela ou clicar em voltar. deve ser tratado onde essa função for utilizada.
                selecionado = None
        else:
            selecionado = None #retorna None caso não existam pacientes cadastrados.
        return selecionado #retorna None se fechar ou voltar, '' se não selecionar nenhum e clicar em "selecionar", ou ocodigo do Paciente selecionado.

    def mostra_pacientes(self, lista_pacientes):
        if lista_pacientes is not None: #só cria a string caso existam pacientes...
            big_string = ''
            for paciente in lista_pacientes:
                big_string =  str(big_string) + '\nCódigo: ' + str(paciente['codigo']) + '\n' + 'Nome: ' + str(paciente['nome']) + '\n' + 'Idade: ' + str(paciente['idade']) + '\n--------------------------' #gambiarra mas é o que temos.
            layout = [
                [sg.Txt('Lista de pacientes cadastrados:')],
                [sg.Txt(big_string)],
                [sg.Exit('Ok', size = (20, 1))]
                ]
            self.__window = sg.Window("Lista de pacientes").Layout(layout)
            button, values = self.__window.Read()
            self.__window.Close()

    def mensagem(self, mensagem: str): #função para exibir avisos na tela.
        layout = [
            [sg.Txt(mensagem)],
            [sg.Exit('Ok', size = (20, 1))]
        ]
        self.__window = sg.Window('Aviso!', element_justification = 'c').Layout(layout)
        buttons, values = self.__window.Read()
        self.__window.Close()

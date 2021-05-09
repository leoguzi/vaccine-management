import os
import PySimpleGUI as sg


class TelaEnfermeiros:

    def __init__(self):
        self.__window = None

    def opcoes_enfermeiro(self):
        layout = [
                [sg.Txt('Controle de Enfermeiros. Clique na opção desejada: ', justification='center')],
                [sg.ReadButton('Cadastrar novo enfermeiro', size = (30, 1), key = 1)],
                [sg.ReadButton('Excluir enfermeiro', size = (30, 1), key = 2)],
                [sg.ReadButton('Editar enfermeiro', size = (30, 1), key = 3)],
                [sg.ReadButton('Listar enfermeiros', size = (30, 1), key = 4)],
                [sg.ReadButton('Voltar', size = (30, 1), key = 0)]
            ]
        self.__window = sg.Window('PACIENTES', size = (400, 230), element_justification='c').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        opcao = button
        return opcao

    def le_nome(self, nome_atual = None): #se estiver editando recebe o nome atual do enfermeiro selecionado.
        if nome_atual == None:
            layout = [
                [sg.Txt('Nome: ', justification='center'), sg.InputText(key = '-nome-')],
                [sg.ReadButton('Cadastrar', size = (20, 1)), sg.ReadButton('Voltar', size = (20, 1))]
            ]
        else: #preenche o campo de texto com o nome atual em caso de edição.
            layout = [
                [sg.Txt('Nome: ', justification='center'), sg.InputText(nome_atual, key = '-nome-')],
                [sg.ReadButton('Cadastrar', size = (20, 1)), sg.ReadButton('Voltar', size = (20, 1))]
            ]
        self.__window = sg.Window('Cadastro de Enfermeiro', element_justification = 'c').Layout(layout)
        button, values = self.__window.Read()
        if button == 'Voltar' or button == sg.WIN_CLOSED: #retorna none se a pessoa fechar a janela ou clicar em voltar. deve ser tratado onde essa função for utilizada.
            retorno = None
        elif button == 'Cadastrar' and values['-nome-'] is not None:
            retorno = values['-nome-']
        self.__window.Close()
        return retorno

    def mostra_enfermeiros(self, lista_enfermeiros):
        if lista_enfermeiros is not None: #só cria a string caso existam enfermeiros...
            big_string = ''
            for enfermeiro in lista_enfermeiros:
                big_string =  str(big_string) + '\nCódigo: ' + str(enfermeiro['codigo']) + '\n' + 'Nome: ' + str(enfermeiro['nome']) + '\n--------------------------' #gambiarra mas é o que temos.
            layout = [
                [sg.Txt('Lista de enfermeiros cadastrados:')],
                [sg.Txt(big_string)],
                [sg.Exit('Ok', size = (20, 1))]
                ]
            self.__window = sg.Window("Lista de enfermeiros").Layout(layout)
            button, values = self.__window.Read()
            self.__window.Close()
    
    def combo_box_enfermeiros(self, lista_enfermeiros): #cria um combobox com todos os enfermeiros cadastrados atravez de uma lista de dicionarios recebida do controlador e retorna um dicionario com o enfermeiro selecionado. 
        if lista_enfermeiros is not None: #só cria a combobox se existirem enfermeiros
            codigos_nomes = []
            for enfermeiro in lista_enfermeiros:
                codigos_nomes.append(str(enfermeiro['codigo']) + ' - ' + enfermeiro['nome']) #separa os codigos e os nomes em uma lista para criar o combobox
            layout = [
                [sg.InputCombo(codigos_nomes, key = '-codigo_nome-')],
                [sg.ReadButton('Selecionar', size = (20, 1)), sg.ReadButton('Voltar', size = (20, 1))]
            ]
            self.__window = sg.Window("Seleção de enferemeiro").Layout(layout)
            button, values = self.__window.Read()
            self.__window.Close()
            if button == 'Selecionar':
                if values['-codigo_nome-'] == '': #clicou em selecionar sem selecionar nenhum nome
                    selecionado = values['-codigo_nome-']  # retorna '' (string vazia), tratar onde esta função for utilizada.
                else:
                    selecionado = int(values['-codigo_nome-'].split(' ')[0])
            if button == 'Voltar' or button == sg.WIN_CLOSED: #retorna none se a pessoa fechar a janela ou clicar em voltar. deve ser tratado onde essa função for utilizada.
                selecionado = None
        else:
            selecionado = None #retorna None caso não existam enfermeiros cadastrados.
        return selecionado #retorna None se fechar ou voltar, '' se não selecionar nenhum e clicar em "selecionar", ou o codigo do enfermeiro selecionado.

    def mensagem(self, mensagem: str): #função para exibir avisos na tela.
        layout = [
            [sg.Txt(mensagem)],
            [sg.Exit('Ok', size = (20, 1))]
        ]
        self.__window = sg.Window('Aviso!', element_justification = 'c').Layout(layout)
        buttons, values = self.__window.Read()
        self.__window.Close()

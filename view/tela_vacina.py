import sys
sys.path.append(".")
import os
import PySimpleGUI as sg
class TelaVacina():
    def __init__(self):
        self.__window = None

    def menu_vacina(self):
        layout = [
                [sg.Txt('Controle de vacinas. Clique na opção desejada: ', justification='center')],
                [sg.ReadButton('Incluir doses no estoque', size = (30, 1), key = 1)],
                [sg.ReadButton('Remover doses do estoque', size = (30, 1), key = 2)],
                [sg.ReadButton('Consultar vacinas disponíveis', size = (30, 1), key = 3)],
                [sg.ReadButton('Voltar', size = (30, 1), key = 0)]
            ]
        self.__window = sg.Window('PACIENTES', size = (400, 230), element_justification='c').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        opcao = button
        return opcao

    def ler_dados(self):
        layout = [
            [sg.Txt('Tipo: ', justification='center'), sg.InputText(key = '-tipo-')],
            [sg.Txt('Fabricante: ', justification='center'), sg.InputText(key = '-fabricante-')],
            [sg.Txt('Quantidade: ', justification='center'), sg.InputText(key = '-quantidade-')],
            [sg.ReadButton('Cadastrar', size=(20,1)),sg.ReadButton('Voltar', size=(20,1))]
        ]
        self.__window = sg.Window('Inclusão de Vacinas', element_justification = 'c').Layout(layout)
        button, values = self.__window.Read()
        retorno = {}
        if button == 'Cadastrar': #retorna o valor digitado ou '' se a pessoa clicar em cadastrar.
            retorno['tipo'] = values['-tipo-']
            retorno['fabricante'] = values['-fabricante-']
            retorno['quantidade'] = values['-quantidade-']
        if button == 'Voltar' or button == sg.WIN_CLOSED: #retorna none se a pessoa fechar a janela ou clicar em voltar. deve ser tratado onde essa função for utilizada.
            retorno = None
        self.__window.Close()
        return retorno
    
    #funcao anterior utilizada para leo o codigo e selecionar uma vacina
    #não é mais necessária, podemos excluir depois
    #def ler_codigo(self):
    #    codigo = int(input("Código: "))
    #    return codigo

    def ler_quantidade(self):
        layout=[
            [sg.Txt('Quantidade: ', justification='center'), sg.InputText(key='-quantidade-')],
            [sg.ReadButton('Confirmar',size=(20,1)), sg.ReadButton('Voltar',size=(20,1))]
        ]
        self.__window = sg.Window("Quantidade").Layout(layout)
        button, values = self.__window.Read()
        quantidade = int(0)
        if button == 'Confirmar': #retorna o valor digitado ou 0 se a pessoa clicar em confirmar sem informar uma quantidade.
            if values['-quantidade-']=='':
                quantidade = 0
            else:
                quantidade = values['-quantidade-']
        if button == 'Voltar' or button == sg.WIN_CLOSED: #retorna none se a pessoa fechar a janela ou clicar em voltar. deve ser tratado onde essa função for utilizada.
            quantidade = None
        self.__window.Close()
        return quantidade

    

    def listar_vacinas(self, lista_vacinas):
        if lista_vacinas is not None: #só cria a string caso existam vacinas cadastradas...
            big_string = ''
            for vacina in lista_vacinas:
                big_string =  str(big_string) + '\nCódigo: ' + str(vacina['codigo']) + '\n' + 'Tipo: ' + str(vacina['tipo']) + '\n' + 'Fabricante: ' + str(vacina['fabricante']) + '\n' + 'Qauntidade disponível: ' + str(vacina['quantidade']) + '\n--------------------------' #cria uma string com todas as vacinas do estoque para poder mostrar na tela
            layout = [
                [sg.Txt('Lista de vacinas disponíveis:')],
                [sg.Txt(big_string)],
                [sg.Exit('Ok', size = (20, 1))]
                ]
            self.__window = sg.Window("Lista de vacinas disponíveis").Layout(layout)
            button, values = self.__window.Read()
            self.__window.Close()

    def selecionar_vacina(self, lista_vacinas):
        if lista_vacinas is not None: #só cria a combobox se existirem vacinas
            dados_vacinas = []
            for vacina in lista_vacinas:
                cod_tipo_fabricante = str(vacina['codigo']) + ' - ' + str(vacina['tipo']) + ' - ' + str(vacina['fabricante'])
                dados_vacinas.append(cod_tipo_fabricante) #cria lista de dados da vacina para criar o combobox
            layout = [
                [sg.Txt('Selecione a vacina desejada.')],
                [sg.Txt('Codigo - Tipo - Fabricante')],
                [sg.InputCombo(dados_vacinas, key = '-dados_vacinas-')],
                [sg.ReadButton('Selecionar', size = (20, 1)), sg.ReadButton('Voltar', size = (20, 1))]
            ]
            self.__window = sg.Window("Seleção de Vacina").Layout(layout)
            button, values = self.__window.Read()
            self.__window.Close()
            if button == 'Selecionar':
                if values['-dados_vacinas-'] == '': #clicou em selecionar sem selecionar nenhuma vacina
                    selecionado = values['-dados_vacinas-']  # retorna '' (string vazia), tratar onde esta função for utilizada.
                else:
                    selecionado = int(values['-dados_vacinas-'].split(' ')[0]) #pega o código selecionado
            if button == 'Voltar' or button == sg.WIN_CLOSED: #retorna none se a pessoa fechar a janela ou clicar em voltar. deve ser tratado onde essa função for utilizada.
                selecionado = None
        else:
            selecionado = None #retorna None caso não existam vacinas cadastradas.
        return selecionado #retorna None se fechar ou voltar, '' se não selecionar nenhum e clicar em "selecionar", ou o código da vacina selecionada.

    def mensagem(self, mensagem: str): #função para exibir avisos na tela.
        layout = [
            [sg.Txt(mensagem)],
            [sg.Exit('Ok', size = (20, 1))]
        ]
        self.__window = sg.Window('Aviso!', element_justification = 'c').Layout(layout)
        buttons, values = self.__window.Read()
        self.__window.Close()





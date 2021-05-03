import os
import PySimpleGUI as sg
class TelaSistema():

    def __init__(self):
        self.__window = None

    def mostra_menu_principal(self):
        layout = [
                [sg.Txt('Bem vindo ao sistema de gerenciamento de vacinação!\nClique na opção desejada:', justification='center')],
                [sg.ReadButton('Controle de Enfermeiros', size = (30, 1), key = 1)],
                [sg.ReadButton('Controle de Pacientes', size = (30, 1), key = 2)],
                [sg.ReadButton('Controle de Agendamentos', size = (30, 1), key = 3)],
                [sg.ReadButton('Controle de Vacinas', size = (30, 1), key = 4)],
                [sg.ReadButton('Listar Atendimentos por enfermeiro', size = (30, 1), key = 5)],
                [sg.ReadButton('Relatorio Gerencial', size = (30, 1), key = 6)],
                [sg.ReadButton('Sair', size = (30, 1), key = 0)]
            ]
        self.__window = sg.Window('SISTEMA DE GERENCIAMENTO DE VACINAÇÃO', size = (400, 300), element_justification='c').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        opcao = button
        return opcao

    def mostra_relatorio(self, relatorio):
        layout = [
            [sg.Txt('=====RELATÓRIO GERENCIAL=====', size = (50,1), justification = 'c')],
            [sg.Txt('O numero de pacientes na fila é: ' + str(relatorio['fila']) + '.')],
            [sg.Txt('O numero de pacientes que já tomaram a primeira dose é: ' + str(relatorio['total_primeira_dose']) + '.')],
            [sg.Txt('O numero de pacientes que já tomaram a segunda dose é: ' + str(relatorio["total_segunda_dose"]) + '.')],
            [sg.Txt('O numero total de doses aplicadas é : ' + str(relatorio['total_doses']) + '.')],
            [sg.ReadButton('Voltar', pad=((180, 0), 3))] 
        ]
        self.__window = sg.Window('Relatório').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        
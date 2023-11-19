import sys
sys.path.append(".")
import PySimpleGUI as sg

class TelaAgendamento():

    def __init__(self):
        self.__window = None
   
    def opcoes_agendamento(self):
        layout = [
                [sg.Txt('Controle de Agendamentos. Clique na opção desejada: ', justification='center')],
                [sg.ReadButton('Cadastrar novo agendamento', size = (30, 1), key = 1)],
                [sg.ReadButton('Excluir agendamento', size = (30, 1), key = 2)],
                [sg.ReadButton('Editar agendamento', size = (30, 1), key = 3)],
                [sg.ReadButton('Listar agendamentos', size = (30, 1), key = 4)],
                [sg.ReadButton('Concluir agendamento', size = (30,1), key = 5)],
                [sg.ReadButton('Voltar', size = (30, 1), key = 0)]
            ]
        self.__window = sg.Window('AGENDAMENTOS', size = (400, 230), element_justification='c').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        opcao = button
        return opcao
    
    def seleciona_dados(self, lista_pacientes, lista_enfermeiros, dados_anteriores = None):
        if lista_pacientes is not None and lista_enfermeiros is not None: #só cria a combobox se existirem pacientes, enfermeiros e vacinas já cadastrados
            dados_pacientes = []
            for paciente in lista_pacientes:
                cod_nome = str(paciente['codigo']) + ' - ' + str(paciente['nome'])
                dados_pacientes.append(cod_nome) #cria lista de dados dos pacientes para criar o combobox
            dados_enfermeiros = []
            for enfermeiro in lista_enfermeiros:
                cod_nome = str(enfermeiro['codigo']) + ' - ' + str(enfermeiro['nome'])
                dados_enfermeiros.append(cod_nome) #cria lista com dados dos enfermeiros para criar o combobox
            if dados_anteriores is None:
                layout = [
                    [sg.Txt('Selecione os campos para adicionar ou editar o agendamento')],
                    [sg.Txt('Paciente: '), sg.InputCombo(dados_pacientes, key = '-dados_paciente-')],
                    [sg.Txt('Enfermeiro: '), sg.InputCombo(dados_enfermeiros, key = '-dados_enfermeiro-')],
                    [sg.Txt('Data (DD/MM/AAA): '), sg.InputText(key = '-data-')],
                    [sg.Txt('Hora (hh:mm): '), sg.InputText(key = '-hora-')],
                    [sg.ReadButton('Agendar', size = (20, 1)), sg.ReadButton('Voltar', size = (20, 1))]
                ]
            if dados_anteriores is not None:
                layout = [
                    [sg.Txt('Selecione os campos para adicionar ou editar o agendamento')],
                    [sg.Txt('Paciente: '), sg.InputCombo(dados_pacientes, default_value = dados_anteriores['paciente'], key = '-dados_paciente-')],
                    [sg.Txt('Enfermeiro: '), sg.InputCombo(dados_enfermeiros, default_value = dados_anteriores['enfermeiro'], key = '-dados_enfermeiro-')],
                    [sg.Txt('Data (DD/MM/AAA): '), sg.InputText(dados_anteriores['data'], key = '-data-')],
                    [sg.Txt('Hora (hh:mm): '), sg.InputText(dados_anteriores['hora'], key = '-hora-')],
                    [sg.ReadButton('Agendar', size = (20, 1)), sg.ReadButton('Voltar', size = (20, 1))]
                ]
            self.__window = sg.Window("Cadastro de Agendamento").Layout(layout)
            button, values = self.__window.Read()
            self.__window.Close()
            if button == 'Agendar':
                selecionado = {'paciente': values['-dados_paciente-'], 'enfermeiro': values['-dados_enfermeiro-'], 'data': values['-data-'], 'hora': values['-hora-']}  # retorna '' (string vazia), tratar onde esta função for utilizada.
            if button == 'Voltar' or button == sg.WIN_CLOSED: #retorna none se a pessoa fechar a janela ou clicar em voltar. deve ser tratado onde essa função for utilizada.
                selecionado = None
        else:
            selecionado = None #retorna None caso não existam pacientes ou enfermeiros cadastrados.
        return selecionado #retorna None se fechar ou voltar, '' se não selecionar nenhum e clicar em "selecionar", ou o dicionário com as informações selecionadas.

    def selecionar_vacina(self, lista_vacinas, dados_anteriores = None):
        if lista_vacinas is not None: #só cria a combobox se existirem vacinas
            dados_vacinas = []
            for vacina in lista_vacinas:
                cod_tipo_fabricante = str(vacina['codigo']) + ' - ' + str(vacina['tipo']) + ' - ' + str(vacina['fabricante'])
                dados_vacinas.append(cod_tipo_fabricante) #cria lista de dados da vacina para criar o combobox
            if dados_anteriores is not None:
                layout = [
                    [sg.Txt('Selecione a vacina desejada.')],
                    [sg.Txt('Codigo - Tipo - Fabricante')],
                    [sg.InputCombo(dados_vacinas, default_value = dados_anteriores['vacina'], key = '-dados_vacinas-')],
                    [sg.ReadButton('Selecionar', size = (20, 1)), sg.ReadButton('Voltar', size = (20, 1))]
                ]
            if dados_anteriores is None:
                layout = [
                    [sg.Txt('Selecione a vacina desejada.')],
                    [sg.Txt('Codigo - Tipo - Fabricante')],
                    [sg.InputCombo(dados_vacinas, key = '-dados_vacinas-'), ],
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
    
    def seleciona_agendamento(self, lista_agendamentos):
        if lista_agendamentos is not None: #só cria a combobox se existirem vacinas
            dados_agendamentos = []
            for agendamento in lista_agendamentos:
                cod_paciente = str(agendamento['codigo']) + ' - ' + str(agendamento['paciente'])
                dados_agendamentos.append(cod_paciente) #cria lista de dados do agendamento para criar o combobox
            layout = [
                [sg.Txt('Selecione o agendamento desejado.')],
                [sg.Txt('Codigo - Paciente')],
                [sg.InputCombo(dados_agendamentos, key = '-dados_agendamentos-')],
                [sg.ReadButton('Selecionar', size = (20, 1)), sg.ReadButton('Voltar', size = (20, 1))]
            ]
            self.__window = sg.Window("Seleção de Agendamento").Layout(layout)
            button, values = self.__window.Read()
            self.__window.Close()
            if button == 'Selecionar':
                if values['-dados_agendamentos-'] == '': #clicou em selecionar sem selecionar nenhuma vacina
                    selecionado = values['-dados_agendamentos-']  # retorna '' (string vazia), tratar onde esta função for utilizada.
                else:
                    selecionado = int(values['-dados_agendamentos-'].split(' ')[0]) #pega o código selecionado
            if button == 'Voltar' or button == sg.WIN_CLOSED: #retorna none se a pessoa fechar a janela ou clicar em voltar. deve ser tratado onde essa função for utilizada.
                selecionado = None
        else:
            selecionado = None #retorna None caso não existam vacinas cadastradas.
        return selecionado #retorna None se fechar ou voltar, '' se não selecionar nenhum e clicar em "selecionar", ou o código da vacina selecionada.

    def listar_agendamentos(self, lista_agendamentos, texto = 'agendamentos:'):
        if lista_agendamentos is not None: #só cria a string caso existam vacinas cadastradas...
            big_string = ''
            for agendamento in lista_agendamentos:
                big_string =  str(big_string) + '\nCódigo: ' + str(agendamento['codigo']) + '\n' + 'Paciente: ' + str(agendamento['paciente']) + '\n' + 'Enfermeiro: ' + str(agendamento['enfermeiro']) + '\n' + 'Vacina: ' + str(agendamento['vacina']) + '\n' + 'Data e Hora: ' + str(agendamento['data_hora']) + '\n' + 'Conclusão: ' + str(agendamento['conclusao']) + '\n--------------------------' #cria uma string com todas as vacinas do estoque para poder mostrar na tela
                #big_string =  str(big_string) + '\nCódigo: ' + str(agendamento['codigo']) + '\n' + 'Vacina: ' + str(agendamento['vacina']) + '\n' + 'Data e Hora: ' + str(agendamento['data_hora']) + '\n' + 'Conclusão: ' + str(agendamento['conclusao']) + '\n--------------------------'
            layout = [
                [sg.Txt('Lista de ' + texto)],
                [sg.Txt(big_string)],
                [sg.Exit('Ok', size = (20, 1))]
                ]
            self.__window = sg.Window("Lista de agendamentos").Layout(layout)
            button, values = self.__window.Read()
            self.__window.Close()
    
    def selecionar_lista_agendamentos(self):
        layout = [
                [sg.Txt('Controle de Agendamentos. Clique na opção desejada: ', justification='center')],
                [sg.ReadButton('Listar Agendamentos em Aberto', size = (30, 1), key = 1)],
                [sg.ReadButton('Listar Agendamentos Concluídos', size = (30, 1), key = 2)],
                [sg.ReadButton('Listar Todos os Agendamentos', size = (30, 1), key = 3)],
                [sg.ReadButton('Voltar', size = (30,1), key = 0)]
        ]
        self.__window = sg.Window('AGENDAMENTOS', size = (400, 230), element_justification='c').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        opcao = button
        return opcao

    def mensagem(self, mensagem: str): #função para exibir avisos na tela.
        layout = [
            [sg.Txt(mensagem)],
            [sg.Exit('Ok', size = (20, 1))]
        ]
        self.__window = sg.Window('Aviso!', element_justification = 'c').Layout(layout)
        buttons, values = self.__window.Read()
        self.__window.Close()
    
    
    
    
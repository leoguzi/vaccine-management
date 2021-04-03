import sys
sys.path.append(".")

from controller.controlador_enfermeiros import ControladorEnfermeiros
from controller.controlador_pacientes import ControladorPacientes
from controller.controlador_vacinas import ControladorVacina
from view.tela_agendamento import TelaAgendamento

class ControladorAgendamento():
    def __init__(self, tela_agendamento:TelaAgendamento, controlador_paciente: ControladorPacientes, controlador_enfermeiro: ControladorEnfermeiro, controlador_vacina: ControladorVacina):
        self.__tela_agendamento = tela_agendamento
        self.__controlador_paciente = controlador_paciente
        self.__controlador_enfermeiro = controlador_enfermeiro
        self.__controlador_vacina = controlador_vacina
        self.__lista_de_agendamentos = []
        self.__gera_codigo_agendamento = int(500)

    def setAgendamento(self):
        from model.agendamento import Agendamento

    def inserir_novo_agendamento(self):
        self.setAgendamento()
        n_doses = 0
        self.__controlador_paciente.lista_pacientes()
        codigo_paciente = self.__tela_agendamento.ler_paciente()
        self.__controlador_enfermeiro.lista_enfermeiros()
        codigo_enfermeiro = self.__tela_agendamento.ler_enfermeiro()
        data_hora = self.__tela_agendamento.ler_data_hora()
        novo_agendamento = None
        paciente = self.__controlador_paciente.encontra_paciente_por_codigo(codigo_paciente)
        enfermeiro = self.__controlador_enfermeiro.encontra_enfermeiro_por_codigo(codigo_enfermeiro)
        for i in range(len(lista_de_agendamentos)):
            if (paciente == self.__lista_de_agendamentos[i].paciente and self.__lista_de_agendamentos[i].conclusao == True):
                n_doses += 1
        try:
            n_doses > 0 and n_doses < 2
            if n_doses == 0:
                ControladorVacina.retorna_estoque()
                codigo_da_vacina = self.__tela_agendamento.ler_vacina()
                vacina = self.__controlador_vacina.lista_de_vacinas[self.__controlador_vacina.encontra_indice_por_codigo(codigo_da_vacina)]
            if n_doses == 1:
                indice = self.__encontra_agendamento_por_paciente(paciente)
                vacina = self.__lista_de_agendamentos[indice].vacina
        except:
            print("Este paciente já tomou duas doses da vacina. Não é possível fazer um novo agendamento.")
        
        else:
        novo_agendamento = Agendamento(paciente,enfermeiro,vacina,data_hora,False)
        self.__gera_codigo_agendamento += 1
        self.__lista_de_agendamentos.append(novo_agendamento)
    
    def __encontra_agendamento_por_paciente(self,paciente):
        indice = None
        for i in range(len(self.__lista_de_agendamentos)):
            if paciente == self.__lista_de_agendamentos[i].paciente:
                indice = i
                return indice
            



    def inicia_tela_agendamento(self):
        lista_opcoes={1: self.inserir_novo_agendamento}
        while True:
            try:
                valor_lido = self.__tela_agendamento.opcoes_agendamento()
                if valor_lido >=0 and valor_lido<=1:
                    lista_opcoes[valor_lido]()
                else:
                    raise ValueError
            except ValueError:
                print("\nOpção Invalida! Digite um numero inteiro entre 0 e 1!\n")

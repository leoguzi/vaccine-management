import sys
sys.path.append(".")

from controller.controlador_enfermeiros import ControladorEnfermeiros
from controller.controlador_pacientes import ControladorPacientes
from controller.controlador_vacinas import ControladorVacina
from model.agendamento import Agendamento
from view.tela_agendamento import TelaAgendamentos

class ControladorAgendamentos:
    def __init__(self, tela_agendamento:TelaAgendamentos):
        self.__tela_agendamento = tela_agendamento
        self.__lista_de_agendamentos = []
        self.__gera_codigo_agendamento = int(500)

    def inserir_novo_agendamento(self):
        n_doses = 0
        dados_agendamento = self.__tela_agendamento.ler_dados()
        novo_agendamento = None
        paciente = ControladorPacientes.encontra_paciente_por_codigo(dados_agendamento["paciente"])
        enfermeiro = ControladorEnfermeiros.encontra_enfermeiro_por_codigo(dados_agendamento["enfermeiro"])
        for i in range(len(lista_de_agendamentos)):
            if (paciente == self.__lista_de_agendamentos[i].paciente and self.__lista_de_agendamentos[i].conclusao == True:
                n_doses += 1
        try:
            n_doses > 0 and n_doses < 2
            if n_doses == 0:
                ControladorVacina.retorna_estoque()
                codigo_da_vacina = self.__tela_agendamento.ler_codigo_da_vacina()
            if n_doses == 1:
                indice = self.__encontra_agendamento_por_paciente(dados_agendamento["paciente"])
                codigo_da_vacina = self.__lista_de_agendamentos[i].vacina
        except:
            print("Este paciente já tomou duas doses da vacina. Não é possível fazer um novo agendamento.")
        
        else:
            vacina = ControladorVacina.encontra_indice_por_codigo(codigo_da_vacina)
            novo_agendamento = Agendamento(dados_agendamento["paciente"],dados_agendamento["enfermeiro"],ControladorVacina.lista_de_vacinas[vacina](),dados_agendamento["data_hora"],False)
            self.__gera_codigo_agendamento += 1

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

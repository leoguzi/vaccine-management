import os
import sys
sys.path.append(".")
from controller.controlador_enfermeiros import ControladorEnfermeiros
from controller.controlador_pacientes import ControladorPacientes
from controller.controlador_vacinas import ControladorVacina
from controller.controlador_agendamentos import ControladorAgendamento
from view.tela_agendamento import TelaAgendamento
from view.tela_vacina import TelaVacina
from view.tela_sistema import TelaSistema
from view.tela_enfermeiro import TelaEnfermeiros
from view.tela_paciente import TelaPaciente


class ControladorSistema():
    def __init__(self, tela_sistema: TelaSistema):
        self.__tela_sistema = tela_sistema
        self.__controlador_pacientes = ControladorPacientes(TelaPaciente())
        self.__controlador_enfermeiros = ControladorEnfermeiros(TelaEnfermeiros())
        self.__controlador_vacinas = ControladorVacina(TelaVacina())
        self.__controlador_agendamento = ControladorAgendamento(TelaAgendamento(), self.__controlador_pacientes, self.__controlador_enfermeiros, self.__controlador_vacinas)
    def encerra_sistema(self):
        exit(0)

    def abre_menu_principal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        lista_opcoes = {1: self.__controlador_enfermeiros.abre_tela_enfermeiros, 2: self.__controlador_pacientes.abre_tela_pacientes, 3: self.__controlador_agendamento.inicia_tela_agendamento, 4: self.__controlador_vacinas.inicia_tela_vacina, 5: self.listar_atendimentos_enfermeiro, 6: self.gera_relatorio, 0: self.encerra_sistema} #adicionar as outras opções quando prontas
        while True:
            try:
                valor_lido = self.__tela_sistema.mostra_menu_principal()
                if valor_lido >=0 and valor_lido<=6:
                    lista_opcoes[valor_lido]()
                else:
                    raise ValueError
            except ValueError:
                print("\nOpção Invalida! Digite um numero inteiro entre 0 e 6!\n")

    def listar_atendimentos_enfermeiro(self):
        try:
            if len(self.__controlador_enfermeiros.enfermeiros) > 0:
                lista_atendimentos_concluidos = self.__controlador_agendamento.retorna_agendamentos_concluidos()
                self.__controlador_enfermeiros.lista_enfermeiros()
                codigo_enfermeiro = self.__controlador_enfermeiros.retorna_codigo_lido()
                print("Lista de pacientes atendidos pelo enfermeiro escolhido: ")
                for atendimento in lista_atendimentos_concluidos:
                    enfermeiro = atendimento.enfermeiro
                    if codigo_enfermeiro == enfermeiro.codigo:
                        self.__controlador_agendamento.mostra_agendamento(atendimento)
            else: 
                raise Exception
        except:
            wait = input("Nenhum enfermeiro Cadastrado. Pressione enter...")
            os.system('cls' if os.name == 'nt' else 'clear')
            
    def gera_relatorio(self):
        lista_pacientes = self.__controlador_pacientes.pacientes
        total_doses_aplicadas = 0
        pacientes_fila = 0
        pacientes_primeira_dose = 0
        pacientes_segunda_dose = 0
        for paciente in lista_pacientes:
            if paciente.numero_doses == 0:
                pacientes_fila +=1
            elif paciente.numero_doses == 1:
                pacientes_primeira_dose +=1
                total_doses_aplicadas +=1
            else:
                pacientes_segunda_dose +=1
                total_doses_aplicadas +=2
        self.__tela_sistema.mostra_relatorio({"fila": pacientes_fila, "total_primeira_dose": pacientes_primeira_dose, "total_segunda_dose": pacientes_segunda_dose, "total_doses": total_doses_aplicadas})
    

     


import os
import sys
sys.path.append(".")

from controller.controlador_enfermeiros import ControladorEnfermeiros
from controller.controlador_pacientes import ControladorPacientes
from controller.controlador_vacinas import ControladorVacina
from view.tela_agendamento import TelaAgendamento
from model.agendamento import Agendamento

class ControladorAgendamento():
    def __init__(self, tela_agendamento:TelaAgendamento, controlador_paciente: ControladorPacientes, controlador_enfermeiro: ControladorEnfermeiros, controlador_vacina: ControladorVacina):
        self.__tela_agendamento = tela_agendamento
        self.__controlador_paciente = controlador_paciente
        self.__controlador_enfermeiro = controlador_enfermeiro
        self.__controlador_vacina = controlador_vacina
        self.__lista_de_agendamentos = []
        self.__gera_codigo_agendamento = int(500)
        self.__lista_de_agendamentos_concluidos = []
        self.__lista_de_agendamentos_em_aberto = []
        
    def inserir_novo_agendamento(self):
        n_doses = 0
        if len(self.__controlador_paciente.pacientes) == 0:
            return print("Cadastre pelo menos um paciente antes de cadastrar um agendamento")
        print("\n========== SELEÇÃO DE PACIENTES =========\n")
        self.__controlador_paciente.lista_pacientes()
        codigo_paciente = self.__tela_agendamento.ler_paciente()
        if len(self.__controlador_enfermeiro.enfermeiros) == 0:
            return print("Cadastre pelo menos um enfermeiro antes de cadastrar um agendamento")
        if len(self.__controlador_vacina.lista_de_vacinas) == 0:
            return print("Cadastre pelo menos um tipo de vacina antes de cadastrar um agendamento.")
        print("\n========== SELEÇÃO DE ENFERMEIROS ==========\n")
        self.__controlador_enfermeiro.lista_enfermeiros()
        codigo_enfermeiro = self.__tela_agendamento.ler_enfermeiro()
        print("\n========== ESCOLHA DE DATA E HORÁRIO ==========\n")
        data_hora = self.__tela_agendamento.ler_data_hora()
        novo_agendamento = None
        paciente = self.__controlador_paciente.encontra_paciente_por_codigo(codigo_paciente)
        enfermeiro = self.__controlador_enfermeiro.encontra_enfermeiro_por_codigo(codigo_enfermeiro)
        for i in range(len(self.__lista_de_agendamentos)):
            if (paciente == self.__lista_de_agendamentos[i].paciente and self.__lista_de_agendamentos[i].conclusao == True):
                n_doses += 1
            if (paciente == self.__lista_de_agendamentos[i].paciente and self.__lista_de_agendamentos[i].conclusao == False):
                return print("Este paciente já possui um agendamento em aberto. Conclua ou exclua o agendamento existente antes de cadastrar outro.")
        try:
            n_doses >= 0 and n_doses < 2
        except:
            print("Este paciente já tomou duas doses da vacina. Não é possível fazer um novo agendamento.")
        
        else:
            if n_doses == 0:
                print("\n========== SELEÇÃO DE VACINA ==========\n")
                self.__controlador_vacina.retorna_estoque()
                codigo_da_vacina = self.__tela_agendamento.ler_vacina()
                vacina = self.__controlador_vacina.encontra_vacina_por_codigo(codigo_da_vacina)
                dose = 1
                n_doses_necessarias = 2
            if n_doses == 1:
                agendamento = self.encontra_agendamento_por_paciente(paciente) #erro de digitação corrigido aqui! (estava com .__, mas é um metodo desta classe, léo)
                vacina = agendamento.vacina
                dose = 2
                n_doses_necessarias = 1
            try:
                self.__controlador_vacina.consulta_dose_estoque(vacina.codigo,n_doses_necessarias)
            except:
                print("Não é possível realizar este agendamento, pois não há doses de vacinas disponíveis no estoque.")
            else:
                novo_agendamento = Agendamento(paciente,enfermeiro,vacina,data_hora,dose,self.__gera_codigo_agendamento,False)
                self.__gera_codigo_agendamento += 1
                self.__lista_de_agendamentos.append(novo_agendamento)
                self.__lista_de_agendamentos_em_aberto.append(novo_agendamento)
                print("\nAgendamento cadastrado ou alterado com sucesso!\n")
                return novo_agendamento
        
    def encontra_agendamento_por_paciente(self, paciente):
        for i in range(len(self.__lista_de_agendamentos)):
            if paciente == self.__lista_de_agendamentos[i].paciente:
                agendamento = self.__lista_de_agendamentos[i]
                return agendamento
    
    def encontra_agendamento_por_codigo(self,codigo):
        agendamento = None
        while agendamento is None:
            for i in range(len(self.__lista_de_agendamentos)):
                if codigo == self.__lista_de_agendamentos[i].codigo:
                    agendamento = self.__lista_de_agendamentos[i]
                    return agendamento
            print("Agendamento não encontrado. Informe um código válido.")
            codigo = self.__tela_agendamento.ler_codigo()

    
    def edita_agendamento(self):
        if len(self.__lista_de_agendamentos_em_aberto) == 0:
            print("Não é possível alterar um agendamento, pois não há agendamentos em aberto cadastrados neste posto, e não é possível alterar agendamento concluídos.")
        else:
            self.lista_agendamentos_em_aberto()
            print("\nInforme o código do agendamento que você deseja alterar\n")
            codigo = self.__tela_agendamento.ler_codigo()
            agendamento = self.encontra_agendamento_por_codigo(codigo)
            if agendamento.conclusao:
                return print("Não é possível alterar um agendamento concluído")
            else:
                agendamento.paciente = None
                print("\nInforme os novos dados para o agendamento.\n")
                agendamento_auxiliar = self.inserir_novo_agendamento()
                agendamento.paciente = agendamento_auxiliar.paciente
                agendamento.enfermeiro = agendamento_auxiliar.enfermeiro
                agendamento.data_hora = agendamento_auxiliar.data_hora
                agendamento.vacina = agendamento_auxiliar.vacina
                self.__lista_de_agendamentos_em_aberto.remove(agendamento_auxiliar)
                self.__lista_de_agendamentos.remove(agendamento_auxiliar)

    def excluir_agendamento(self):
        if len(self.__lista_de_agendamentos) == 0:
            return print("Não é possível excluir nenhum agendamento, pois não há nenhum agendamento cadastrado no posto.")
        else:
            print("Informe o código do agendamento que você deseja excluir.")
            self.lista_todos_agendamentos()
            codigo = self.__tela_agendamento.ler_codigo()
            agendamento = self.encontra_agendamento_por_codigo(codigo)
            self.__lista_de_agendamentos.remove(agendamento)
            if agendamento.conclusao:
                self.__lista_de_agendamentos_concluidos.remove(agendamento)
            else:
                self.__lista_de_agendamentos_em_aberto.remove(agendamento)
            print("\nSolicitação efetivada com sucesso!\n")
    
    def lista_agendamentos(self):
        opcoes_de_lista = {1: self.lista_agendamentos_em_aberto, 2: self.lista_agendamentos_concluidos, 3: self.lista_todos_agendamentos}
        try:
            valor_lido = self.__tela_agendamento.selecionar_lista_agendamentos()
            if valor_lido >= 0 and valor_lido <= 3:
                opcoes_de_lista[valor_lido]()
            else:
                raise ValueError
        except ValueError:
            print("\nOpção Invalida! Digite um numero inteiro entre 1 e 3!\n")
    
    def lista_todos_agendamentos(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Lista de agendamentos:")
        for agendamento in self.__lista_de_agendamentos:
            dados_agendamentos = {"paciente": agendamento.paciente.nome, "enfermeiro":agendamento.enfermeiro.nome,"vacina":agendamento.vacina.tipo, "data_hora":agendamento.data_hora,"codigo":agendamento.codigo,"conclusao":agendamento.conclusao}
            self.__tela_agendamento.listar_agendamentos(dados_agendamentos)
    
    def concluir_agendamento(self):
        self.lista_agendamentos_em_aberto()
        print("Informe o código do agendamento que você deseja concluir")
        codigo = self.__tela_agendamento.ler_codigo()
        agendamento = self.encontra_agendamento_por_codigo(codigo)
        try:
            agendamento.conclusao is False
        except:
            print("Este agendamento já foi concluído anteriormente. Selecione um agendamento em aberto para concluir.")
        else:
            agendamento.conclusao = True
            self.__lista_de_agendamentos_em_aberto.remove(agendamento)
            self.__lista_de_agendamentos_concluidos.append(agendamento)
            codigo_vacina = agendamento.vacina.codigo
            self.__controlador_vacina.remove_dose_aplicada_do_estoque(codigo_vacina)
            codigo_paciente = agendamento.paciente.codigo
            self.__controlador_paciente.vacina_paciente(codigo_paciente)

    def lista_agendamentos_em_aberto(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Lista de agendamentos em aberto:")
        for agendamento in self.__lista_de_agendamentos_em_aberto:
            dados_agendamentos = {"paciente":agendamento.paciente.nome, "enfermeiro":agendamento.enfermeiro.nome,"vacina":agendamento.vacina.tipo, "data_hora":agendamento.data_hora,"codigo":agendamento.codigo,"conclusao":agendamento.conclusao}
            self.__tela_agendamento.listar_agendamentos(dados_agendamentos)
    
    def lista_agendamentos_concluidos(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Lista de agendamentos realizados:")
        for agendamento in self.__lista_de_agendamentos_concluidos:
            dados_agendamentos = {"paciente":agendamento.paciente.nome, "enfermeiro":agendamento.enfermeiro.nome,"vacina":agendamento.vacina.tipo, "data_hora":agendamento.data_hora,"codigo":agendamento.codigo,"conclusao":agendamento.conclusao}
            self.__tela_agendamento.listar_agendamentos(dados_agendamentos)

    def retorna_agendamentos_concluidos(self):
        return self.__lista_de_agendamentos_concluidos
    
    def mostra_agendamento(self, agendamento: Agendamento):
        dados_agendamento = {"paciente":agendamento.paciente.nome, "enfermeiro":agendamento.enfermeiro.nome,"vacina":agendamento.vacina.tipo, "data_hora":agendamento.data_hora,"codigo":agendamento.codigo,"conclusao":agendamento.conclusao}
        self.__tela_agendamento.listar_agendamentos(dados_agendamento)


        
    def inicia_tela_agendamento(self):
        lista_opcoes={1: self.inserir_novo_agendamento,2: self.excluir_agendamento, 3: self.edita_agendamento, 4: self.lista_agendamentos, 5: self.concluir_agendamento}
        continua = True
        while continua:
            try:
                valor_lido = self.__tela_agendamento.opcoes_agendamento()
                if valor_lido >=1 and valor_lido <= 5:
                    lista_opcoes[valor_lido]()
                elif valor_lido == 0:
                    continua = False
                    os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    raise ValueError
            except ValueError:
                print("\nOpção Invalida! Digite um numero inteiro entre 0 e 5!\n")

import os
import sys
sys.path.append(".")
from controller.controlador_enfermeiros import ControladorEnfermeiros
from controller.controlador_pacientes import ControladorPacientes
from controller.controlador_vacinas import ControladorVacina
from view.tela_agendamento import TelaAgendamento
from model.agendamento import Agendamento
from model.agendamento_dao import AgendamentoDAO
from controller.excecoes import ListaVaziaException
from controller.excecoes import CampoEmBrancoException
from controller.excecoes import NenhumSelecionadoException
from controller.excecoes import VacinaIndisponivelException

class ControladorAgendamento():
    def __init__(self, tela_agendamento: TelaAgendamento, controlador_paciente: ControladorPacientes, controlador_enfermeiro: ControladorEnfermeiros, controlador_vacina: ControladorVacina):
        self.__tela_agendamento = tela_agendamento
        self.__controlador_paciente = controlador_paciente
        self.__controlador_enfermeiro = controlador_enfermeiro
        self.__controlador_vacina = controlador_vacina
        self.__agendamento_DAO = AgendamentoDAO()
        if len(self.__agendamento_DAO.get_all()) == 0:
            self.__gera_codigo = int(500) #codigo dos agendamentos começa em 500
        else:
            codigo = 500
            for agendamento in self.__agendamento_DAO.get_all(): #encontra o maior codigo que já foi usado.
                if agendamento.codigo > codigo:
                    codigo = agendamento.codigo
            self.__gera_codigo = codigo + 1
        
    def inserir_novo_agendamento(self):
        n_doses = 0
        try: 
            if len(self.__controlador_paciente.lista_pacientes()) == 0:
                raise ListaVaziaException('paciente')
        except ListaVaziaException as mensagem:
            self.__tela_agendamento.mensagem(mensagem)
        try: 
            if len(self.__controlador_enfermeiro.lista_enfermeiros()) == 0:
                raise ListaVaziaException('enfermeiro')
        except ListaVaziaException as mensagem:
            self.__tela_agendamento.mensagem(mensagem)
        try: 
            if len(self.__controlador_vacina.lista_vacinas()) == 0:
                raise ListaVaziaException('vacina')
        except ListaVaziaException as mensagem:
            self.__tela_agendamento.mensagem(mensagem)
        dados_agendamento = self.__tela_agendamento.seleciona_dados(self.__controlador_paciente.lista_pacientes(),self.__controlador_enfermeiro.lista_enfermeiros())
        try: 
            if dados_agendamento['paciente'] == '' or dados_agendamento['enfermeiro'] == '' or dados_agendamento['data'] == '' or dados_agendamento['hora'] == '':
                raise CampoEmBrancoException()
        except CampoEmBrancoException as mensagem:
            self.__tela_agendamento.mensagem(mensagem)
        if dados_agendamento is not None:
            codigo_paciente = int(dados_agendamento['paciente'].split(' ')[0])
            codigo_enfermeiro = int(dados_agendamento['enfermeiro'].split(' ')[0])
            data_hora = str(dados_agendamento['data']) + str(dados_agendamento['hora'])
            paciente = self.__controlador_paciente.encontra_paciente_por_codigo(codigo_paciente)
            enfermeiro = self.__controlador_enfermeiro.encontra_enfermeiro_por_codigo(codigo_enfermeiro)
            agendamento_existente = False
            if len(self.__agendamento_DAO.get_all()) > 0:
                for agendamento in self.__agendamento_DAO.get_all():
                    if (paciente == agendamento.paciente and agendamento.conclusao == True):
                        n_doses += 1
                    if (paciente == agendamento.paciente and agendamento.conclusao == False):
                        agendamento_existente = True
            if agendamento_existente == False:
                if n_doses >= 0 and n_doses < 2:
                    if n_doses == 0:
                        codigo_da_vacina = self.__tela_agendamento.selecionar_vacina(self.__controlador_vacina.lista_vacinas())
                        vacina = self.__controlador_vacina.encontra_vacina_por_codigo(codigo_da_vacina)
                        dose = 1
                        n_doses_necessarias = 2
                    if n_doses == 1:
                        agendamento = self.encontra_agendamento_por_paciente(paciente) #erro de digitação corrigido aqui! (estava com .__, mas é um metodo desta classe, léo)
                        vacina = agendamento.vacina
                        dose = 2
                        n_doses_necessarias = 1
                    try:
                        if self.__controlador_vacina.consulta_dose_estoque(vacina.codigo,n_doses_necessarias):
                            novo_agendamento = Agendamento(paciente,enfermeiro,vacina,data_hora,dose,self.__gera_codigo,False)
                            self.__agendamento_DAO.add(Agendamento(paciente,enfermeiro,vacina,data_hora,dose,self.__gera_codigo,False))
                            self.__gera_codigo += 1
                            return novo_agendamento
                        else:    
                            raise VacinaIndisponivelException
                    except VacinaIndisponivelException as mensagem:
                        self.__tela_agendamento.mensagem(mensagem)
                else:    
                    mensagem = 'Este paciente já tomou duas doses da vacina. Não é possível fazer um novo agendamento.'
                    self.__tela_agendamento.mensagem(mensagem)
            else:
                mensagem = 'Este paciente já possui um agendamento em aberto. Conclua ou exclua o agendamento existente antes de cadastrar outro.'
                self.__tela_agendamento.mensagem(mensagem)
       
    def encontra_agendamento_por_paciente(self, paciente):
        agendamento_selecionado = None
        for agendamento in self.__agendamento_DAO.get_all():
            if agendamento.paciente == paciente:
                agendamento_selecionado = agendamento
        return agendamento_selecionado

    
    def edita_agendamento(self):
        if len(self.__agendamento_DAO.get_all()) == 0:
            self.__tela_agendamento.mensagem("Não é possível alterar um agendamento, pois não há agendamentos em aberto cadastrados neste posto, e não é possível alterar agendamento concluídos.")
        else:
            codigo = self.__tela_agendamento.seleciona_agendamento(self.lista_agendamentos_em_aberto())
            agendamento_selecionado = self.__agendamento_DAO.get(codigo)
            if agendamento_selecionado.conclusao:
                self.__tela_agendamento.mensagem('Não é possível alterar um agendamento concluído')
            else:
                agendamento_auxiliar = self.inserir_novo_agendamento()
                agendamento_selecionado.paciente = agendamento_auxiliar.paciente
                agendamento_selecionado.enfermeiro = agendamento_auxiliar.enfermeiro
                agendamento_selecionado.data_hora = agendamento_auxiliar.data_hora
                agendamento_selecionado.vacina = agendamento_auxiliar.vacina
                self.__agendamento_DAO.remove(agendamento_auxiliar.codigo)
                self.__agendamento_DAO.update()

    def excluir_agendamento(self):
        if len(self.__agendamento_DAO.get_all()) == 0:
            self.__tela_agendamento.mensagem('Não é possível excluir nenhum agendamento, pois não há nenhum agendamento cadastrado no posto.')
        else:
            codigo = self.__tela_agendamento.seleciona_agendamento(self.lista_todos_agendamentos())
            self.__agendamento_DAO.remove(codigo)
    
    def lista_agendamentos(self):
        opcoes_de_lista = {1: self.mostra_agendamentos_em_aberto, 2: self.mostra_agendamentos_concluidos, 3: self.mostra_todos_agendamentos}
        while True:
            valor_lido = self.__tela_agendamento.selecionar_lista_agendamentos()
            if valor_lido == 0 or valor_lido == None:
                break
            else:
                opcoes_de_lista[valor_lido]()

    def lista_todos_agendamentos(self):
        lista_agendamentos=[]
        for agendamento in self.__agendamento_DAO.get_all():
            dados_agendamentos = {"paciente": agendamento.paciente.nome, "enfermeiro":agendamento.enfermeiro.nome,"vacina":agendamento.vacina.tipo, "data_hora":agendamento.data_hora,"codigo":agendamento.codigo,"conclusao":agendamento.conclusao}
            #dados_agendamentos = {"paciente": agendamento.paciente, "enfermeiro":agendamento.enfermeiro,"vacina":agendamento.vacina.tipo, "data_hora":agendamento.data_hora,"codigo":agendamento.codigo,"conclusao":agendamento.conclusao}
            #dados_agendamentos = {"vacina":agendamento.vacina.tipo, "data_hora":agendamento.data_hora,"codigo":agendamento.codigo,"conclusao":agendamento.conclusao}
            lista_agendamentos.append(dados_agendamentos)
        return lista_agendamentos

    def lista_agendamentos_em_aberto(self):
        lista_agendamentos_em_aberto=[]
        for agendamento in self.__agendamento_DAO.get_all():
            if agendamento.conclusao == False:
                dados_agendamentos = {"paciente": agendamento.paciente.nome, "enfermeiro":agendamento.enfermeiro.nome,"vacina":agendamento.vacina.tipo, "data_hora":agendamento.data_hora,"codigo":agendamento.codigo,"conclusao":agendamento.conclusao}
                lista_agendamentos_em_aberto.append(dados_agendamentos)
        return lista_agendamentos_em_aberto

    def lista_agendamentos_concluidos(self):
        lista_agendamentos_concluidos=[]
        for agendamento in self.__agendamento_DAO.get_all():
            if agendamento.conclusao == True:
                dados_agendamentos = {"paciente": agendamento.paciente.nome, "enfermeiro":agendamento.enfermeiro.nome,"vacina":agendamento.vacina.tipo, "data_hora":agendamento.data_hora,"codigo":agendamento.codigo,"conclusao":agendamento.conclusao}
                lista_agendamentos_em_concluidos.append(dados_agendamentos)
    
    def mostra_agendamentos_concluidos(self):
        self.__tela_agendamento.listar_agendamentos(self.lista_agendamentos_concluidos())

    def mostra_agendamentos_em_aberto(self):
        self.__tela_agendamento.listar_agendamentos(self.lista_agendamentos_em_aberto())

    def mostra_todos_agendamentos(self):
        self.__tela_agendamento.listar_agendamentos(self.lista_todos_agendamentos())
    
    def concluir_agendamento(self):
        try:
            if len(self.lista_agendamentos_em_aberto()) > 0:
                codigo = self.__tela_agendamento.seleciona_agendamento(self.lista_agendamentos_em_aberto())
                agendamento = self.__agendamento_DAO.get(codigo)
                agendamento.conclusao = True
                codigo_vacina = agendamento.vacina.codigo
                self.__controlador_vacina.remove_dose_aplicada_do_estoque(codigo_vacina)
                codigo_paciente = agendamento.paciente.codigo
                self.__controlador_paciente.vacina_paciente(codigo_paciente)
                self.__agendamento_DAO.update()
            else:
                raise ListaVaziaException('agendamento')
        except ListaVaziaException as mensagem:
            self.__tela_agendamento.mensagem(mensagem)

    def inicia_tela_agendamento(self):
        lista_opcoes={1: self.inserir_novo_agendamento,2: self.excluir_agendamento, 3: self.edita_agendamento, 4: self.lista_agendamentos, 5: self.concluir_agendamento}
        while True:
            valor_lido = self.__tela_agendamento.opcoes_agendamento()
            if valor_lido == 0 or valor_lido == None:
                break
            else:
                lista_opcoes[valor_lido]()
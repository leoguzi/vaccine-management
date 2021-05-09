import os
import sys
sys.path.append(".")
from model.vacina import Vacina
from view.tela_vacina import TelaVacina
from model.vacina_dao import VacinaDAO
from controller.excecoes import ListaVaziaException
from controller.excecoes import CampoEmBrancoException
from controller.excecoes import NenhumSelecionadoException

class ControladorVacina:
    def __init__(self, tela_vacina: TelaVacina):
        self.__tela_vacina = tela_vacina
        self.__vacina_DAO = VacinaDAO()
        if len(self.__vacina_DAO.get_all()) == 0:
            self.__gera_codigo = int(400) #codigo das vacinas começa em 400
        else:
            codigo = 400
            for vacina in self.__vacina_DAO.get_all(): #encontra o maior codigo que já foi usado.
                if vacina.codigo > codigo:
                    codigo = vacina.codigo
            self.__gera_codigo = codigo + 1 

    def inclui_vacina(self):
        while True: #obtem todos os dados ou None
            try:
                dados = self.__tela_vacina.ler_dados()
                if dados == None:
                    break
                if dados['tipo'] == '' or dados['fabricante'] == '' or dados['quantidade'] == '':
                    raise CampoEmBrancoException #exceção para quando não digitar algum dos dados e clicar em cadastrar
                else:
                    try:
                        int(dados['quantidade'])
                        break
                    except ValueError:
                        self.__tela_vacina.mensagem('A quantidade deve ser um numero inteiro!') 
            except CampoEmBrancoException as mensagem:
                self.__tela_vacina.mensagem(mensagem)
        if dados is not None:
            for vacina in self.__vacina_DAO.get_all():
                if (dados['tipo'] == vacina.tipo and dados['fabricante'] == vacina.fabricante):
                    vacina.quantidade += dados['quantidade']
            self.__vacina_DAO.add(Vacina(dados['tipo'], dados['fabricante'], int(dados['quantidade']), self.__gera_codigo))
            self.__gera_codigo += 1 #incrementa o codigo

    def remove_doses_vacina(self):
        try:
            codigo = self.__tela_vacina.selecionar_vacina(self.lista_vacinas())
            if codigo == '':
                raise NenhumSelecionadoException('vacina')
            else:
                vacina = self.encontra_vacina_por_codigo(codigo)
                quantidade_inicial = int(vacina.quantidade)
                mensagem = 'Vacina encontrada. \n Existem ' + str(quantidade_inicial) + ' doses desta vacina no estoque. Informe a quantidade que deseja remover'
                self.__tela_vacina.mensagem(mensagem)
                quantidade = int(self.__tela_vacina.ler_quantidade())
                while quantidade_inicial < quantidade:
                    mensagem = 'Informe uma quantidade igual ou inferior a ' + str(quantidade_inicial)
                    self.__tela_vacina.mensagem(mensagem)
                    quantidade = self.__tela_vacina.ler_quantidade()
                vacina.quantidade -= quantidade
                if vacina.quantidade == 0: 
                    self.__vacina_DAO.remove(vacina.codigo)
                else:
                    self.__vacina_DAO.update()
        except NenhumSelecionadoException as mensagem:
            self.__tela_vacina.mensagem(mensagem)

    def lista_vacinas(self): #retorna uma lista de dicionarios contendo as informações das vacinas ou None caso não exista nenhum cadastrado.
        try: 
            if len(self.__vacina_DAO.get_all()) > 0:
                lista_vacinas = []
                for vacina in self.__vacina_DAO.get_all():
                    lista_vacinas.append({'codigo': vacina.codigo, 'tipo': vacina.tipo, 'fabricante': vacina.fabricante, 'quantidade': vacina.quantidade})
            else:
                lista_vacinas = None
                raise ListaVaziaException('vacina') #exceção para lista vazia 
        except ListaVaziaException as mensagem:
            self.__tela_vacina.mensagem(mensagem)
        return lista_vacinas

    def retorna_estoque(self): #função utilizada para retornar todo o estoque de vacinas do posto
        self.__tela_vacina.listar_vacinas(self.lista_vacinas())

    
    def remove_dose_aplicada_do_estoque(self,codigo): #função utilizada para remover uma dose do estoque sempre que um agendamento eh concluído
        vacina = self.encontra_vacina_por_codigo(codigo)
        vacina.quantidade -= 1
        if vacina.quantidade == 0:
            self.__vacina_DAO.remove(vacina.codigo)
        else:
            self.__vacina_DAO.update()
    
    def encontra_vacina_por_codigo(self, codigo):
        vacina_selecionada = None
        for vacina in self.__vacina_DAO.get_all():
            if vacina.codigo == codigo:
                vacina_selecionada = vacina
        return vacina_selecionada
         
    def consulta_dose_estoque(self,codigo, n_doses_necessarias): #função utilizada para consultar o estoque de uma vacina específica, para saber se é possivel agendar um atendimento de primeira ou segunda dose
        vacina = self.encontra_vacina_por_codigo(codigo)
        n_estoque = vacina.quantidade
        if n_estoque >= n_doses_necessarias:
            return True
        else:
            return False

    def inicia_tela_vacina(self):
        lista_opcoes = {1:self.inclui_vacina,2:self.remove_doses_vacina, 3:self.retorna_estoque}
        while True:
            valor_lido = self.__tela_vacina.menu_vacina()
            if valor_lido == 0 or valor_lido == None:
                break
            else:
                lista_opcoes[valor_lido]()







    

    




        
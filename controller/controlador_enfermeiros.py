import sys
sys.path.append(".")
from model.enfermeiro import Enfermeiro
from model.enfermeiro_dao import EnfermeiroDAO
from view.tela_enfermeiro import TelaEnfermeiros
from controller.excecoes import ListaVaziaException
from controller.excecoes import CampoEmBrancoException
from controller.excecoes import NenhumSelecionadoException

class ControladorEnfermeiros():

    def __init__(self, tela_enfermeiros: TelaEnfermeiros):
        self.__tela_enfermeiros = tela_enfermeiros
        self.__enfermeiro_DAO = EnfermeiroDAO()
        if len(self.__enfermeiro_DAO.get_all()) == 0:
            self.__gera_codigo = int(100) #codigo dos enfermeiros começa em 100
        else:
            codigo = 100
            for enfermeiro in self.__enfermeiro_DAO.get_all(): #encontra o maior codigo que já foi usado.
                if enfermeiro.codigo > codigo:
                    codigo = enfermeiro.codigo
            self.__gera_codigo = codigo + 1 

    def adiciona_enfermeiro(self):
        while True:
            try:
                nome = self.__tela_enfermeiros.le_nome() #obtem um nome ou none caso a janela seja fechada
                if nome == '':
                    raise CampoEmBrancoException #exeção para campo em branco aqui
                else:
                    break
            except CampoEmBrancoException as mensagem:
                self.__tela_enfermeiros.mensagem(mensagem)   
        if nome is not None:
            self.__enfermeiro_DAO.add(Enfermeiro(nome, self.__gera_codigo)) 
            self.__gera_codigo += 1 #incrementa o codigo
              
    def remove_enfermeiro(self):
        while True: #obtem o dicionario do enfermeiro ou None
            try:
                enfermeiro_selecionado = self.__tela_enfermeiros.combo_box_enfermeiros(self.lista_enfermeiros())
                if enfermeiro_selecionado == '':
                    raise NenhumSelecionadoException('enfermeiro') # exceção para "clicou em selecionar sem selecionar" aqui
                else: 
                    break
            except NenhumSelecionadoException as mensagem:
                self.__tela_enfermeiros.mensagem(mensagem)
        if enfermeiro_selecionado is not None:
            self.__enfermeiro_DAO.remove(enfermeiro_selecionado['codigo'])

    def edita_enfermeiro(self):
        while True: #obtem o dicionario do enfermeiro ou None
            try:
                enfermeiro_selecionado = self.__tela_enfermeiros.combo_box_enfermeiros(self.lista_enfermeiros())
                if enfermeiro_selecionado == '':
                    raise NenhumSelecionadoException('enfermeiro') # exceção para "clicou em selecionar sem selecionar" aqui
                else: 
                    break
            except NenhumSelecionadoException as mensagem:
                self.__tela_enfermeiros.mensagem(mensagem)
        if enfermeiro_selecionado is not None: #se o usuario fechar a tela ou clicar em voltar antes de selecionar o enfermeiro, nem tenta ler o nome.
            while True: #obtem o novo nome ou None
                try:
                    novo_nome = self.__tela_enfermeiros.le_nome(enfermeiro_selecionado['nome'])
                    if novo_nome == '':
                        raise CampoEmBrancoException #exceção para "clicou em cadastrar sem digitar nada" aqui
                    else:
                        break
                except CampoEmBrancoException as mensagem:
                    self.__tela_enfermeiros.mensagem(mensagem)
        if enfermeiro_selecionado is not None and novo_nome is not None:
            for enfermeiro in self.__enfermeiro_DAO.get_all():
                if enfermeiro.codigo == enfermeiro_selecionado['codigo']:
                    enfermeiro.nome = novo_nome
                    self.__enfermeiro_DAO.update()

    def lista_enfermeiros(self): #retorna uma lista de dicionarios contendo as informações dos enfermeiros ou None cado não exista nenhum cadastrado.
        try: 
            if len(self.__enfermeiro_DAO.get_all()) > 0:
                lista_enfermeiros = []
                for enfermeiro in self.__enfermeiro_DAO.get_all():
                    lista_enfermeiros.append({"codigo": enfermeiro.codigo, "nome": enfermeiro.nome})
            else:
                lista_enfermeiros = None
                raise ListaVaziaException('enfermeiro') #exceção para lista vazia 
        except ListaVaziaException as mensagem:
            self.__tela_enfermeiros.mensagem(mensagem)
        return lista_enfermeiros 

    def encontra_enfermeiro_por_codigo(self, codigo):
        enfermeiro_selecionado = None
        for enfermeiro in self.__enfermeiro_DAO.get_all():
            if enfermeiro.codigo == codigo:
                enfermeiro_selecionado = enfermeiro
        return enfermeiro_selecionado

  
    def mostra_enfermeiros(self): #abre a tela que lista os enfermeiros

        self.__tela_enfermeiros.mostra_enfermeiros(self.lista_enfermeiros())

    def abre_tela_enfermeiros(self):
        lista_opcoes = {1: self.adiciona_enfermeiro, 2: self.remove_enfermeiro, 3: self.edita_enfermeiro, 4: self.mostra_enfermeiros}
        while True:
            valor_lido = self.__tela_enfermeiros.opcoes_enfermeiro()
            if valor_lido == 0 or valor_lido == None:
                break
            else:
                lista_opcoes[valor_lido]()
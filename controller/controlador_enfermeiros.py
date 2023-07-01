import sys
sys.path.append(".")

from model.facade import Facade

from controller.excecoes import ListaVaziaException
from controller.excecoes import CampoEmBrancoException
from controller.excecoes import NenhumSelecionadoException

class ControladorEnfermeiros():

    def __init__(self, tela_enfermeiros: Facade.get_instaciar_tela_enfermeiro()):
        self.__facade = Facade()

        if len(self.__facade.pega_tudo_enfermeiro()) == 0:
            self.__gera_codigo = int(100) #codigo dos enfermeiros começa em 100
        else:
            codigo = 100
            for enfermeiro in self.__facade.pega_tudo_enfermeiro(): #encontra o maior codigo que já foi usado.
                if enfermeiro.codigo > codigo:
                    codigo = enfermeiro.codigo
            self.__gera_codigo = codigo + 1

    def adiciona_enfermeiro(self):
        while True:
            try:
                nome = self.__facade.le_nome_tela() #obtem um nome ou none caso a janela seja fechada
                if nome == '':
                    raise CampoEmBrancoException #exeção para campo em branco aqui
                else:
                    break
            except CampoEmBrancoException as mensagem:
                self.__facade.mensagem_tela_enfermeiro(mensagem)   
        if nome is not None:
            self.__facade.adiciona_enfermeiro(self.__facade.get_instaciar_enfermeiro(nome, self.__gera_codigo)) 
            self.__gera_codigo += 1 #incrementa o codigo
              
    def remove_enfermeiro(self):
        enfermeiro_selecionado = self.seleciona_enfermeiro()
        if enfermeiro_selecionado is not None:
            self.__facade.remove_enfermeiro(enfermeiro_selecionado)
            self.__facade.mensagem_tela_enfermeiro('Excluido!')

    def edita_enfermeiro(self):
        enfermeiro = self.__facade.pega_enfermeiro(self.seleciona_enfermeiro())
        if enfermeiro is not None: #se o usuario fechar a tela ou clicar em voltar antes de selecionar o enfermeiro, nem tenta ler o nome.
            while True: #obtem o novo nome ou None
                try:
                    novo_nome = self.__facade.le_nome_tela(enfermeiro.nome)
                    if novo_nome == '':
                        raise CampoEmBrancoException #exceção para "clicou em cadastrar sem digitar nada" aqui
                    else:
                        break
                except CampoEmBrancoException as mensagem:
                    self.__facade.mensagem_tela_enfermeiro(mensagem)
        if enfermeiro is not None and novo_nome is not None:
            enfermeiro.nome = novo_nome
            self.__facade.atualiza_enfermeiro()

    def lista_enfermeiros(self): #retorna uma lista de dicionarios contendo as informações dos enfermeiros ou None cado não exista nenhum cadastrado.
        try: 
            if len(self.__facade.pega_tudo_enfermeiro()) > 0:
                lista_enfermeiros = []
                for enfermeiro in self.__facade.pega_tudo_enfermeiro():
                    lista_enfermeiros.append({"codigo": enfermeiro.codigo, "nome": enfermeiro.nome})
            else:
                lista_enfermeiros = None
                raise ListaVaziaException('enfermeiro') #exceção para lista vazia 
        except ListaVaziaException as mensagem:
            self.__facade.mensagem_tela_enfermeiro(mensagem)
        return lista_enfermeiros 

    def encontra_enfermeiro_por_codigo(self, codigo):
        return self.__facade.pega_enfermeiro(codigo)
  
    def mostra_enfermeiros(self): #abre a tela que lista os enfermeiros
        self.__facade.mostra_enfermeiro_tela(self.lista_enfermeiros())

    def seleciona_enfermeiro(self): #obtem o codigo do enfermeiro ou None
        while True: 
            try:
                enfermeiro_selecionado = self.__facade.combo_box_enfermeiros_tela(self.lista_enfermeiros())
                if enfermeiro_selecionado == '':
                    raise NenhumSelecionadoException('enfermeiro') # exceção para "clicou em selecionar sem selecionar" aqui
                else: 
                    break
            except NenhumSelecionadoException as mensagem:
                self.__facade.mensagem_tela_enfermeiro(mensagem)
        return enfermeiro_selecionado

    def abre_tela_enfermeiros(self):
        lista_opcoes = {1: self.adiciona_enfermeiro, 2: self.remove_enfermeiro, 3: self.edita_enfermeiro, 4: self.mostra_enfermeiros}
        while True:
            valor_lido = self.__facade.opcoes_enfermeiro_tela()
            if valor_lido == 0 or valor_lido == None:
                break
            else:
                lista_opcoes[valor_lido]()
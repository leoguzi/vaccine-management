import sys
sys.path.append(".")
from model.enfermeiro import Enfermeiro
from model.enfermeiro_dao import EnfermeiroDAO
from view.tela_enfermeiro import TelaEnfermeiros

class ControladorEnfermeiros():

    def __init__(self, tela_enfermeiros: TelaEnfermeiros):
        self.__tela_enfermeiros = tela_enfermeiros
        self.__enfermeiro_DAO = EnfermeiroDAO()
        self.__gera_codigo = int(100)

    def adiciona_enfermeiro(self):
        while True: # obtem o nome ou None
            try:
                nome = self.__tela_enfermeiros.le_nome()
                if nome == '': 
                    raise Exception #implementar uma exeção para quando não digitar nada e clicar em cadastrar
                else:
                    break
            except:
                self.__tela_enfermeiros.mensagem("Enfermeiro não cadastrado. Digite um nome...")
        if nome is not None:
            self.__enfermeiro_DAO.add(Enfermeiro(nome, self.__gera_codigo)) 
            self.__gera_codigo += 1 #incrementa o codigo
              
    def remove_enfermeiro(self):
        while True: #obtem o dicionario do enfermeiro ou None
            try:
                enfermeiro_selecionado = self.__tela_enfermeiros.combo_box_enfermeiros(self.lista_enfermeiros())
                if enfermeiro_selecionado == '':
                    raise Exeption # exceção para "clicou em selecionar sem selecionar" aqui
                else: 
                    break
            except:
                self.__tela_enfermeiros.mensagem("Selecione um enfermeiro")
        if enfermeiro_selecionado is not None:
            self.__enfermeiro_DAO.remove(enfermeiro_selecionado['codigo'])

    def edita_enfermeiro(self):
        while True: #obtem o dicionario do enfermeiro ou None
            try:
                enfermeiro_selecionado = self.__tela_enfermeiros.combo_box_enfermeiros(self.lista_enfermeiros())
                if enfermeiro_selecionado == '':
                    raise Exeption # exceção para "clicou em selecionar sem selecionar" aqui
                else: 
                    break
            except:
                self.__tela_enfermeiros.mensagem("Selecione um enfermeiro")
        if enfermeiro_selecionado is not None: #se o usuario fechar a tela ou clicar em voltar antes de selecionar o enfermeiro, nem tenta ler o nome.
            while True: #obtem o novo nome ou None
                try:
                    novo_nome = self.__tela_enfermeiros.le_nome(enfermeiro_selecionado['nome'])
                    if novo_nome == '':
                        raise Exeption #exceção para "clicou em cadastrar sem digitar nada" aqui
                    else:
                        break
                except:
                    self.__tela_enfermeiros.mensagem("Digite um nome!")
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
                raise Exception #criar uma exeção para lista vazia 
        except: 
           self.__tela_enfermeiros.mensagem("Nenhum enfermeiro cadastrado no posto!")
        return lista_enfermeiros 

    def encontra_enfermeiro_por_codigo(self, codigo): #provavelmente não vai mais ser usada
        enfermeiro = None
        while enfermeiro is None:
            for i in range(len(self.__enfermeiros)):
                if self.__enfermeiros[i].codigo == codigo:
                    enfermeiro = self.__enfermeiros[i]
                    return enfermeiro
            print("\nEnfermeiro não encontrado. Informe um código válido.\n")
            codigo = self.__tela_enfermeiros.le_codigo()

    def retorna_codigo_lido(self): #provavelmente não vai mais ser usada
        codigo = self.__tela_enfermeiros.le_codigo()
        return codigo
    
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
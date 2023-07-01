import sys
sys.path.append(".")

from model.enfermeiro import Enfermeiro
from model.enfermeiro_dao import EnfermeiroDAO
from view.tela_enfermeiro import TelaEnfermeiros

class Facade:
    def __init__(self) -> None:
        self.__enfermeiro_dao = EnfermeiroDAO()
        self.__tela_enfermeiros = TelaEnfermeiros()

    def get_instaciar_enfermeiro(self, nome, codigo):
        return Enfermeiro(nome, codigo)
    
    def get_instaciar_tela_enfermeiro():
        return TelaEnfermeiros()
    
    def adiciona_enfermeiro(self, enfermeiro: Enfermeiro):
        self.__enfermeiro_dao.add(enfermeiro)
    
    def pega_enfermeiro(self, key:int):
        return self.__enfermeiro_dao.get(key)
    
    def remove_enfermeiro(self, key:int):
        return self.__enfermeiro_dao.remove(key)

    def atualiza_enfermeiro(self):
        self.__enfermeiro_dao.update()

    def pega_tudo_enfermeiro(self):
        return self.__enfermeiro_dao.get_all()
    ##### METODOS de TelaEnfermeiro 
    def opcoes_enfermeiro_tela(self):
        return self.__tela_enfermeiros.opcoes_enfermeiro()
    
    def le_nome_tela(self, nome_atual = None):
        return self.__tela_enfermeiros.le_nome(nome_atual)
    
    def mostra_enfermeiro_tela(self, lista_enfermeiros):
        self.__tela_enfermeiros.mostra_enfermeiros(lista_enfermeiros)
    
    def combo_box_enfermeiros_tela(self, lista_enfermeiros):
        return self.__tela_enfermeiros.combo_box_enfermeiros(lista_enfermeiros)
    
    def mensagem_tela_enfermeiro(self, mensagem: str):
        self.__tela_enfermeiros.mensagem(mensagem)
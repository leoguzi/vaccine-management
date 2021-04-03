from model.pessoa import Pessoa
from model.agendamento import Agendamento

class Enfermeiro(Pessoa):
    
    def __init__(self, nome: str, codigo: int):
        super().__init__(nome, codigo)
        self.__atendimentos = []

    def inclui_atendimento(self, atendimento: Agendamento):
        if isinstance (atendimento, Agendamento):
            self.__atendimentos.append(atendimento)
        else:
            raise Exception
    
    def remove_atendimento(self, atendimento: Agendamento):
        if isinstance (atendimento, Agendamento):
            self.__atendimentos.remove(atendimento)
        else:
            raise Exception

    def retorna_atendimentos(self):
        return self.__atendimentos

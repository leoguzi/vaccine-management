from model.dao import DAO
from model.agendamento import Agendamento

#cada entidade terá uma classe dessa, implementação bem simples.
class AgendamentoDAO(DAO):
    def __init__(self):
        super().__init__('agendamentos.pkl')

    def add(self, agendamento: Agendamento):
        if((agendamento is not None) and isinstance(agendamento, Agendamento)):
            super().add(agendamento.codigo, agendamento)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
    
    def update(self):
        super().update_file()
from model.dao import DAO
from model.vacina import Vacina

#cada entidade terá uma classe dessa, implementação bem simples.
class VacinaDAO(DAO):
    def __init__(self):
        super().__init__('vacinas.pkl')

    def add(self, vacina:Vacina):
        if((vacina is not None) and isinstance(vacina, Vacina) and isinstance(vacina.quantidade, int)):
            super().add(vacina.codigo, vacina)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
    
    def update(self):
        super().update_file()
from model.dao import DAO
from model.enfermeiro import Enfermeiro

#cada entidade terá uma classe dessa, implementação bem simples.
class EnfermeiroDAO(DAO):
    def __init__(self):
        super().__init__('enfermeiros.pkl')

    def add(self, enfermeiro: Enfermeiro):
        if((enfermeiro is not None) and isinstance(enfermeiro, Enfermeiro) and isinstance(enfermeiro.codigo, int)):
            super().add(enfermeiro.codigo, enfermeiro)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
    
    def update(self):
        super().update_file()
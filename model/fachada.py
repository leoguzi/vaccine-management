import sys
sys.path.append(".")

from model.enfermeiro_dao import EnfermeiroDAO
from model.paciente_dao import PacienteDAO
from model.vacina_dao import VacinaDAO
from model.enfermeiro import Enfermeiro
from model.paciente import Paciente


class Fachada:
    def __init__(self):
        self.enfermeiro_dao = EnfermeiroDAO()
        self.paciente_dao = PacienteDAO()
        self.vacina_dao = VacinaDAO()
    
    def adiciona_enfermeiro(self, enfermeiro: Enfermeiro):
        self.enfermeiro_dao.add(self, enfermeiro)
    
    def pega_enfermeiro(self, key:int):
        return self.enfermeiro_dao.get(self, key)
    
    def remove_enfermeiro(self, key:int):
        return self.enfermeiro_dao.remove(self, key)

    def atualiza_enfermeiro(self):
        self.enfermeiro_dao.update(self)

    # def adiciona_dao_enfermeiro(self, key, obj):
    #     self.enfermeiro_dao.add(key, obj)

    # def pega_dao_enfermeiro(self, key):     
    #     return self.enfermeiro_dao.get(key)
    
    # def remove_dao_enfermeiro(self, key):
    #     self.enfermeiro_dao.remove(key)

    def pega_tudo_enfermeiro(self):
        self.enfermeiro_dao.get_all()

    # def atualizar_dao_enfermeiro(self):
    #     self.enfermeiro_dao.update_file()
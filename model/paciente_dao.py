from model.dao import DAO
from model.paciente import Paciente

#cada entidade terá uma classe dessa, implementação bem simples.
class PacienteDAO(DAO):
    def __init__(self):
        super().__init__('pacientes.pkl')

    def add(self, paciente: Paciente):
        if((paciente is not None) and isinstance(paciente, Paciente) and isinstance(paciente.codigo, int)):
            super().add(paciente.codigo, paciente)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
    
    def update(self):
        super().update_file()
import sys
sys.path.append(".")

from model.enfermeiro import Enfermeiro
from model.paciente import Paciente
from model.vacina import Vacina

class Agendamento:
    def __init__(self, paciente: Paciente, enfermeiro: Enfermeiro, vacina: Vacina, data_hora: str, conclusao: Boolean=False):
        if isinstance(paciente, Paciente):
            self.__paciente = paciente
        if isinstance(enfermeiro, Enfermeiro):
            self.__enfermeiro = enfermeiro
        if isinstance(vacina, Vacina):
            self.__vacina = vacina
        self.__data_hora = data_hora
        self.__conclusao = conclusao
    
    @property
    def paciente(self):
        return self.__paciente
    @paciente.setter
    def paciente(self,paciente):
        if isinstance(paciente,Paciente):
            self.__paciente = paciente
    
    @property
    def enfermeiro(self):
        return self.__enfermeiro
    @enfermeiro.setter
    def enfermeiro(self,enfermeiro):
        if isinstance(enfermeiro,Enfermeiro):
            self.__enfermeiro = enfermeiro
    
    @property
    def vacina(self):
        return self.__vacina
    @vacina.setter
    def vacina(self,vacina):
        if isinstance(vacina,Vacina):
            self.__vacina = vacina
    
    @property
    def data_hora(self):
        return self.__data_hora
    @data_hora.setter
    def data_hora(self,data_hora):
        self.__data_hora = data_hora
    
    @property
    def conclusao(self):
        return self.__conclusao
    @conclusao.setter
    def conclusao(self,conclusao):
        self.__conclusao = conclusao
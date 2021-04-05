from model.pessoa import Pessoa

class Paciente(Pessoa):

    def __init__(self, nome: str, idade: int, codigo: int):
        super().__init__(nome, codigo)
        if isinstance(idade, int) and 0<idade<=150:
            self.__idade = idade
        else:
            raise Exception
        self.__numero_doses = 0

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade: int):
        if isinstance(idade, int):
            self.__idade = idade
        else:
            raise Exception

    @property
    def numero_doses(self):
        return self.__numero_doses
    
    @numero_doses.setter
    def numero_doses(self,numero_doses: int):
        self.__numero_doses = numero_doses
    



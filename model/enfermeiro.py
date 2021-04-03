from model.pessoa import Pessoa

class Enfermeiro(Pessoa):
    
    def __init__(self, nome: str, codigo: int):
        super().__init__(nome, codigo)

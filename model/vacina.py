class Vacina:
    def __init__(self, tipo:str, fabricante: str, quantidade: int):
        self.__tipo = tipo
        self.__quantidade = quantidade
        self.__fabricante = fabricante

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo:str):
        self.__tipo = tipo
    
    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        self.__quantidade = quantidade
    
    @property
    def fabricante(self):
        return self.__fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante:str):
        self.__fabricante = fabricante
    
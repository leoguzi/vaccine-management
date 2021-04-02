from abc import ABC, abstractmethod

class Pessoa(ABC):

    @abstractmethod
    def __init__(self, nome: str, codigo: int):
        if isinstance(nome, str) and isinstance(codigo, int):
            self.__nome = nome
            self.__codigo = codigo
        else:
            raise Exception
        

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise Exception
    @property
    def codigo(self):
        return self.__codigo


import pickle
from abc import ABC, abstractmethod

class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {} #é aqui que vai ficar a lista que estava no controlador. Nesse exemplo estamos usando um dicionario
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource,'rb'))

    #esse método precisa chamar o self.__dump()
    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()  #atualiza o arquivo depois de add novo amigo

    def get(self, key):
        return self.__cache[key]
       
    # esse método precisa chamar o self.__dump()
    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump() #atualiza o arquivo depois de remover um objeto
        except KeyError:
            pass #implementar aqui o tratamento da exceção

    def get_all(self):
        return self.__cache.values()
    
    def update_file(self): # funçao para atualizar apos uma edição 
        self.__dump()
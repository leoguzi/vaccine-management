import os
import sys
sys.path.append(".")
from model.enfermeiro import Enfermeiro
from view.tela_enfermeiro import TelaEnfermeiros


class ControladorEnfermeiros():

    def __init__(self, tela_enfermeiros: TelaEnfermeiros):
        self.__tela_enfermeiros = tela_enfermeiros
        self.__enfermeiros = []
        self.__gera_codigo = int(100)
    
    @property
    def enfermeiros(self):
        return self.__enfermeiros

    def adiciona_enfermeiro(self):
        print("Digite o nome do enfermeiro:")
        nome = self.__tela_enfermeiros.le_nome()
        novo_enfermeiro = None
        try:
            novo_enfermeiro = Enfermeiro(nome, self.__gera_codigo)   
        except:
            print("Enfermeiro não cadastrado. Tente novamente!")
        finally:
            if novo_enfermeiro is not None:    
                self.__enfermeiros.append(novo_enfermeiro)
                self.__gera_codigo += 1
            return(novo_enfermeiro)

    def remove_enfermeiro(self):
        try:
            if len(self.__enfermeiros) > 0:
                print("\nInforme o código do enfermeiro que você deseja excluir.\n")
                self.lista_enfermeiros()
                codigo = self.__tela_enfermeiros.le_codigo()
                enfermeiro = self.encontra_enfermeiro_por_codigo(codigo)
                self.__enfermeiros.remove(enfermeiro)
                wait = input("Removido com sucesso! Pressione enter")
                os.system('cls' if os.name == 'nt' else 'clear')
            else: 
                raise Exception
        except:
            wait = input("Nenhum enfermeiro cadastrado no posto! Pressione enter...")
            os.system('cls' if os.name == 'nt' else 'clear')

    def edita_enfermeiro(self):
        try:
            if len(self.__enfermeiros) > 0:
                print("\nInforme o código do enfermeiro que você deseja alterar\n")
                self.lista_enfermeiros()
                codigo = self.__tela_enfermeiros.le_codigo()
                enfermeiro = self.encontra_enfermeiro_por_codigo(codigo)
                enfermeiro_auxiliar = self.adiciona_enfermeiro()
                enfermeiro.nome = enfermeiro_auxiliar.nome
                self.__enfermeiros.remove(enfermeiro_auxiliar)
            else:
                raise Exception
        except:
            wait = input("Nenhum enfermeiro cadastrado no posto! Pressione enter...")
            os.system('cls' if os.name == 'nt' else 'clear')

    def lista_enfermeiros(self):
        try: 
            if len(self.__enfermeiros) > 0:
                print("Lista de enfermeiros cadastrados: \n")
                for enfermeiro in self.__enfermeiros:
                    self.__tela_enfermeiros.mostra_enfermeiro({"codigo": enfermeiro.codigo, "nome": enfermeiro.nome})
            else:
                raise Exception
        except: 
            wait = input("Nenhum enfermeiro Cadastrado no posto! Pressione enter...")
            os.system('cls' if os.name == 'nt' else 'clear')
        

    def encontra_enfermeiro_por_codigo(self, codigo):
        enfermeiro = None
        while enfermeiro is None:
            for i in range(len(self.__enfermeiros)):
                if self.__enfermeiros[i].codigo == codigo:
                    enfermeiro = self.__enfermeiros[i]
                    return enfermeiro
            print("\nEnfermeiro não encontrado. Informe um código válido.\n")
            codigo = self.__tela_enfermeiros.le_codigo()

    def retorna_codigo_lido(self):
        codigo = self.__tela_enfermeiros.le_codigo()
        return codigo

    def abre_tela_enfermeiros(self):
        lista_opcoes = {1: self.adiciona_enfermeiro, 2: self.remove_enfermeiro, 3: self.edita_enfermeiro, 4: self.lista_enfermeiros}
        continua = True
        while continua:
            try:
                valor_lido = self.__tela_enfermeiros.opcoes_enfermeiro()
                if valor_lido >= 1 and valor_lido <= 4:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    lista_opcoes[valor_lido]()
                elif valor_lido == 0: 
                    continua = False
                    os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    raise ValueError
            except ValueError:
                wait = input("Opção Invalida! Digite um numero inteiro entre 0 e 5! Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')

        




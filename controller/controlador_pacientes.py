import sys
sys.path.append(".")

from model.paciente import Paciente
from view.tela_paciente import TelaPaciente

class ControladorPacientes():

    def __init__(self, tela_paciente: TelaPaciente):
        self.__tela_paciente = tela_paciente
        self.__pacientes = []
        self.__gera_codigo = int(200)

    def adiciona_paciente(self):
        print("Digite os dados do novo paciente: ")
        novo_paciente = None
        try:
            dados_paciente = self.__tela_paciente.le_dados()
            novo_paciente = Paciente(dados_paciente["nome"], dados_paciente["idade"], self.__gera_codigo)
        except: 
            print("Não criou o paciente! Dados Inválidos. O ano deve ser um número inteiro.")
        finally:
            if isinstance(novo_paciente, Paciente):
                self.__pacientes.append(novo_paciente)
                self.__gera_codigo +=1

    def remove_paciente(self):
        removeu = False
        self.lista_pacientes()
        codigo = self.__tela_paciente.le_codigo()
        try:
            for paciente in self.__pacientes:
                if paciente.codigo == codigo:
                    self.__pacientes.remove(paciente)
                    removeu = True 
            if not removeu:
                raise Exception
            else:
                print("Removido!")
        except: print("Paciente não encontrado!")

    def edita_paciente(self):
        indice = None
        self.lista_pacientes()
        codigo = self.__tela_paciente.le_codigo()
        for i in range(len(self.__pacientes)):
            if self.__pacientes[i].codigo == codigo:
                indice = i
        if indice is not None:
            print("Digite os novos dados:")
            dados_paciente = self.__tela_paciente.le_dados()
            self.__pacientes[indice].nome = dados_paciente["nome"]
            self.__pacientes[indice].idade = dados_paciente["idade"]

    def lista_pacientes(self):
        print("Lista de pacientes cadastrados: \n")
        for paciente in self.__pacientes:
            self.__tela_paciente.mostra_paciente({"codigo": paciente.codigo, "nome": paciente.nome, "idade": paciente.idade, "numero_doses": paciente.numero_doses})

    def retorna_menu_principal(self):
        pass
    
    def encontra_paciente_por_codigo(self, codigo):
        indice = None
        while indice is None:
            for i in range(len(self.__pacientes)):
                if self.__pacientes[i].codigo == codigo:
                    indice = i
            print("\nPaciente não encontrado.\n")
            codigo = self.__tela_paciente.le_codigo()
        return indice

    def abre_tela_pacientes(self):
        lista_opcoes = {1: self.adiciona_paciente, 2: self.remove_paciente, 3: self.edita_paciente, 4: self.lista_pacientes, 0: self.retorna_menu_principal}

        while True:
            try:
                valor_lido = self.__tela_paciente.opcoes_paciente()
                if valor_lido >=0 and valor_lido<=4:
                    lista_opcoes[valor_lido]()
                else:
                    raise ValueError
            except ValueError:
                print("\nOpção Invalida! Digite um numero inteiro entre 0 e 4!\n")
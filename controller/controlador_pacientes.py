import os
import sys
sys.path.append(".")
from model.paciente import Paciente
from view.tela_paciente import TelaPaciente

class ControladorPacientes():

    def __init__(self, tela_paciente: TelaPaciente):
        self.__tela_paciente = tela_paciente
        self.__pacientes = []
        self.__gera_codigo = int(200) #codigo dos pacientes começa em 200

    #Função que recebe um dicionario da tela_paciente com os dados lidos, tenta criar um paciente e adicionalo na lista
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
                self.__gera_codigo +=1 #incrementa o codigo para o proximo paciente

    #lista os pacientes, solicita ao usuário o código do paciente a ser removido e remove o paciente.
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

    #lista os pacientes, solicita o codigo do paciente a ser editado, solicita os novos dados, modifica na lista de pacientes.
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
    # lista todos os pacientes cadastrados. 
    def lista_pacientes(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Lista de pacientes cadastrados: \n")
        for paciente in self.__pacientes:
            self.__tela_paciente.mostra_paciente({"codigo": paciente.codigo, "nome": paciente.nome, "idade": paciente.idade, "numero_doses": paciente.numero_doses})
   
    

    #inicia o menu de controle de pacientes e chama a função referente ao valor lido pela tela.
    def abre_tela_pacientes(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        lista_opcoes = {1: self.adiciona_paciente, 2: self.remove_paciente, 3: self.edita_paciente, 4: self.lista_pacientes}
        continua = True
        while continua:
            try:
                valor_lido = self.__tela_paciente.opcoes_paciente()
                if valor_lido >=1 and valor_lido<=4:
                    lista_opcoes[valor_lido]()
                elif valor_lido == 0:
                    continua = False
                    os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    raise ValueError
            except ValueError:
                print("\nOpção Invalida! Digite um numero inteiro entre 0 e 4!\n")
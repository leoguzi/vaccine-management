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
    
    @property
    def pacientes(self):
        return self.__pacientes

    #Função que recebe um dicionario da tela_paciente com os dados lidos, tenta criar um paciente e adicionalo na lista
    def adiciona_paciente(self):
        print("Digite os dados do novo paciente: ")
        novo_paciente = None
        try:
            dados_paciente = self.__tela_paciente.le_dados()
            novo_paciente = Paciente(dados_paciente["nome"], dados_paciente["idade"], self.__gera_codigo)
            wait = input ("Cadastrado com sucesso! Pressione enter...")
            os.system('cls' if os.name == 'nt' else 'clear')
        except: 
            print("Não criou o paciente! Dados Inválidos. A idade deve ser um inteiro entre 0 e 150.")
        finally:
            if isinstance(novo_paciente, Paciente):
                self.__pacientes.append(novo_paciente)
                self.__gera_codigo +=1 #incrementa o codigo para o proximo paciente
            return(novo_paciente)

    #lista os pacientes, solicita ao usuário o código do paciente a ser removido e remove o paciente.
    def remove_paciente(self):
        try:
            if len(self.__pacientes) > 0:
                print("\nInforme o código do paciente que você deseja excluir.\n")
                self.lista_pacientes()
                codigo = self.__tela_paciente.le_codigo()
                paciente = self.encontra_paciente_por_codigo(codigo)
                self.__pacientes.remove(paciente)
                wait = input("Paciente removido com sucesso! Pressione enter...")
                os.system('cls' if os.name == 'nt' else 'clear')
            else: 
                raise Exception
        except:
            wait = input("Nenhum paciente cadastrado no posto! Pressione enter...")
            os.system('cls' if os.name == 'nt' else 'clear')
            
    #lista os pacientes, solicita o codigo do paciente a ser editado, solicita os novos dados, modifica na lista de pacientes.
    def edita_paciente(self):
        try:
            len(self.__pacientes) > 0
        except:
            print("\nNão é possível alterar um paciente, pois não há pacientes cadastrados neste posto.\n")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("\nInforme o código do paciente que você deseja alterar\n")
            self.lista_pacientes()
            codigo = self.__tela_paciente.le_codigo()
            paciente = self.encontra_paciente_por_codigo(codigo)
            paciente_auxiliar = self.adiciona_paciente()
            paciente.nome = paciente_auxiliar.nome
            paciente.idade = paciente_auxiliar.idade
            self.__pacientes.remove(paciente_auxiliar)


    # lista todos os pacientes cadastrados. 
    def lista_pacientes(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Lista de pacientes cadastrados: \n")
        for paciente in self.__pacientes:
            self.__tela_paciente.mostra_paciente({"codigo": paciente.codigo, "nome": paciente.nome, "idade": paciente.idade, "numero_doses": paciente.numero_doses})
   
    def encontra_paciente_por_codigo(self, codigo):
        paciente = None
        while paciente is None:
            for i in range(len(self.__pacientes)):
                if self.__pacientes[i].codigo == codigo:
                    paciente = self.__pacientes[i]
                    return paciente
            print("\nPaciente não encontrado.\n")
            codigo = self.__tela_paciente.le_codigo()
    
    def vacina_paciente(self,codigo):
        paciente_vacinado = self.encontra_paciente_por_codigo(codigo)
        try:
            paciente_vacinado.numero_doses <= 2
        except:
            print("\nNão é possível concluir este agendamento. O paciente já recebeu duas doses de vacina.\n")
        else:
            paciente_vacinado.numero_doses += 1
    
    def abre_tela_pacientes(self):
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
                wait = input("Opção Invalida! Digite um numero inteiro entre 0 e 4! Enter para Continuar")
                os.system('cls' if os.name == 'nt' else 'clear')
import sys
sys.path.append(".")

from view.tela_enfermeiro import TelaEnfermeiros

class ControladorEnfermeiros():

    def __init__(self, tela_enfermeiros: TelaEnfermeiros):
        self.__tela_enfermeiros = tela_enfermeiros
        self.__enfermeiros = []
        self.__gera_codigo = int(100)

    def setEnfermeiro():
        from model.enfermeiro import Enfermeiro
            
    def adiciona_enfermeiro(self):
        print("Digite o nome do novo enfermeiro:")
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

    def remove_enfermeiro(self):
        self.lista_enfermeiros()
        codigo = self.__tela_enfermeiros.le_codigo()
        removeu = False
        try:
            for enfermeiro in self.__enfermeiros:
                if enfermeiro.codigo == codigo:
                    self.__enfermeiros.remove(enfermeiro)
                    removeu = True 
            if not removeu:
                raise Exception
            else:
                print("Removido!")
        except: print("Enfermeiro não encontrado!")

    def edita_enfermeiro(self):
        indice = None
        self.lista_enfermeiros()
        codigo = self.__tela_enfermeiros.le_codigo()
        for i in range(len(self.__enfermeiros)):
            if self.__enfermeiros[i].codigo == codigo:
                indice = i
        if indice is not None:
            print("Digite o nome corrigido:")
            nome_enfermeiro = self.__tela_enfermeiros.le_nome()
            self.__enfermeiros[indice].nome = nome_enfermeiro

    def lista_enfermeiros(self):
        print("Lista de enfermeiros cadastrados: \n")
        for enfermeiro in self.__enfermeiros:
            atendimentos = enfermeiro.retorna_atendimentos()
            self.__tela_enfermeiros.mostra_enfermeiro({"codigo": enfermeiro.codigo, "nome": enfermeiro.nome, "n_atendimentos": len(atendimentos)})
    
    def lista_atendimentos_enfermeiro(self):
        pass

    def retorna_menu_principal(self):
        pass

    def encontra_enfermeiro_por_codigo(self, codigo):
        indice = None
        while indice is None:
            for i in range(len(self.__enfermeiros)):
                if self.__enfermeiros[i].codigo == codigo:
                    indice = i
            print("\nEnfermeiro não encontrado.\n")
            codigo = self.__tela_enfermeiros.le_codigo()
        return indice 

    def abre_tela_enfermeiros(self):
        lista_opcoes = {1: self.adiciona_enfermeiro, 2: self.remove_enfermeiro, 3: self.edita_enfermeiro, 4: self.lista_enfermeiros, 5: self.lista_atendimentos_enfermeiro, 0: self.retorna_menu_principal}
        while True:
            try:
                valor_lido = self.__tela_enfermeiros.opcoes_enfermeiro()
                if valor_lido >=0 and valor_lido<=4:
                    lista_opcoes[valor_lido]()
                else:
                    raise ValueError
            except ValueError:
                print("\nOpção Invalida! Digite um numero inteiro entre 0 e 5!\n")






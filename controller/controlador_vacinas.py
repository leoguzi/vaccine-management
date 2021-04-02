import sys
sys.path.append(".")

from model.vacina import Vacina
from view.tela_vacina import TelaVacina

class ControladorVacina(self, tela_vacina:TelaVacina):
    self.__tela_vacina = tela_vacina
    self.__lista_de_vacinas = []
    self.__gera_codigo_vacina = int(500)

    def inclui_vacina(self):
        print("Informe os dados da vacina que será incluída no estoque:")
        dados_vacina = self.__tela_vacina.le_dados()
        for i in range len(self.__lista_de_vacinas):
            if (dados_vacina["tipo"] == self.__lista_de_vacinas[i].tipo and dados_vacina["fabricante"] == self.__lista_de_vacinas[i].fabricante):
                self.__lista_de_vacinas[i].quantidade += dados_vacina["quantidade"]
                print('\nEsta vacina já está cadastrada. As novas doses foram adicionadas ao estoque. \n Agora, existem ',self.__lista_de_vacinas[i].quantidade,' doses desta vacina no sistema.')
            else:
                nova_vacina = Vacina(dados_vacina["tipo"],dados_vacina["fabricante"],dados_vacina["quantidade"], self.__gera_codigo_vacina)
                self.__gera_codigo_vacina += 1
                if isinstance(nova_vacina, Vacina):
                    self.__lista_de_vacinas.append(nova_vacina)
    def exclui_vacina(self):
        removeu = False
        self.retorna_estoque()
        codigo = self.__tela_vacina.le_codigo()
        indice = 0
        for i in range len(self.__lista_de_vacinas):
            if self.__lista_de_vacinas[i].codigo == codigo:
                indice = i
                quantidade_inicial = self.__lista_de_vacinas[indice].quantidade
                print("Vacina encontrada.\n Existem ",quantidade_inicial," doses desta vacina no estoque. Informe a quantidade que deseja remover")
                quantidade = self.__tela_vacina.le_quantidade()
                while quantidade_inicial <= quantidade:
                    print("Informe uma quantidade igual ou inferior a ",quantidade_inicial)
                    quantidade = self.__tela_vacina.le_quantidade()
                self.__lista_de_vacinas[i].quantidade -= quantidade
                removeu = True
        if removeu == True:
            print("Foram removidas ",quantidade," doses do estoque. \n Restam ",self.__lista_de_vacinas[indice].quantidade," doses desta vacina no estoque.")
        else:
            print("Não foi possível remover esta vacina. Informe um código válido.")
        if self.__lista_de_vacinas[indice].quantidade == 0:
            self.__lista_de_vacinas.remove(self.__lista_de_vacinas[indice])

    def retorna_estoque(self): #função utilizada para retornar todo o estoque de vacinas do posto
        print("Lista de vacinas constantes no estoque:")
        for vacina in self.__lista_de_vacinas:
            self.__tela_vacina.lista_vacinas({"tipo":vacina.tipo, "fabricante":vacina.fabricante,"quatidade":vacina.quantidade,"código":vacina.codigo})
    
    def remove_dose_aplicada_do_estoque(self, codigo): #função utilizada para remover uma dose do estoque sempre que um agendamento eh concluído
        for i in range (len(self.__lista_de_vacinas)):
            if codigo == self.__lista_de_vacinas[i].codigo:
                self.__lista_de_vacinas[i].quantidade -= 1
    
    def consulta_dose_estoque(self,codigo, n_doses): #função utilizada para consultar o estoque de uma vacina específica, para saber se é possivel agendar um atendimento de primeira ou segunda dose
        n_estoque = 0
        for i in range(len(self.__lista_de_vacinas)):
            if codigo == self.__lista_de_vacinas[i].codigo:
                n_estoque = self.__lista_de_vacinas[i].quantidade
        if n-estoque >= n_doses:
            return True
        else:
            return False
    
    




    

    




        
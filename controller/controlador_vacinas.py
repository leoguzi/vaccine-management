import os
import sys
sys.path.append(".")

from model.vacina import Vacina
from view.tela_vacina import TelaVacina

class ControladorVacina:
    def __init__(self, tela_vacina: TelaVacina):
        self.__tela_vacina = tela_vacina
        self.__lista_de_vacinas = []
        self.__gera_codigo_vacina = int(500)

    @property
    def lista_de_vacinas(self):
        return self.__lista_de_vacinas

    def inclui_vacina(self):
        nova_vacina = False
        print("Informe os dados da vacina que será incluída no estoque:")
        dados_vacina = self.__tela_vacina.ler_dados()
        for i in range (len(self.__lista_de_vacinas)):
            if (dados_vacina["tipo"] == self.__lista_de_vacinas[i].tipo and dados_vacina["fabricante"] == self.__lista_de_vacinas[i].fabricante):
                print("vacina_nova: ",type(dados_vacina["quantidade"]))
                print("vacina_antigo: ",type(self.__lista_de_vacinas[i].quantidade))
                self.__lista_de_vacinas[i].quantidade += dados_vacina["quantidade"]
                print('\nEsta vacina já está cadastrada. As novas doses foram adicionadas ao estoque. \n Agora, existem ',self.__lista_de_vacinas[i].quantidade,' doses desta vacina no sistema.')
                nova_vacina = True
        if nova_vacina == False:
            nova_vacina = Vacina(dados_vacina["tipo"],dados_vacina["fabricante"],dados_vacina["quantidade"], self.__gera_codigo_vacina)
            self.__gera_codigo_vacina += 1
            self.__lista_de_vacinas.append(nova_vacina)

    def remove_doses_vacina(self):
        removeu = False
        self.retorna_estoque()
        codigo = self.__tela_vacina.ler_codigo()
        vacina = self.encontra_vacina_por_codigo(codigo)
        quantidade_inicial = vacina.quantidade
        print("Vacina encontrada.\n Existem ",quantidade_inicial," doses desta vacina no estoque. Informe a quantidade que deseja remover")
        quantidade = self.__tela_vacina.ler_quantidade()
        while quantidade_inicial < quantidade:
            print("Informe uma quantidade igual ou inferior a ",quantidade_inicial)
            quantidade = self.__tela_vacina.ler_quantidade()
        vacina.quantidade -= quantidade
        print("Foram removidas ",quantidade," doses do estoque. \n Restam ",vacina.quantidade," doses desta vacina no estoque.")
        if vacina.quantidade == 0: 
            self.exclui_vacina(vacina)

    def retorna_estoque(self): #função utilizada para retornar todo o estoque de vacinas do posto
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Lista de vacinas constantes no estoque:")
        for vacina in self.__lista_de_vacinas:
            dados_vacina = {"tipo":vacina.tipo, "fabricante":vacina.fabricante,"quantidade":vacina.quantidade,"codigo":vacina.codigo}
            self.__tela_vacina.listar_vacinas(dados_vacina)
    
    def remove_dose_aplicada_do_estoque(codigo): #função utilizada para remover uma dose do estoque sempre que um agendamento eh concluído
        vacina = self.encontra_vacina_por_codigo(codigo)
        vacina.quantidade -= 1
        if vacina.quantidade == 0:
            self.exclui_vacina(vacina)
    
    def exclui_vacina(self,vacina):
        self.__lista_de_vacinas.remove(vacina)
        return(self.__lista_de_vacinas)

    def encontra_vacina_por_codigo(self, codigo):
        vacina = None
        while vacina is None:
            for i in range (len(self.__lista_de_vacinas)):
                if self.__lista_de_vacinas[i].codigo == codigo:
                    vacina = self.__lista_de_vacinas[i]
                    return vacina
            print("Vacina não encontrada. Informe um código válido.")
            codigo = self.__tela_vacina.ler_codigo()
         
    def consulta_dose_estoque(self,codigo, n_doses_necessarias): #função utilizada para consultar o estoque de uma vacina específica, para saber se é possivel agendar um atendimento de primeira ou segunda dose
        vacina = self.encontra_vacina_por_codigo(codigo)
        n_estoque = vacina.quantidade
        if n_estoque >= n_doses_necessarias:
            return True
        else:
            return False

    def inicia_tela_vacina(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        lista_opcoes = {1:self.inclui_vacina,2:self.remove_doses_vacina, 3:self.retorna_estoque}
        continua = True
        while continua:
            try:
                opcao_escolhida = self.__tela_vacina.menu_vacina()
                if 1 <= opcao_escolhida and opcao_escolhida <= 3:
                    lista_opcoes[opcao_escolhida]()
                elif opcao_escolhida == 0:
                    continua = False
                else:
                    raise ValueError
            except ValueError:
                print("\n Opção inválida, digite um número de 0 a 3.\n")






    

    




        
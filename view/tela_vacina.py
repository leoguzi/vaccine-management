import sys
sys.path.append(".")
import os

class TelaVacina():
    def __init__(self):
        self.__window = None
    def menu_vacina(self):
        print("============== CONTROLE DE VACINAS ==============")
        print("1 - Incluir doses no estoque")
        print("2 - Remover doses do estoque")
        print("3 - Consultar estoque de vacinas disponíveis")
        print("0 - Retornar ao menu principal")
        opcao = int(input("\nInforme a opção desejada: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        return(opcao)

    def ler_dados(self):
        print("\nInforme os dados solicitados abaixo\n")
        tipo = input("Tipo de Vacina: ")
        fabricante = input("Fabricante: ")
        quantidade = self.ler_quantidade()
        return{"tipo":tipo,"fabricante":fabricante,"quantidade":quantidade}
    
    def ler_codigo(self):
        codigo = int(input("Código: "))
        return codigo

    def ler_quantidade(self):
        quantidade = int(input("Quantidade de doses: "))
        try:
            quantidade > 0
        except:
            print("Não foi possível continuar a solicitação. A quantidade deve ser um número maior que zero.")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            return quantidade
    
    def listar_vacinas(self, dados_vacina):
        print("===============================")
        print("Codigo: ",dados_vacina["codigo"])
        print("Tipo: ",dados_vacina["tipo"])
        print("Fabricante: ",dados_vacina["fabricante"])
        print("Doses disponíveis: ",dados_vacina["quantidade"])
        print("===============================")




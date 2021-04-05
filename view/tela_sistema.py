import os
class TelaSistema():

    def mostra_menu_principal(self):
        print("===========SISTEMA DE GERENCIAMENTO DE VACINAÇÃO===========")
        print("1 - Controle de Enfermeiros ")
        print("2 - Controle de pacientes")
        print("3 - Controle de Agendamentos")
        print("4 - Controle de Vacinas")
        print("5 - Listar atendimentos por enfermeiro")
        print("6 - Relatório Gerencial")
        print("0 - Sair")

        opcao = int(input("\nDigite o numero da opção: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        return opcao
    def mostra_relatorio(self, relatorio):
        print("O numero de pacientes na fila é: ", relatorio["fila"])
        print("O numero de pacientes que já tomaram a primeira dose é: ", relatorio["total_primeira_dose"])
        print("O numero de pacientes que já tomaram a segunda dose é: ", relatorio["total_segunda_dose"])
        print("O numero total de doses aplicadas é : ", relatorio["total_doses"])
        whait = input("\nPressione enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
        
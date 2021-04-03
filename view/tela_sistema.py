class TelaSistema():

    def mostra_menu_principal(self):
        print("===========SISTEMA DE GERENCIAMENTO DE VACINAÇÃO===========")
        print("1 - Controle de Enfermeiros ")
        print("2 - Controle de pacientes")
        print("3 - Controle de Agendamentos")
        print("4 - Controle de Vacinas")
        print("5 - Relatório Gerencial")
        print("0 - Sair")

        opcao = int(input("\nDigite o numero da opção: "))
        print("\n")
        return opcao
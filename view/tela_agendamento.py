class TelaAgendamento:
   
    def opcoes_agendamento(self):
        print("\n========CONTROLE DE AGENDAMENTOS=========")
        print("1 - Cadastrar novo agendamento")
        print("2 - Excluir agendamento")
        print("3 - Editar agendamento")
        print("4 - Listar agendamentos")
        print("0 - Voltar ao menu principal")

        opcao = int(input("\nDigite o numero da opção: "))
        print("\n")
        return opcao
class TelaAgendamento():
   
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
    
    def ler_paciente(self):
        print("\n=========SELEÇÃO DE PACIENTE=========\n")
        paciente = int(input("Informe o código do paciente para agendar o atendimento: "))
        return paciente

    def ler_enfermeiro(self):
        print("\n=========SELEÇÃO DE ENFERMEIRO=========\n")
        enfermeiro = int(input("Informe o código do enfermeiro que realizará o atendimento: "))
        return enfermeiro

    def ler_data_hora(self):
        data_hora = input("Informa a data e horário do atendimento no formato: DD/MM/AA hh:mm: ")
        return data_hora
    
    
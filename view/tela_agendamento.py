class TelaAgendamento():
   
    def opcoes_agendamento(self):
        print("\n========CONTROLE DE AGENDAMENTOS=========")
        print("1 - Cadastrar novo agendamento")
        print("2 - Excluir agendamento")
        print("3 - Editar agendamento")
        print("4 - Listar agendamentos")
        print("5 - Concluir agendamento")
        print("0 - Voltar ao menu principal")

        opcao = int(input("\nDigite o numero da opção: "))
        print("\n")
        return opcao
    
    def ler_paciente(self):
        paciente = int(input("Informe o código do paciente para agendar o atendimento: "))
        return paciente

    def ler_enfermeiro(self):
        enfermeiro = int(input("Informe o código do enfermeiro que realizará o atendimento: "))
        return enfermeiro

    def ler_data_hora(self):
        data_hora = input("Informa a data e horário do atendimento no formato: DD/MM/AA hh:mm: ")
        return data_hora

    def ler_codigo(self):
        codigo = int(input("Código: "))
        return codigo
    
    def ler_vacina(self):
        codigo_vacina = int(input("Informe o código da vacina: "))
        return codigo_vacina
    
    def listar_agendamentos(self,dados_agendamentos):
        print("--------------------")
        print("Código: ",dados_agendamentos["codigo"])
        print("Paciente: ",dados_agendamentos["paciente"])
        print("Enfermeiro: ",dados_agendamentos["enfermeiro"])
        print("Vacina: ",dados_agendamentos["vacina"])
        print("Concluído (True or False): ",dados_agendamentos["conclusao"])
    
    def selecionar_lista_agendamentos(self):
        print("\nSelecione os agendamentos que você quer listar:\n")
        print("1 - Listar agendamentos em aberto")
        print("2 - Listar agendamentos concluídos")
        print("3 - Listar todos os agendamentos")
        opcao = int(input("\nInforme a opção escolhida: \n"))
        return opcao
    
    
    
    
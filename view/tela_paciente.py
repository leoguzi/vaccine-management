class TelaPaciente():

    def opcoes_paciente(self):
        print("========CONTROLE DE PACIENTES=========")
        print("1 - Cadastrar novo paciente")
        print("2 - Excluir paciente")
        print("3 - Editar paciente")
        print("4 - Listar pacientes")
        print("0 - Voltar ao menu principal")

        opcao = int(input("\nDigite o numero da opção: "))
        print("\n")
        return opcao
    
    def le_dados(self):
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))

        return {"nome": nome, "idade": idade}
        
    def le_codigo(self):
        codigo = int(input("Digite o código do paciente: "))
        return codigo

    def mostra_paciente(self, dados_paciente):
        print("Codigo: ", dados_paciente["codigo"])
        print("Nome: ", dados_paciente["nome"])
        print("Idade: ", dados_paciente["idade"])
        print("Numero de Doses: ", dados_paciente["numero_doses"])
        print("------------------------------")

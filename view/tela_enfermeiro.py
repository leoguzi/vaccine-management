class TelaEnfermeiros:

    def opcoes_enfermeiro(self):
            print("\n========CONTROLE DE ENFERMEIROS=========")
            print("1 - Cadastrar novo enfermeiro")
            print("2 - Excluir enfermeiro")
            print("3 - Editar enfermeiro")
            print("4 - Listar enfermeiros")
            print("5 - Listar atendimentos")
            print("0 - Voltar ao menu principal")

            opcao = int(input("\nDigite o numero da opção: "))
            print("\n")
            return opcao
    
    def le_nome(self):
        nome = str(input("Nome: "))
        return nome

    def le_codigo(self):
        try:
            codigo = int(input("Digite o código do enfermeiro: "))
        except:
            print("O codigo deve ser um numero!")
        return codigo

    def mostra_enfermeiro(self, dados_enfermeiro):
        print("Codigo: ", dados_enfermeiro["codigo"])
        print("Nome: ", dados_enfermeiro["nome"])
        print("Numero de atendimentos: ", dados_enfermeiro["n_atendimentos"])
        print("------------------------------")

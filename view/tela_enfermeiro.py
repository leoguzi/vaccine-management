import os
class TelaEnfermeiros:

    def opcoes_enfermeiro(self):
            print("========CONTROLE DE ENFERMEIROS=========")
            print("1 - Cadastrar novo enfermeiro")
            print("2 - Excluir enfermeiro")
            print("3 - Editar enfermeiro")
            print("4 - Listar enfermeiros")
            print("0 - Voltar ao menu principal")

            opcao = int(input("\nDigite o numero da opção: "))
            print("\n")
            return opcao
    
    def le_nome(self):
        nome = str(input("Nome: "))
        wait = input("Cadastrado! Pressione enter...")
        os.system('cls' if os.name == 'nt' else 'clear')
        return nome

    def le_codigo(self):
        codigo = None
        try:
            codigo = int(input("Digite o código do enfermeiro: "))
        except:
            print("\nO codigo deve ser um numero!")
        return codigo

    def mostra_enfermeiro(self, dados_enfermeiro):
        
        print("Codigo: ", dados_enfermeiro["codigo"])
        print("Nome: ", dados_enfermeiro["nome"])
        print("------------------------------")

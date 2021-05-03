import sys
sys.path.append(".")
from model.paciente import Paciente
from model.paciente_dao import PacienteDAO
from view.tela_paciente import TelaPaciente


class ControladorPacientes():

    def __init__(self, tela_paciente: TelaPaciente):
        self.__tela_paciente = tela_paciente
        self.__paciente_DAO = PacienteDAO()
        self.__gera_codigo = int(200) #codigo dos pacientes começa em 200

    def adiciona_paciente(self):
        while True: # obtem todos os dados ou None
            try:
                dados = self.__tela_paciente.le_dados()
                if dados == None:
                    break
                elif dados['nome'] == '' or dados['idade'] == '':
                    raise Exception #implementar uma exeção para quando não digitar algum dos dados e clicar em cadastrar
                else:
                    break
            except:
                self.__tela_paciente.mensagem("Paciente não cadastrado, digite todos os dados.")
        if dados is not None: #somente cadastra o novo paciente caso a janela não tenha sido fechada a ou clicado em voltar.
            self.__paciente_DAO.add(Paciente(dados['nome'], int(dados['idade']), self.__gera_codigo))
            self.__gera_codigo += 1 #incrementa o codigo

    def remove_paciente(self):
        while True: #obtem o dicionario do paciente ou None
            try:
                paciente_selecionado = self.__tela_paciente.combo_box_pacientes(self.lista_pacientes())
                if paciente_selecionado == '':
                    raise Exeption # exceção para "clicou em selecionar sem selecionar" aqui
                else: 
                    break
            except:
                self.__tela_paciente.mensagem("Selecione um paciente")
        if paciente_selecionado is not None:
            self.__paciente_DAO.remove(int(paciente_selecionado['codigo']))

    def edita_paciente(self):
        while True: #obtem o dicionario do enfermeiro ou None
            try:
                paciente_selecionado = self.__tela_paciente.combo_box_pacientes(self.lista_pacientes())
                if paciente_selecionado == '':
                    raise Exeption # exceção para "clicou em selecionar sem selecionar" aqui
                else: 
                    break
            except:
                self.__tela_paciente.mensagem("Selecione um paciente")
        if paciente_selecionado is not None: #se o usuario fechar a tela ou clicar em voltar antes de selecionar o enfermeiro, nem tenta ler os dados.
            while True: #obtem os novos dados ou None
                try:
                    novos_dados = self.__tela_paciente.le_dados(paciente_selecionado)
                    if novos_dados['nome'] == '' or novos_dados['idade'] == '':
                        raise Exeption #exceção para "clicou em cadastrar sem digitar nada" aqui
                    else:
                        break
                except:
                    self.__tela_paciente.mensagem("Digite todos os dados!")
        if paciente_selecionado is not None and novos_dados is not None: #somente edita caso a janela não tenha sido fechada.
            for paciente in self.__paciente_DAO.get_all():
                if paciente.codigo == paciente_selecionado['codigo']:
                    paciente.nome = novos_dados['nome']
                    paciente.idade = int(novos_dados['idade'])#está dando erro quando não digita inteiro arrumar exceção 
                    self.__paciente_DAO.update()
   
    def encontra_paciente_por_codigo(self, codigo):
        paciente = None
        while paciente is None:
            for i in range(len(self.__pacientes)):
                if self.__pacientes[i].codigo == codigo:
                    paciente = self.__pacientes[i]
                    return paciente
            print("\nPaciente não encontrado.\n")
            codigo = self.__tela_paciente.le_codigo()
    
    def vacina_paciente(self,codigo):
        paciente_vacinado = self.encontra_paciente_por_codigo(codigo)
        try:
            paciente_vacinado.numero_doses <= 2
        except:
            print("\nNão é possível concluir este agendamento. O paciente já recebeu duas doses de vacina.\n")
        else:
            paciente_vacinado.numero_doses += 1

    def lista_pacientes(self): #retorna uma lista de dicionarios contendo as informações dos pacientes ou None cado não exista nenhum cadastrado.
        try: 
            if len(self.__paciente_DAO.get_all()) > 0:
                lista_pacientes = []
                for paciente in self.__paciente_DAO.get_all():
                    lista_pacientes.append({'codigo': paciente.codigo, 'nome': paciente.nome, 'idade': paciente.idade, 'numero_doses': paciente.numero_doses})
            else:
                lista_pacientes = None
                raise Exception #criar uma exeção para lista vazia 
        except: 
           self.__tela_paciente.mensagem("Nenhum paciente cadastrado no posto!")
        return lista_pacientes

    def mostra_pacientes(self): #abre a tela que lista os pacientes

        self.__tela_paciente.mostra_pacientes(self.lista_pacientes()) 
    
    def abre_tela_pacientes(self):
        lista_opcoes = {1: self.adiciona_paciente, 2: self.remove_paciente, 3: self.edita_paciente, 4: self.mostra_pacientes}
        while True:
            valor_lido = self.__tela_paciente.opcoes_paciente()
            if valor_lido == 0 or valor_lido == None:
                break
            else:
                lista_opcoes[valor_lido]()
                
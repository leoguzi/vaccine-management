import sys
sys.path.append(".")
from model.paciente import Paciente
from model.paciente_dao import PacienteDAO
from view.tela_paciente import TelaPaciente
from controller.excecoes import ListaVaziaException
from controller.excecoes import CampoEmBrancoException
from controller.excecoes import NenhumSelecionadoException

class ControladorPacientes():

    def __init__(self, tela_paciente: TelaPaciente):
        self.__tela_paciente = tela_paciente
        self.__paciente_DAO = PacienteDAO()
        if len(self.__paciente_DAO.get_all()) == 0:
            self.__gera_codigo = int(200) #codigo dos pacientes começa em 200
        else:
            codigo = 200
            for paciente in self.__paciente_DAO.get_all(): #encontra o maior codigo que já foi usado.
                if paciente.codigo > codigo:
                    codigo = paciente.codigo
            self.__gera_codigo = codigo + 1
    
    def adiciona_paciente(self):
        while True: #obtem todos os dados ou None
            try:
                dados = self.__tela_paciente.le_dados()
                if dados == None:
                    break
                if dados['nome'] == '' or dados['idade'] == '':
                    raise CampoEmBrancoException #exceção para quando não digitar algum dos dados e clicar em cadastrar
                else:
                    try:
                        int(dados['idade'])
                        break
                    except ValueError:
                        self.__tela_paciente.mensagem('A idade deve ser um numero inteiro!') 
            except CampoEmBrancoException as mensagem:
                self.__tela_paciente.mensagem(mensagem)
        if dados is not None: #somente cadastra o novo paciente caso a janela não tenha sido fechada a ou clicado em voltar.
            self.__paciente_DAO.add(Paciente(dados['nome'], int(dados['idade']), self.__gera_codigo))
            self.__gera_codigo += 1 #incrementa o codigo

    def remove_paciente(self):
        codigo_paciente = self.seleciona_paciente()
        if codigo_paciente is not None:
            self.__paciente_DAO.remove(codigo_paciente)

    def edita_paciente(self):
        paciente = self.__paciente_DAO.get(self.seleciona_paciente())
        if paciente is not None: #se o usuario fechar a tela ou clicar em voltar antes de selecionar o paciente, nem tenta ler os dados.
            while True: #obtem os novos dados ou None
                try:
                    novos_dados = self.__tela_paciente.le_dados({'nome': paciente.nome, 'idade': paciente.idade})
                    if novos_dados == None:
                        break
                    if novos_dados['nome'] == '' or novos_dados['idade'] == '':
                        raise CampoEmBrancoException #exceção para quando não digitar algum dos dados e clicar em cadastrar
                    else:
                        try:
                            int(novos_dados['idade'])
                            break
                        except ValueError: #não digitou um numero inteiro
                            self.__tela_paciente.mensagem('A idade deve ser um numero inteiro!') 
                except CampoEmBrancoException as mensagem:
                    self.__tela_paciente.mensagem(mensagem)
        if paciente is not None and novos_dados is not None: #somente edita caso a janela não tenha sido fechada.
            paciente.nome = novos_dados['nome']
            paciente.idade = int(novos_dados['idade']) #foi garantido que o numero é inteiro anteriormente.
            self.__paciente_DAO.update()
   
    def encontra_paciente_por_codigo(self, codigo):
        return self.__paciente_DAO.get(codigo)


    
    def vacina_paciente(self,codigo):
        paciente_vacinado = self.encontra_paciente_por_codigo(codigo)
        try:
            if paciente_vacinado.numero_doses < 2:
                paciente_vacinado.numero_doses += 1
            else:
                raise Exception
        except:
            mensagem = 'Não é possível concluir este agendamento. O paciente já recebeu duas doses de vacina.'
            self.__tela_paciente.mensagem(mensagem)

    def lista_pacientes(self): #retorna uma lista de dicionarios contendo as informações dos pacientes ou None caso não exista nenhum cadastrado.
        try: 
            if len(self.__paciente_DAO.get_all()) > 0:
                lista_pacientes = []
                for paciente in self.__paciente_DAO.get_all():
                    lista_pacientes.append({'codigo': paciente.codigo, 'nome': paciente.nome, 'idade': paciente.idade, 'numero_doses': paciente.numero_doses})
            else:
                lista_pacientes = None
                raise ListaVaziaException('paciente') #exceção para lista vazia 
        except ListaVaziaException as mensagem:
            self.__tela_paciente.mensagem(mensagem)
        return lista_pacientes

    def mostra_pacientes(self): #abre a tela que lista os pacientes
        self.__tela_paciente.mostra_pacientes(self.lista_pacientes()) 
    
    def seleciona_paciente(self): #obtem o codigo do paciente ou None
        while True: 
            try:
                codigo_paciente_selecionado = self.__tela_paciente.combo_box_pacientes(self.lista_pacientes())
                if codigo_paciente_selecionado == '':
                    raise NenhumSelecionadoException('paciente') # exceção para "clicou em selecionar sem selecionar" aqui
                else: 
                    break
            except NenhumSelecionadoException as mensagem:
                self.__tela_paciente.mensagem(mensagem)
        return codigo_paciente_selecionado
    
    def abre_tela_pacientes(self):
        lista_opcoes = {1: self.adiciona_paciente, 2: self.remove_paciente, 3: self.edita_paciente, 4: self.mostra_pacientes}
        while True:
            valor_lido = self.__tela_paciente.opcoes_paciente()
            if valor_lido == 0 or valor_lido == None:
                break
            else:
                lista_opcoes[valor_lido]()
                
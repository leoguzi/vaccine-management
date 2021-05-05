class ListaVaziaException(Exception):
    def __init__(self, texto):
        super().__init__('Nenhum(a) ' + texto + ' cadastrado(a) no sistema.')

class CampoEmBrancoException(Exception):
    def __init__(self):
        super().__init__('Você deve preencher todos os campos antes de confirmar!')

class NenhumSelecionadoException(Exception):
    def __init__(self, texto):
        super().__init__('Voce deve selecnionar um(a) ' + texto + " antes de continuar!")


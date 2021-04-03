from controller.controlador_sistema import ControladorSistema
from view.tela_sistema import TelaSistema

if __name__ == "__main__":

    controlador_sistema = ControladorSistema(TelaSistema())
    controlador_sistema.abre_menu_principal()

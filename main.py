from controller.controlador_enfermeiros import ControladorEnfermeiros
from controller.controlador_pacientes import ControladorPacientes
from view.tela_paciente import TelaPaciente
from view.tela_enfermeiro import TelaEnfermeiros

#controlador = ControladorEnfermeiros(TelaEnfermeiros())

#controlador.abre_tela_enfermeiros()

controlador = ControladorPacientes(TelaPaciente())

controlador.abre_tela_pacientes()
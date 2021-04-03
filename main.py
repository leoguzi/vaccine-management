from controller.controlador_enfermeiros import ControladorEnfermeiros
from controller.controlador_pacientes import ControladorPacientes
from view.tela_paciente import TelaPaciente
from view.tela_enfermeiro import TelaEnfermeiros
from view.tela_vacina import TelaVacina
from controller.controlador_vacinas import ControladorVacina
from controller.controlador_agendamentos import ControladorAgendamento
from view.tela_agendamento import TelaAgendamento

#controlador = ControladorEnfermeiros(TelaEnfermeiros())

#controlador.abre_tela_enfermeiros()

#controlador = ControladorPacientes(TelaPaciente())

#controlador.abre_tela_pacientes()

#controlador = ControladorVacina(TelaVacina())
#controlador.inicia_tela_vacina()

controlador = ControladorAgendamento(TelaAgendamento())
controlador.inicia_tela_agendamento()
from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoPaciente import DaoPaciente
from pectusapi.schemas.Schema import PacienteSchema, serializar_a_json

paciente_servicio = Blueprint('paciente_servicio', __name__)

@paciente_servicio.route('/paciente/agregar')
def pctAgregar():

	parametros = {}
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	paciente = DaoPaciente.crear(parametros)

	if paciente:
		respuesta['ok'] = True

	return jsonify(respuesta)


@paciente_servicio.route('/paciente/todos')
def pctTodos():

	pacientes = DaoPaciente.buscarTodos()
	return serializar_a_json(PacienteSchema, 'paciente', pacientes)


@paciente_servicio.route('/paciente/editar')
def pctEditar():

	cedula = request.args.get('cedula')
	parametros = dict()
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	paciente = DaoPaciente.actualizar(cedula, parametros)

	if paciente:
		respuesta['ok'] = True

	return jsonify(respuesta)

@paciente_servicio.route('/paciente/buscar')
def pctBuscar():

	parametros = {}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	pacientes = DaoPaciente.buscarPorArgumentos(parametros)

	return serializar_a_json(PacienteSchema, 'paciente', pacientes)
from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoEstudio import DaoEstudio
from pectusapi.schemas.Schema import EstudioSchema, serializar_a_json

estudio_servicio = Blueprint('estudio_servicio', __name__)

@estudio_servicio.route('/estudio/buscar')
def estudioBuscar():

	parametros = {}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	estudios = DaoEstudio.buscarPorArgumentos(parametros)

	return serializar_a_json(EstudioSchema, 'estudios', estudios, muchos=True)

@estudio_servicio.route('/estudio/todos')
def estudioTodos():
	estudios = DaoEstudio.buscarTodos()
	return serializar_a_json(EstudioSchema, 'estudios', estudios)

@estudio_servicio.route('/estudio/agregar')
def estudioAgregar():

	parametros = {}
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	estudio = DaoEstudio.crear(parametros)

	if estudio:
		respuesta['ok'] = True

	return jsonify(respuesta)

@estudio_servicio.route('/estudio/editar')
def estudioEditar():
	id = request.args.get('id')
	parametros = dict()
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	estudio = DaoEstudio.actualizar(id, parametros)

	if estudio:
		respuesta['ok'] = True

	return jsonify(respuesta)
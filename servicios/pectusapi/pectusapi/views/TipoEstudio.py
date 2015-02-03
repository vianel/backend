from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoTipoEstudio import DaoTipoEstudio
from pectusapi.schemas.Schema import TipoEstudioSchema, serializar_a_json

tipo_estudio_servicio = Blueprint('tipo_estudio_servicio', __name__)

@tipo_estudio_servicio.route('/tipo-estudio/todos')
def clinicaTodos():
	tipos_estudios = DaoTipoEstudio.buscarTodos()
	return serializar_a_json(TipoEstudioSchema, 'tipoestudios', tipos_estudios)

@tipo_estudio_servicio.route('/tipo-estudio/agregar')
def tipoEstudioAgregar():

	parametros = {}
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	tipo_estudio = DaoTipoEstudio.crear(parametros)

	if tipo_estudio:
		respuesta['ok'] = True

	return jsonify(respuesta)

@tipo_estudio_servicio.route('/tipo-estudio/editar')
def tipoEstudioEditar():
	id = request.args.get('id')
	parametros = dict()
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	tipo_estudio = DaoTipoEstudio.actualizar(id, parametros)

	if tipo_estudio:
		respuesta['ok'] = True

	return jsonify(respuesta)

@tipo_estudio_servicio.route('/tipo-estudio/buscar')
def evetBuscar():

	parametros = {}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	tipo_estudio = DaoTipoEstudio.buscarPorArgumentos(parametros)

	return serializar_a_json(TipoEstudioSchema, 'tipoestudio', tipo_estudio, muchos=True)
from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoTipoColaboracion import DaoTipoColaboracion
from pectusapi.schemas.Schema import TipoColaboracionSchema, serializar_a_json

tipo_colaboracion_servicio = Blueprint('tipo_colaboracion_servicio', __name__)

@tipo_colaboracion_servicio.route('/tipo-colaboracion/todos')
def tipoColaTodos():
	tipos_colaboracion = DaoTipoColaboracion.buscarTodos()
	return serializar_a_json(TipoColaboracionSchema, 'tipocolaboracion', tipos_colaboracion)


@tipo_colaboracion_servicio.route('/tipo-colaboracion/agregar')
def tipoColaAgregar():

	parametros = {}
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	tipo_colaboracion = DaoTipoColaboracion.crear(parametros)

	if tipo_colaboracion:
		respuesta['ok'] = True

	return jsonify(respuesta)

@tipo_colaboracion_servicio.route('/tipo-colaboracion/editar')
def tipoColaEditar():
	id = request.args.get('id')
	parametros = dict()
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	tipo_colaboracion = DaoTipoColaboracion.actualizar(id, parametros)

	if tipo_colaboracion:
		respuesta['ok'] = True

	return jsonify(respuesta)

@tipo_colaboracion_servicio.route('/tipo-colaboracion/buscar')
def tipoColaBuscar():

	parametros = {}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	tipo_colaboracion = DaoTipoColaboracion.buscarPorArgumentos(parametros)

	return serializar_a_json(TipoColaboracionSchema, 'tipocolaboracion', tipo_colaboracion, muchos=True)
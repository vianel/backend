from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoColaboracion import DaoColaboracion
from pectusapi.schemas.Schema import ColaboracionCESchema, serializar_a_json

colaboracion_servicio = Blueprint('colaboracion_servicio', __name__)

@colaboracion_servicio.route('/colaboracion/todos')
def colaboracionTodos():
	colaboraciones = DaoColaboracion.buscarTodos()
	return serializar_a_json(ColaboracionCESchema, 'colaboraciones', colaboraciones)

@colaboracion_servicio.route('/colaboracion/agregar')
def colaboracionAgregar():

	parametros = {}
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	colaboracion = DaoColaboracion.crear(parametros)

	if colaboracion:
		respuesta['ok'] = True

	return jsonify(respuesta)

@colaboracion_servicio.route('/colaboracion/editar')
def colaboracionEditar():
	id = request.args.get('id')
	parametros = dict()
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)
			
	colaboracion = DaoColaboracion.actualizar(id, parametros)

	if colaboracion:
		respuesta['ok'] = True

	return jsonify(respuesta)
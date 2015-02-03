from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoPatologia import DaoPatologia
from pectusapi.schemas.Schema import PatologiaSchema, serializar_a_json

patologia_servicio = Blueprint('patologia_servicio', __name__)

@patologia_servicio.route('/patologia/todos')
def patologiaTodos():
	patologias = DaoPatologia.buscarTodos()
	return serializar_a_json(PatologiaSchema, 'patologias', patologias)

@patologia_servicio.route('/patologia/agregar')
def patologiaAgregar():

	parametros = {}
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	patologia = DaoPatologia.crear(parametros)

	if patologia:
		respuesta['ok'] = True

	return jsonify(respuesta)

@patologia_servicio.route('/patologia/editar')
def patologiaEditar():
	id = request.args.get('id')
	parametros = dict()
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	patologia = DaoPatologia.actualizar(id, parametros)

	if patologia:
		respuesta['ok'] = True

	return jsonify(respuesta)
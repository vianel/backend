from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoPatrocinador import DaoPatrocinador
from pectusapi.schemas.Schema import PatrocinadorSchema, serializar_a_json

patrocinador_servicio = Blueprint('patrocinador_servicio', __name__)

@patrocinador_servicio.route('/patrocinador/todos')
def patroTodos():
	patrocinadores = DaoPatrocinador.buscarTodos()
	return serializar_a_json(PatrocinadorSchema, 'patrocinadores', patrocinadores)

@patrocinador_servicio.route('/patrocinador/agregar')
def patroAgregar():

	parametros = {}
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	patrocinador = DaoPatrocinador.crear(parametros)

	if patrocinador:
		respuesta['ok'] = True

	return jsonify(respuesta)
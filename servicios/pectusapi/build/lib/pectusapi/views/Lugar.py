from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoLugar import DaoLugar
from pectusapi.schemas.Schema import LugarSchema, serializar_a_json

lugar_servicio = Blueprint('lugar_servicio', __name__)

@lugar_servicio.route('/lugar/todos')
def lugarTodos():
	lugares = DaoLugar.buscarTodos()
	return serializar_a_json(LugarSchema, 'lugares', lugares)


@lugar_servicio.route('/lugar/agregar')
def lugarAgregar():

	parametros = {}
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	lugar = DaoLugar.crear(parametros)

	if lugar:
		respuesta['ok'] = True

	return jsonify(respuesta)

@lugar_servicio.route('/lugar/editar')
def lugarEditar():
	id = request.args.get('id')
	parametros = dict()
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)
			
	lugar = DaoLugar.actualizar(id, parametros)

	if lugar:
		respuesta['ok'] = True

	return jsonify(respuesta)

@lugar_servicio.route('/lugar/buscar')
def lugarBuscar():

	parametros = {}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	lugar = DaoLugar.buscarPorArgumentos(parametros)

	return serializar_a_json(LugarSchema, 'lugar', lugar, muchos=True)
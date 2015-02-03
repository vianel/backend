from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoTipoLugar import DaoTipoLugar
from pectusapi.schemas.Schema import TipoLugarSchema, serializar_a_json

tipo_lugar_servicio = Blueprint('tipo_lugar_servicio', __name__)

@tipo_lugar_servicio.route('/tipo-lugar/todos')
def lugarTodos():
	tipo_lugares = DaoTipoLugar.buscarTodos()
	return serializar_a_json(TipoLugarSchema, 'tipolugar', tipo_lugares)


@tipo_lugar_servicio.route('/tipo-lugar/agregar')
def lugarAgregar():

	parametros = {}
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	lugar = DaoTipoLugar.crear(parametros)

	if lugar:
		respuesta['ok'] = True

	return jsonify(respuesta)

@tipo_lugar_servicio.route('/tipo-lugar/editar')
def lugarEditar():
	id = request.args.get('id')
	parametros = dict()
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)
			
	lugar = DaoTipoLugar.actualizar(id, parametros)

	if lugar:
		respuesta['ok'] = True

	return jsonify(respuesta)

@tipo_lugar_servicio.route('/tipo-lugar/buscar')
def lugarBuscar():

	parametros = {}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	lugar = DaoTipoLugar.buscarPorArgumentos(parametros)

	return serializar_a_json(TipoLugarSchema, 'tipolugar', lugar, muchos=True)
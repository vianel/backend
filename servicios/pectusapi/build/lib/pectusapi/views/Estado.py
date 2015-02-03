from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoEstado import DaoEstado
from pectusapi.schemas.Schema import EstadoSchema, serializar_a_json

estado_servicio = Blueprint('estado_servicio', __name__)

@estado_servicio.route('/estado/todos')
def ciudadTodos():
	estados = DaoEstado.buscarTodos()
	return serializar_a_json(EstadoSchema, 'estados', estados)

@estado_servicio.route('/estado/buscar')
def ciudadBuscar():

	parametros = {}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	estados = DaoEstado.buscarPorArgumentos(parametros)
	return serializar_a_json(EstadoSchema, 'estados', estados, muchos=True)
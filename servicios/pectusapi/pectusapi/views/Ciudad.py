from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoCiudad import DaoCiudad
from pectusapi.schemas.Schema import CiudadSchema, serializar_a_json

ciudad_servicio = Blueprint('ciudad_servicio', __name__)

@ciudad_servicio.route('/ciudad/todos')
def ciudadTodos():
	ciudades = DaoCiudad.buscarTodos()
	return serializar_a_json(CiudadSchema, 'ciudades', ciudades)

@ciudad_servicio.route('/ciudad/buscar')
def ciudadBuscar():

	parametros = {}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	ciudades = DaoCiudad.buscarPorArgumentos(parametros)
	return serializar_a_json(CiudadSchema, 'ciudades', ciudades, muchos=True)
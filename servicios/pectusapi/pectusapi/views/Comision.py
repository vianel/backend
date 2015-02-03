from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoComision import DaoComision
from pectusapi.schemas.Schema import ComisionSchema, serializar_a_json

comision_servicio = Blueprint('comision_servicio', __name__)

@comision_servicio.route('/comision/todos')
def comisionTodos():
	comisiones = DaoComision.buscarTodos()
	return serializar_a_json(ComisionSchema, 'comisiones', comisiones)


@comision_servicio.route('/comision/agregar')
def comisionAgregar():

	parametros = {}
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	comision = DaoComision.crear(parametros)

	if comision:
		respuesta['ok'] = True

	return jsonify(respuesta)

@comision_servicio.route('/comision/editar')
def comisionEditar():
	id = request.args.get('id')
	parametros = dict()
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)
			
	comision = DaoComision.actualizar(id, parametros)

	if comision:
		respuesta['ok'] = True

	return jsonify(respuesta)

@comision_servicio.route('/comision/buscar')
def comisionBuscar():

	parametros = {}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	comision = DaoComision.buscarPorArgumentos(parametros)

	return serializar_a_json(ComisionSchema, 'comision', comision, muchos=True)
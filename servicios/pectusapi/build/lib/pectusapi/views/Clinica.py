from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoClinica import DaoClinica
from pectusapi.schemas.Schema import ClinicaSchema, serializar_a_json

clinica_servicio = Blueprint('clinica_servicio', __name__)

@clinica_servicio.route('/clinica/buscar')
def clinicaBuscar():

	parametros = {}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	clinicas = DaoClinica.buscarPorArgumentos(parametros)

	return serializar_a_json(ClinicaSchema, 'clinicas', clinicas, muchos=True)

@clinica_servicio.route('/clinica/todos')
def clinicaTodos():
	clinicas = DaoClinica.buscarTodos()
	return serializar_a_json(ClinicaSchema, 'clinicas', clinicas)

@clinica_servicio.route('/clinica/editar')
def clinicaEditar():
	id = request.args.get('rif')
	parametros = dict()
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)
			
	clinica = DaoClinica.actualizar(id, parametros)

	if clinica:
		respuesta['ok'] = True

	return jsonify(respuesta)

@clinica_servicio.route('/clinica/agregar')
def estudioAgregar():

	parametros = {}
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	clinica = DaoClinica.crear(parametros)

	if clinica:
		respuesta['ok'] = True

	return jsonify(respuesta)
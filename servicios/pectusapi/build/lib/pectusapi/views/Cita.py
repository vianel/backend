from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoCita import DaoCita
from pectusapi.daos.DaoResultadoAyuda import DaoResultadoAyuda
from pectusapi.schemas.Schema import CitaSchema, serializar_a_json

cita_servicio = Blueprint('cita_servicio', __name__)

@cita_servicio.route('/cita/todos')
def citaTodos():

	citas = DaoCita.buscarTodos()
	return serializar_a_json(CitaSchema, 'citas', citas)


@cita_servicio.route('/cita/agregar')
def citaAgregar():

	parametros = {}
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	cita = DaoCita.crear(parametros)

	if cita:
		respuesta['ok'] = True

	return jsonify(respuesta)

@cita_servicio.route('/cita/buscar')
def citaBuscar():

	parametros = {}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	citas = DaoCita.buscarPorArgumentos(parametros)

	return serializar_a_json(CitaSchema, 'cita', citas, muchos=True)

@cita_servicio.route('/cita/resultado/agregar')
def citaRegistrarResultado():

  parametros = {}
  respuesta = {'ok' : False}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)

  operacion = DaoResultadoAyuda.crear(parametros)

  if operacion:
    respuesta['ok'] = True

  return jsonify(respuesta)
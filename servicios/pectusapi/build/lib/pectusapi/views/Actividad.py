from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoActividad import DaoActividad
from pectusapi.daos.DaoVoluntario import DaoVoluntario
from pectusapi.daos.DaoSolicitudActividad import DaoSolicitudActividad
from pectusapi.schemas.Schema import (
	ActividadSchema, 
	VoluntarioSchema,
	serializar_a_json,
)

actividad_servicio = Blueprint('actividad_servicio', __name__)

@actividad_servicio.route('/actividad/agregar')
def actividadAgregar():

	parametros = {}
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	actividad = DaoActividad.crear(parametros)

	if actividad:
		respuesta['ok'] = True

	return jsonify(respuesta)

@actividad_servicio.route('/actividad/todos')
def actvBuscarTodos():

	actividades = DaoActividad.buscarTodos()
	return serializar_a_json(ActividadSchema, 'actividades', actividades)

@actividad_servicio.route('/actividad/voluntarios')
def actVoluntarios():

	voluntarios = None
	id = request.args.get('id')

	actividad = DaoActividad.buscarPorId(id)
	print actividad

	if actividad:
		voluntarios = actividad.voluntarios

	return serializar_a_json(VoluntarioSchema, 'voluntarios', voluntarios)

@actividad_servicio.route('/actividad/buscar')
def actBuscar():

	parametros = {}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	actividad = DaoActividad.buscarPorArgumentos(parametros)

	return serializar_a_json(ActividadSchema, 'actividad', actividad, muchos=True)


@actividad_servicio.route('/actividad/buscar-por-tipo')
def actBuscarTipo():
	idtipoactividad = request.args.get('idtipoactividad')

	solicitudes = DaoSolicitudActividad.buscarPorArgumentos({'idtipoactividad': idtipoactividad})
	actividades = list()

	for sol in solicitudes:
		actividades += DaoActividad.buscarPorArgumentos({'idsolicitudactividad': sol.id})

	return serializar_a_json(ActividadSchema, 'actividades', actividades, muchos=True)


@actividad_servicio.route('/actividad/editar')
def actvEditar():

	id = request.args.get('id')
	parametros = dict()
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	actividad = DaoActividad.actualizar(id, parametros)

	if actividad:
		respuesta['ok'] = True

	return jsonify(respuesta)

@actividad_servicio.route('/actividad/asingar-voluntario')
def agregVoluntarioActividad():

	cedulas = request.args.get('cedula')
	idactividad = request.args.get('idactividad')
	respuesta = dict(ok=False)
	cant = 0
	actividad = DaoActividad.buscarPorId(idactividad)

	for cedula in cedulas.split(','):
		voluntario = DaoVoluntario.buscarPorId(cedula)
		
		if actividad and voluntario:
			DaoActividad.agregarVoluntario(actividad, voluntario)
			cant += 1

	respuesta['ok'] = cant == len(cedulas.split(','))
	return jsonify(respuesta)
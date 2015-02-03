from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoEvento import DaoEvento
from pectusapi.daos.DaoVoluntario import DaoVoluntario
from pectusapi.schemas.Schema import EventoSchema, serializar_a_json

evento_servicio = Blueprint('evento_servicio', __name__)

@evento_servicio.route('/evento/buscar')
def evetBuscar():

	parametros = {}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	eventos = DaoEvento.buscarPorArgumentos(parametros)

	return serializar_a_json(EventoSchema, 'evento', eventos, muchos=True)


@evento_servicio.route('/evento/todos')
def evetTodos():
	eventos = DaoEvento.buscarTodos()
	return serializar_a_json(EventoSchema, 'eventos', eventos)


@evento_servicio.route('/evento/agregar')
def eventoAgregar():

	parametros = {}
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	evento = DaoEvento.crear(parametros)

	if evento:
		respuesta['ok'] = True

	return jsonify(respuesta)


@evento_servicio.route('/evento/editar')
def evtEditar():

	evento = None
	respuesta = dict(ok=False)
	parametros = dict()
	id = request.args.get('id')

	if id:
		evento = DaoEvento.buscarPorId(id)

		if evento:
			for key in request.args:
				if request.args.get(key):
					parametros[key] = request.args.get(key)

			if DaoEvento.actualizar(id, parametros):
				respuesta['ok'] = True

	return jsonify(respuesta)

@evento_servicio.route('/evento/asignar-voluntario')
def asignarVolEvento():

	cedula = request.args.get('cedula')
	idevento = request.args.get('idevento')
	respuesta = dict(ok=False)

	voluntario = DaoVoluntario.buscarPorId(cedula)
	evento = DaoEvento.buscarPorId(idevento)

	if evento and voluntario:
		DaoEvento.agregarVoluntario(evento, voluntario)
		respuesta['ok'] = True

	return jsonify(respuesta)

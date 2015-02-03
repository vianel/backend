from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoTarea import DaoTarea
from pectusapi.schemas.Schema import TareaSchema, serializar_a_json

tarea_servicio = Blueprint('tarea_servicio', __name__)


@tarea_servicio.route('/tarea/todos')
def tareaTodos():
	tarea = DaoTarea.buscarTodos()
	return serializar_a_json(TareaSchema, 'tarea', tarea)

@tarea_servicio.route('/tarea/agregar')
def tareaAgregar():

	parametros = {}
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	tarea = DaoTarea.crear(parametros)

	if tarea:
		respuesta['ok'] = True

	return jsonify(respuesta)
from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoModulo import DaoModulo
from pectusapi.daos.DaoTarea import DaoTarea
from pectusapi.schemas.Schema import ModuloSchema, TareaSchema, serializar_a_json

modulo_servicio = Blueprint('modulo_servicio', __name__)


@modulo_servicio.route('/modulo/todos')
def moduloTodos():
	modulo = DaoModulo.buscarTodos()
	return serializar_a_json(ModuloSchema, 'modulos', modulo)

@modulo_servicio.route('/modulo/agregar')
def moduloAgregar():

	parametros = {}
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	modulo = DaoModulo.crear(parametros)

	if modulo:
		respuesta['ok'] = True

	return jsonify(respuesta)

@modulo_servicio.route('/modulo/tarea')
def moduloAgregarTarea():
	respuesta = dict(ok=False)
	idtarea = request.args.get('idtarea')
	idmodulo = request.args.get('idmodulo')

	modulo = DaoModulo.buscarPorId(idmodulo)
	tarea = DaoTarea.buscarPorId(idtarea)

	if modulo and tarea:
		tarea_agregada = DaoModulo.agregarTarea(modulo, tarea)
		respuesta['ok'] = True
		respuesta['idmoduloxtarea'] = tarea_agregada.id

	return jsonify(respuesta)


@modulo_servicio.route('/modulo/tarea/todos')
def moduloTareaTodos():
	id = request.args.get('idmodulo')

	modulo = DaoModulo.buscarPorId(id)
	tareas = []

	if modulo:
		tareas = modulo.tareas

	return serializar_a_json(TareaSchema, 'tareas', tareas, muchos=True)

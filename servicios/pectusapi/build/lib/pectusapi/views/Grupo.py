from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoGrupo import DaoGrupo
from pectusapi.daos.DaoOperaciones import DaoOperaciones
from pectusapi.schemas.Schema import GrupoSchema, serializar_a_json

grupo_servicio = Blueprint('grupo_servicio', __name__)


@grupo_servicio.route('/grupo/todos')
def grupoTodos():
	grupo = DaoGrupo.buscarTodos()
	return serializar_a_json(GrupoSchema, 'grupos', grupo)

@grupo_servicio.route('/grupo/agregar')
def grupoAgregar():

	parametros = {}
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	grupo = DaoGrupo.crear(parametros)

	if grupo:
		respuesta['ok'] = True

	return jsonify(respuesta)


# /grupo/modulo/agregar?idgrupo=2&idmoduloxtarea=4

@grupo_servicio.route('/grupo/modulo/agregar')
def grupoModuloAgregar():
	respuesta = dict(ok=True)
	idgrupo = request.args.get('idgrupo')
	modulosxtareas = request.args.get('idmoduloxtarea')
	t = 0

	for idmoduloxtarea in modulosxtareas.split(','):
		operacion = DaoOperaciones.crear({'idgrupo': idgrupo, 'idmoduloxtarea': idmoduloxtarea})
		t += 1

		if not operacion:
			respuesta['ok'] = False


	return jsonify(respuesta)

# /grupo/modulo/todos?idgrupo=1

@grupo_servicio.route('/grupo/modulo/todos')
def grupoModuloTodos():

	idgrupo = request.args.get('idgrupo')
	grupo = DaoGrupo.buscarPorId(idgrupo)
	respuesta = {'ok': False}

	if grupo:
		modulos = DaoGrupo.modulos(grupo)

		if modulos:
			respuesta['ok'] = True
			respuesta['modulos'] = modulos

	return jsonify(respuesta)


from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoUsuario import DaoUsuario
from pectusapi.daos.DaoGrupo import DaoGrupo
from pectusapi.schemas.Schema import UsuarioSchema, GrupoSchema, serializar_a_json
from pectusapi.lib.util import encriptar

usuario_servicio = Blueprint('usuario_servicio', __name__)


@usuario_servicio.route('/usuario/autentificacion')
def usuAutentificacion():

	parametros = {
		'login': request.args.get('login'),
		'clave': encriptar(request.args.get('clave').strip()),
	}

	usuario = DaoUsuario.buscarPorArgumentos(parametros)
	respuesta  = dict(
		ok=False
	)

	if usuario:
		respuesta['ok'] = True
		respuesta['grupos'] = DaoUsuario.permisos(usuario[0])

	return jsonify(respuesta)

@usuario_servicio.route('/usuario/todos')
def usuarioTodos():
	usuario = DaoUsuario.buscarTodos()
	return serializar_a_json(UsuarioSchema, 'usuario', usuario)

@usuario_servicio.route('/usuario/agregar')
def usuarioAgregar():

	parametros = {}
	respuesta = {'ok' : False}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	usuario = DaoUsuario.crear(parametros)

	if usuario:
		respuesta['ok'] = True

	return jsonify(respuesta)

@usuario_servicio.route('/usuario/grupo')
def usuarioAgregarGrupo():
	respuesta = dict(ok=False)
	login = request.args.get('login')
	idgrupo = request.args.get('idgrupo')

	usuario = DaoUsuario.buscarPorId(login)
	grupo = DaoGrupo.buscarPorId(idgrupo)

	if usuario and grupo:
		DaoUsuario.agregarGrupo(usuario, grupo)
		respuesta['ok'] = True

	return jsonify(respuesta)

@usuario_servicio.route('/usuario/grupo/todos')
def usurioGrupos():
	login = request.args.get('login')

	usuario = DaoUsuario.buscarPorId(login)

	grupos = []
	if usuario:
		grupos = usuario.grupos

	return serializar_a_json(GrupoSchema, 'grupos', grupos, muchos=True)
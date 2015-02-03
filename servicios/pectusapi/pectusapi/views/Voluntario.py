from flask import jsonify, Blueprint, request

from pectusapi.lib.util import parsear_url_parametros
from pectusapi.daos.DaoVoluntario import DaoVoluntario
from pectusapi.daos.DaoComision import DaoComision
from pectusapi.schemas.Schema import VoluntarioSchema, ActividadSchema, serializar_a_json

voluntario_servicio = Blueprint('voluntario_servicio', __name__)


@voluntario_servicio.route('/voluntario/agregar', methods=['GET', 'POST'])
def voluntarioAgregar():
  parametros = {}
  respuesta = {'ok' : False}
  args = None

  if request.method == 'POST':
    args = parsear_url_parametros(request.data)
  else:
    args = request.args

  for key in args:
    if args[key]:
      parametros[key] = args[key]

  voluntario = DaoVoluntario.crear(parametros)

  if voluntario:
    respuesta['ok'] = True

  return jsonify(respuesta)

@voluntario_servicio.route('/voluntario/todos')
def vltTodos():
	voluntarios = DaoVoluntario.buscarTodos()
	return serializar_a_json(VoluntarioSchema, 'voluntarios', voluntarios)

@voluntario_servicio.route('/voluntario/actividades')
def vltActividades():

	cedula = request.args.get('cedula')
	voluntario = None
	actividades = None

	if id:
		voluntario = DaoVoluntario.buscarPorId(cedula)

		if voluntario:
			actividades = voluntario.actividades

	return serializar_a_json(ActividadSchema, 'actividades', actividades)

@voluntario_servicio.route('/voluntario/editar')
def volEditar():
  id = request.args.get('cedula')
  parametros = dict()
  respuesta = {'ok' : False}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)
      
  voluntario = DaoVoluntario.actualizar(id, parametros)

  if voluntario:
    respuesta['ok'] = True

  return jsonify(respuesta)

@voluntario_servicio.route('/voluntario/buscar')
def volBuscar():

  parametros = {}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)

  voluntarios = DaoVoluntario.buscarPorArgumentos(parametros)

  return serializar_a_json(VoluntarioSchema, 'voluntarios', voluntarios, muchos=True)

@voluntario_servicio.route('/voluntario/comision')
def volAgregarComision():

  respuesta = dict(ok=False)
  cedula = request.args.get('cedula')
  idcomision = request.args.get('idcomision')

  voluntario = DaoVoluntario.buscarPorId(cedula)
  comision = DaoComision.buscarPorId(idcomision)

  if voluntario and comision:
    DaoVoluntario.agregarComision(voluntario, comision)
    respuesta['ok'] = True

  return jsonify(respuesta)

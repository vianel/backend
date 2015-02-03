from flask import jsonify, Blueprint, request

from pectusapi.lib.util import parsear_url_parametros
from pectusapi.daos.DaoPersona import DaoPersona
from pectusapi.schemas.Schema import PersonaSchema, serializar_a_json

persona_servicio = Blueprint('persona_servicio', __name__)

@persona_servicio.route('/persona/agregar', methods=['GET', 'POST'])
def personaAgregar():
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

  persona = DaoPersona.crear(parametros)

  if persona:
    respuesta['ok'] = True

  return jsonify(respuesta)

@persona_servicio.route('/persona/buscar')
def personaBuscar():

  parametros = {}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)

  personas = DaoPersona.buscarPorArgumentos(parametros)
  return serializar_a_json(PersonaSchema, 'personas', personas, muchos=True)

@persona_servicio.route('/persona/editar')
def personaEditar():
  id = request.args.get('cedula')
  parametros = dict()
  respuesta = {'ok' : False}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)
      
  persona = DaoPersona.actualizar(id, parametros)

  if persona:
    respuesta['ok'] = True

  return jsonify(respuesta)
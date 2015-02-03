from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoCausa import DaoCausa
from pectusapi.schemas.Schema import CausaSchema, serializar_a_json

causa_servicio = Blueprint('causa_servicio', __name__)

@causa_servicio.route('/causa/buscar')
def causaBuscar():

  parametros = {}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)

  causa = DaoCausa.buscarPorArgumentos(parametros)

  return serializar_a_json(CausaSchema, 'motivorechazos', causa, muchos=True)

@causa_servicio.route('/causa/todos')
def causaTodos():
  causas = DaoCausa.buscarTodos()
  return serializar_a_json(CausaSchema, 'causas', causas)

@causa_servicio.route('/causa/editar')
def causaEditar():
  id = request.args.get('id')
  parametros = dict()
  respuesta = {'ok' : False}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)
      
  causa = DaoCausa.actualizar(id, parametros)

  if causa:
    respuesta['ok'] = True

  return jsonify(respuesta)

@causa_servicio.route('/causa/agregar')
def causaAgregar():

  parametros = {}
  respuesta = {'ok' : False}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)

  causa = DaoCausa.crear(parametros)

  if causa:
    respuesta['ok'] = True

  return jsonify(respuesta)
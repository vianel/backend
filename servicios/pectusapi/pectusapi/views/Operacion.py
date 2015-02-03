from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoOperaciones import DaoOperaciones
from pectusapi.schemas.Schema import OperacionSchema, serializar_a_json

operacion_servicio = Blueprint('operacion_servicio', __name__)


@operacion_servicio.route('/operacion/todos')
def operacionTodos():
  operaciones = DaoOperaciones.buscarTodos()
  return serializar_a_json(OperacionSchema, 'operaciones', operaciones)

#Idtarea & idmodulo
@operacion_servicio.route('/operacion/agregar')
def moduloAgregar():

  parametros = {}
  respuesta = {'ok' : False}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)

  operacion = DaoOperaciones.crear(parametros)

  if operacion:
    respuesta['ok'] = True

  return jsonify(respuesta)
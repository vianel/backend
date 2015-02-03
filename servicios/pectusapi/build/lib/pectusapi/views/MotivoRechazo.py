from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoMotivoRechazo import DaoMotivoRechazo
from pectusapi.schemas.Schema import MotivoRechazoSchema, serializar_a_json

motico_rechazo_servicio = Blueprint('motico_rechazo_servicio', __name__)

@motico_rechazo_servicio.route('/motivo-rechazo/buscar')
def motivoRechazoBuscar():

  parametros = {}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)

  motivo_rechazo = DaoMotivoRechazo.buscarPorArgumentos(parametros)

  return serializar_a_json(MotivoRechazoSchema, 'motivorechazos', motivo_rechazo, muchos=True)

@motico_rechazo_servicio.route('/motivo-rechazo/todos')
def motivoRechazoTodos():
  motivos = DaoMotivoRechazo.buscarTodos()
  return serializar_a_json(MotivoRechazoSchema, 'motivosrechazos', motivos)

@motico_rechazo_servicio.route('/motivo-rechazo/editar')
def motivoRechazoEditar():
  id = request.args.get('id')
  parametros = dict()
  respuesta = {'ok' : False}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)
      
  motivo_rechazo = DaoMotivoRechazo.actualizar(id, parametros)

  if motivo_rechazo:
    respuesta['ok'] = True

  return jsonify(respuesta)

@motico_rechazo_servicio.route('/motivo-rechazo/agregar')
def motivoRechazoAgregar():

  parametros = {}
  respuesta = {'ok' : False}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)

  motivo_rechazo = DaoMotivoRechazo.crear(parametros)

  if motivo_rechazo:
    respuesta['ok'] = True

  return jsonify(respuesta)
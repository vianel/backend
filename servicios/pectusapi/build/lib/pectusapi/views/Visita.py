from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoVisita import DaoVisita
from pectusapi.schemas.Schema import VisitaSchema, serializar_a_json

visita_servicio = Blueprint('visita_servicio', __name__)

@visita_servicio.route('/visita/buscar')
def clinicaBuscar():

  parametros = {}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)

  visitas = DaoVisita.buscarPorArgumentos(parametros)

  return serializar_a_json(VisitaSchema, 'visitas', visitas, muchos=True)

@visita_servicio.route('/visita/todos')
def clinicaTodos():
  visitas = DaoVisita.buscarTodos()
  return serializar_a_json(VisitaSchema, 'visitas', visitas)

@visita_servicio.route('/visita/editar')
def clinicaEditar():
  id = request.args.get('id')
  parametros = dict()
  respuesta = {'ok' : False}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)
      
  visita = DaoVisita.actualizar(id, parametros)

  if visita:
    respuesta['ok'] = True

  return jsonify(respuesta)

@visita_servicio.route('/visita/agregar')
def estudioAgregar():

  parametros = {}
  respuesta = {'ok' : False}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)

  visita = DaoVisita.crear(parametros)

  if visita:
    respuesta['ok'] = True

  return jsonify(respuesta)
from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoTipoActividad import DaoTipoActividad
from pectusapi.schemas.Schema import TipoActividadSchema, serializar_a_json

tipo_actividad_servicio = Blueprint('tipo_actividad_servicio', __name__)

@tipo_actividad_servicio.route('/tipo-actividad/todos')
def tActiTodos():
  tipo_actividades = DaoTipoActividad.buscarTodos()
  return serializar_a_json(TipoActividadSchema, 'tipoactividades', tipo_actividades)


@tipo_actividad_servicio.route('/tipo-actividad/agregar')
def tActiAgregar():

  parametros = {}
  respuesta = {'ok' : False}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)

  tipo_actividad = DaoTipoActividad.crear(parametros)

  if tipo_actividad:
    respuesta['ok'] = True

  return jsonify(respuesta)

@tipo_actividad_servicio.route('/tipo-actividad/editar')
def tActiEditar():
  id = request.args.get('id')
  parametros = dict()
  respuesta = {'ok' : False}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)
      
  tipo_actividad = DaoTipoActividad.actualizar(id, parametros)

  if tipo_actividad:
    respuesta['ok'] = True

  return jsonify(respuesta)

@tipo_actividad_servicio.route('/tipo-actividad/buscar')
def tActiBuscar():

  parametros = {}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)

  tipoactividad = DaoTipoActividad.buscarPorArgumentos(parametros)

  return serializar_a_json(TipoActividadSchema, 'tipoactividad', tipoactividad, muchos=True)
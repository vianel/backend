from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoSolicitudActividad import DaoSolicitudActividad
from pectusapi.daos.DaoActividadRechazada import DaoActividadRechazada
from pectusapi.schemas.Schema import SolicitudActividadSchema, ActividadRechazadaSchema, serializar_a_json

solicitud_actividad_servicio = Blueprint('solicitud_actividad_servicio', __name__)

@solicitud_actividad_servicio.route('/solicitud-actividad/todos')
def tActiTodos():
  solicitud_actividad = DaoSolicitudActividad.buscarTodos()
  return serializar_a_json(SolicitudActividadSchema, 'solicitudactividad', solicitud_actividad)


@solicitud_actividad_servicio.route('/solicitud-actividad/agregar')
def tActiAgregar():

  parametros = {}
  respuesta = {'ok' : False}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)

  solicitud_actividad = DaoSolicitudActividad.crear(parametros)

  if solicitud_actividad:
    respuesta['ok'] = True

  return jsonify(respuesta)

@solicitud_actividad_servicio.route('/solicitud-actividad/editar')
def tActiEditar():
  id = request.args.get('id')
  parametros = dict()
  respuesta = {'ok' : False}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)
      
  solicitud_actividad = DaoSolicitudActividad.actualizar(id, parametros)

  if solicitud_actividad:
    respuesta['ok'] = True

  return jsonify(respuesta)

@solicitud_actividad_servicio.route('/solicitud-actividad/buscar')
def tActiBuscar():

  parametros = {}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)

  solicitud_actividad = DaoSolicitudActividad.buscarPorArgumentos(parametros)

  return serializar_a_json(SolicitudActividadSchema, 'solicitudactividades', solicitud_actividad, muchos=True)

@solicitud_actividad_servicio.route('/solicitud-actividad/rechazar')
def rechazarSolicitudActi():
  parametros = {}
  respuesta = {'ok' : False}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)

  solicitud_actividad = DaoActividadRechazada.crear(parametros)

  if solicitud_actividad:
    respuesta['ok'] = True

  return jsonify(respuesta)

@solicitud_actividad_servicio.route('/solicitud-actividad/rechazadas/todos')
def solActiRechazadas():
  actividades = DaoActividadRechazada.buscarTodos()
  return serializar_a_json(ActividadRechazadaSchema, 'actividadesrechazadas', actividades)

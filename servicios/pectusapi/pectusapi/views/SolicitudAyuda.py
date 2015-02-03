from flask import jsonify, Blueprint, request

from datetime import datetime

from pectusapi.daos.DaoEstudio import DaoEstudio
from pectusapi.daos.DaoSolicitudAyuda import DaoSolicitudAyuda
from pectusapi.daos.DaoSolicitudRechazada import DaoSolicitudRechazada
from pectusapi.daos.DaoPatologia import DaoPatologia
from pectusapi.schemas.Schema import (
  SolicitudAyudaSchema, 
  SolicitudRechazadaSchema, 
  serializar_a_json
)

solicitud_ayuda_servicio = Blueprint('solicitud_ayuda_servicio', __name__)

_PARAMETROS_A_EXCLUIR = [
	'estudios'
]

@solicitud_ayuda_servicio.route('/solicitud-ayuda/todos')
def solAyuTodos():
	solicitudes = DaoSolicitudAyuda.buscarTodos()
	return serializar_a_json(SolicitudAyudaSchema, 'solicitudes', solicitudes)

@solicitud_ayuda_servicio.route('/solicitud-ayuda/agregar')
def solAyuCrear():

	parametros = {}
	estudios = []
	respuesta = {'ok': False}

	for key in request.args:
		if request.args.get(key) and not key in _PARAMETROS_A_EXCLUIR:
			parametros[key] = request.args.get(key)

	for idtipoestudio in request.args.get('estudios').split(','):
		estudio = DaoEstudio.buscarPorId(idtipoestudio)
		if estudio:
			estudios.append(estudio)

	parametros['estudios'] = estudios
	nueva_solicitud = DaoSolicitudAyuda.crear(dict(parametros.items() + {'estatus': 'S', 'fecsolicitud': datetime.now()}.items()))

	if nueva_solicitud:
		respuesta['ok'] = True

	return jsonify(respuesta)

@solicitud_ayuda_servicio.route('/solicitud-ayuda/aprobar-estudio')
def solAprobarEstudio():

	from datetime import datetime
	respuesta = dict(ok=False)

	idsolicitud = request.args.get('solicitud')

	parametros = {
		'porcaprobacion': request.args.get('porcaprobacion'),
		'fecaprobacion':  datetime.now(),
		'estatus': 'A'
	}

	solicitud = DaoSolicitudAyuda.actualizar(idsolicitud, parametros)

	if solicitud:
		respuesta['ok'] = True

	return jsonify(respuesta)

@solicitud_ayuda_servicio.route('/solicitud-ayuda/buscar')
def solBuscar():

  parametros = {}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)

  solicitudes = DaoSolicitudAyuda.buscarPorArgumentos(parametros)
  return serializar_a_json(SolicitudAyudaSchema, 'solicitudes', solicitudes, muchos=True)

@solicitud_ayuda_servicio.route('/solicitud-ayuda/rechazar')
def rechazarSolicitud():
  parametros = {}
  respuesta = {'ok' : False}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)

  from datetime import datetime

  parametros['fecharechazo'] = datetime.now()
  idsolicitudayuda = parametros['idsolicitudayuda']
  sol = DaoSolicitudAyuda.buscarPorId(idsolicitudayuda)

  if sol:
    solicitud_actividad = DaoSolicitudRechazada.crear(parametros)
    DaoSolicitudAyuda.actualizar(sol.id, {'estatus': 'R'})

    if solicitud_actividad:
      respuesta['ok'] = True

  return jsonify(respuesta)

@solicitud_ayuda_servicio.route('/solicitud-ayuda/rechazadas/todos')
def solAyudaRechazadas():
  solicitudes = DaoSolicitudRechazada.buscarTodos()
  return serializar_a_json(SolicitudRechazadaSchema, 'solicitudesrechazadas', solicitudes)


@solicitud_ayuda_servicio.route('/solicitud-ayuda/estadisticas/patologias/')
def patologiasEstadisticas():
  patologias_ = DaoPatologia.buscarTodos()
  solicitudes_ = DaoSolicitudAyuda.buscarTodos()
  patologias = dict()
  solicitudes = dict()

  for pt in patologias_:
    patologias[pt.id] = pt.nombre
    solicitudes[pt.nombre] = 0

  for sl in solicitudes_:
    solicitudes[patologias[sl.idpatologia]] += 1

  solicitudes['total'] = len(solicitudes_)

  return jsonify(patologias=solicitudes)

    


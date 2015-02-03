from pectusapi.App import app
from pectusapi.views.Paciente import paciente_servicio
from pectusapi.views.Usuario import usuario_servicio
from pectusapi.views.Tarea import tarea_servicio
from pectusapi.views.Modulo import modulo_servicio
from pectusapi.views.Grupo import grupo_servicio
from pectusapi.views.Evento import evento_servicio
from pectusapi.views.TipoSeguro import tipo_seguro_servicio
from pectusapi.views.Actividad import actividad_servicio
from pectusapi.views.Patrocinador import patrocinador_servicio
from pectusapi.views.Voluntario import voluntario_servicio
from pectusapi.views.SolicitudAyuda import solicitud_ayuda_servicio
from pectusapi.views.Clinica import clinica_servicio
from pectusapi.views.Estudio import estudio_servicio
from pectusapi.views.Patologia import patologia_servicio
from pectusapi.views.Ciudad import ciudad_servicio
from pectusapi.views.Estado import estado_servicio
from pectusapi.views.TipoEstudio import tipo_estudio_servicio
from pectusapi.views.Cita import cita_servicio
from pectusapi.views.Colaboracion import colaboracion_servicio
from pectusapi.views.TipoColaboracion import tipo_colaboracion_servicio
from pectusapi.views.Lugar import lugar_servicio
from pectusapi.views.TipoLugar import tipo_lugar_servicio
from pectusapi.views.Comision import comision_servicio
from pectusapi.views.Persona import persona_servicio
from pectusapi.views.TipoActividad import tipo_actividad_servicio
from pectusapi.views.SolicitudActividad import solicitud_actividad_servicio
from pectusapi.views.MotivoRechazo import motico_rechazo_servicio
from pectusapi.views.Causa import causa_servicio
from pectusapi.views.SeguridadFuncional import seguridad_funciona_servicio
from pectusapi.views.Visita import visita_servicio
from pectusapi.views.Operacion import operacion_servicio

__blue_prints = [
	paciente_servicio, usuario_servicio, tarea_servicio,modulo_servicio, grupo_servicio,
	actividad_servicio, patrocinador_servicio, solicitud_ayuda_servicio, clinica_servicio,
	estudio_servicio, patologia_servicio, ciudad_servicio, estado_servicio, tipo_estudio_servicio,
	voluntario_servicio, cita_servicio, colaboracion_servicio, tipo_colaboracion_servicio,
	lugar_servicio, tipo_lugar_servicio, comision_servicio, persona_servicio, causa_servicio,
  tipo_actividad_servicio, solicitud_actividad_servicio, motico_rechazo_servicio,
  seguridad_funciona_servicio, visita_servicio, evento_servicio, tipo_seguro_servicio,
  operacion_servicio,
]

if __name__ == '__main__':

	for bp in __blue_prints:
		app.register_blueprint(bp)

	app.run(debug=True, use_reloader=True)

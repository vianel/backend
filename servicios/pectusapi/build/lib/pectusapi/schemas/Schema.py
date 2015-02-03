from flask import jsonify
from marshmallow import Schema, fields

class ActividadEconomicaSchema(Schema):
	
	class Meta:
		fields = ('id', 'nombre', 'descripcion')

class MotivoRechazoSchema(Schema):

	class Meta:
		fields = ('id', 'nombre', 'tipo')

class CausaSchema(Schema):
	
	class Meta:
		fields = ('id', 'nombre', 'descripcion')

class ComisionSchema(Schema):

	class Meta:
		fields = ('id', 'nombre', 'descripcion')

class TipoActividadSchema(Schema):

	comision = fields.Nested(ComisionSchema)

	class Meta:
		fields = ('id', 'nombre', 'descripcion', 'comision')

class TipoColaboracionSchema(Schema):

	class Meta:
		fields = ('id', 'nombre')

class TipoEstudioSchema(Schema):

	class Meta:
		fields = ('id', 'nombre', 'descripcion')

class UsuarioSchema(Schema):

	class Meta:
		fields = ('login', 'clave')

class TareaSchema(Schema):

	class Meta:
		fields = ('id', 'nombre', 'descripcion')

class ModuloSchema(Schema):

	class Meta:
		fields = ('id', 'nombre', 'descripcion', 'ruta')

class GrupoSchema(Schema):

	class Meta:
		fields = ('id', 'nombre', 'descripcion')

class ClinicaSchema(Schema):

	class Meta:
		fields = ('rif', 'nombre', 'direccion', 'tlffijo')

class EstudioSchema(Schema):
	tipoestudio = fields.Nested(TipoEstudioSchema)
	clinica = fields.Nested(ClinicaSchema)

	class Meta:
		fields = ('id', 'tipoestudio', 'monto', 'clinica')

class TipoSeguroSchema(Schema):
	
	class Meta:
		fields = ('id', 'nombre', 'descripcion')

class EstadoSchema(Schema):
	
	class Meta:
		fields = ('id', 'nombre')

class CiudadSchema(Schema):

	estado = fields.Nested(EstadoSchema)
	
	class Meta:
		fields = ('id', 'nombre', 'estado')

class TipoLugarSchema(Schema):

	class Meta:
		fields = ('id', 'nombre', 'descripcion')

class LugarSchema(Schema):

	ciudad = fields.Nested(CiudadSchema)
	tipolugar = fields.Nested(TipoLugarSchema)
	
	class Meta:
		fields = ('id', 'nombre', 'direccion', 'ciudad', 'tipolugar', 'tlffijo', )

class PatologiaSchema(Schema):

	class Meta:
		fields = ('id', 'nombre', 'observacion')


class PersonaSchema(Schema):
	ciudad = fields.Nested(CiudadSchema)
	fecnacimiento = fields.Date()

	class Meta:
		fields = ('cedula', 'ciudad', 'nombre', 'apellido', 'correo', 'sexo', 'tlfcelular', 'tlffijo', 'edocivil', 'direccion', 'fecnacimiento', 'profesion', 'estatus', 'type')

class PacienteSchema(Schema):

	ciudad = fields.Nested(CiudadSchema)
	tiposeguro = fields.Nested(TipoSeguroSchema)
	
	class Meta:
		fields = ('cedula', 'nombre', 'apellido', 'login' ,'correo', 'tlftrabajo', 'lugtrabajo', 'dirtrabajo', 'nrohabitantes', 'tipovivienda', 'tenvivienda', 'precalquiler', 'direccion', 'ciudad', 'fecnacimiento', 'edocivil', 'cedconyugue', 'nombconyugue', 'apeconyugue', 'ocupconyugue', 'fecnacconyugue', 'tiposeguro' , 'tlfcelular', 'tlffijo' ,'nrohijos' ,'profesion','ingfamiliares','egrfamiliares', 'estatus')


class SolicitudAyudaSchemaSESchema(Schema):
	patologia = fields.Nested(PatologiaSchema, many=False)
	paciente = fields.Nested(PacienteSchema)
	causa = fields.Nested(CausaSchema)
	fecsolicitud = fields.Date()
	fecaprobacion = fields.Date()

	class Meta:
		fields=('id', 'patologia', 'observacion', 'causa', 'paciente', 'porcaprobacion', 'fecsolicitud', 'fecaprobacion', 'estatus')


class EstudioXSolicitudAyudaSchema(Schema):
	estudio = fields.Nested(EstudioSchema)
	solicitudayuda = fields.Nested(SolicitudAyudaSchemaSESchema)

	class Meta:
		fields=('id', 'estudio', 'solicitudayuda')


class SolicitudAyudaSchema(Schema):
	patologia = fields.Nested(PatologiaSchema, many=False)
	paciente = fields.Nested(PacienteSchema)
	causa = fields.Nested(CausaSchema)
	estudios = fields.Nested(EstudioSchema, many=True)
	fecaprobacion = fields.Date()


	class Meta:
		fields=('id', 'patologia', 'estudios', 'observacion', 'causa', 'fecaprobacion', 'fecsolicitud', 'paciente', 'porcaprobacion', 'fecsolicitud', 'estatus')


class VoluntarioSchema(Schema):
	ciudad = fields.Nested(CiudadSchema)
	fecnacimiento = fields.Date()
	
	class Meta:
		fields = ('cedula', 'ciudad', 'nombre', 'apellido', 'correo', 'sexo', 'tlfcelular', 'tlffijo', 'edocivil', 'direccion', 'fecnacimiento', 'profesion', 'estatus', 'lugtrabajo', 'cargo', 'dirtrabajo', 'referidopor', 'tlfoficina')

class PatrocinadorSchema(Schema):

	actividadeconomica = fields.Nested(ActividadEconomicaSchema, many=False)
	
	class Meta:
		fields = ('rif', 'nombre', 'direccion', 'tlffijo', 'actividadeconomica', 'tlfcelular', 'nombrerepresentante', 'tlfrepresentante', 'correorepresentante')


class ColaboracionSESchema(Schema):

	patrocinador = fields.Nested(PatrocinadorSchema, many=False)
	tipocolaboracion = fields.Nested(TipoColaboracionSchema, many=False)

	class Meta:
		fields = ('id', 'patrocinador', 'tipocolaboracion', 'idevento', 'cantidad', 'fecha')

class EventoSchema(Schema):
	colaboraciones = fields.Nested(ColaboracionSESchema, many=True)
	voluntarios = fields.Nested(VoluntarioSchema, many=True)
	lugar = fields.Nested(LugarSchema)
	
	class Meta:
		fields = ('id', 'nombre', 'fecha', 'descripcion', 'voluntarios', 'lugar', 'colaboraciones', 'costoentradas', 'cantentradasesperadasventa', 'montorecaudadoesperado', 'estatus')

class SolicitudActividadSchema(Schema):

	tipoactividad = fields.Nested(TipoActividadSchema)
	fecsolicitud = fields.Date()

	class Meta:
		fields = ('id', 'descripcion', 'tipoactividad', 'nombsolicitante', 'fecsolicitud', 'estatus')

class ActividadSchema(Schema):
	
	solicitudactividad = fields.Nested(SolicitudActividadSchema, many=False)
	lugar = fields.Nested(LugarSchema, many=False)

	class Meta:
		fields = ('id', 'fechainicio', 'titulo', 'lugar', 'fechafin', 'montoesperado', 'nroasistentesesperados', 'hora', 'recursosutilizados', 'descripcion', 'observaciones', 'monto', 'duracion', 'nroasistentes', 'descripcion', 'observaciones', 'solicitudactividad', 'estatus')

class PatologiaSchema(Schema):

	class Meta:
		fields = ('id', 'nombre', 'observacion')

class CitaSchema(Schema):
	estudioxsolicitudayuda = fields.Nested(EstudioXSolicitudAyudaSchema)

	class Meta:
		fields = ('id', 'fechaasignacion', 'estudioxsolicitudayuda', 'fechacita', 'fechaentregacomprobante', 'hora', 'idestudioxsolicitudayuda')


class EventoSCSchema(Schema):
	voluntarios = fields.Nested(VoluntarioSchema, many=True)
	lugar = fields.Nested(LugarSchema)
	
	class Meta:
		fields = ('id', 'nombre', 'fecha', 'descripcion', 'voluntarios', 'lugar', 'costoentradas', 'cantentradasesperadasventa', 'montorecaudadoesperado')

class ColaboracionCESchema(Schema):

	patrocinador = fields.Nested(PatrocinadorSchema, many=False)
	tipocolaboracion = fields.Nested(TipoColaboracionSchema, many=False)
	evento = fields.Nested(EventoSCSchema, many=False)

	class Meta:
		fields = ('id', 'patrocinador', 'tipocolaboracion', 'evento', 'cantidad', 'fecha',)

class ActividadRechazadaSchema(Schema):
	solicitudactividad = fields.Nested(SolicitudActividadSchema)
	motivorechazo = fields.Nested(MotivoRechazoSchema)

	class Meta:
		fields  = ('id', 'motivorechazo', 'solicitudactividad', 'observacion', 'codigo')

class SolicitudRechazadaSchema(Schema):
	motivorechazo = fields.Nested(MotivoRechazoSchema)
	solicitudayuda = fields.Nested(SolicitudAyudaSchemaSESchema)
	fecharechazo = fields.Date()

	class Meta:
		fields = ('id', 'motivorechazo', 'solicitudayuda', 'fecharechazo', 'descripcion')


class VisitaSchema(Schema):

	fecha = fields.Date()
	hora = fields.Time()
	persona = fields.Nested(PersonaSchema)

	class Meta:
		fields = ('id', 'codigo', 'persona', 'fecha', 'hora')

class ModuloXTareaSchema(Schema):

	modulo = fields.Nested(ModuloSchema)
	tarea = fields.Nested(TareaSchema)

	class Meta:
		fields = ('id', 'modulo', 'tarea')

class OperacionSchema(Schema):
	grupo = fields.Nested(GrupoSchema)
	moduloxtarea = fields.Nested(ModuloXTareaSchema)

	class Meta:
		fields = ('id', 'moduloxtarea', 'grupo')

def serializar_a_json(SchemaEntity, nombre, targets, muchos=True):

	respuesta = dict(ok=False)
	serializer = SchemaEntity(many=muchos)
	resultado = serializer.dump(targets)
	
	if (muchos and len(targets)) or (not muchos and targets):
		respuesta['ok'] = True
		respuesta[nombre] = resultado.data

	return jsonify(respuesta)

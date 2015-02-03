from pectusapi.App import db

EstudioXSolicitudAyudaTable = db.Table('estudioxsolicitudayuda',
	db.Column('id', db.Integer, primary_key=True),
	db.Column('idestudio', db.Integer, db.ForeignKey('estudio.id')),
	db.Column('idsolicitudayuda', db.Integer, db.ForeignKey('solicitudayuda.id')),
)

VoluntarioXComision = db.Table('voluntarioxcomision',
	db.Column('id', db.Integer, primary_key=True),
	db.Column('cedula', db.Integer, db.ForeignKey('voluntario.cedula')),
	db.Column('idcomision', db.Integer, db.ForeignKey('comision.id'))
)

VoluntarioXEvento = db.Table('voluntarioxevento',
	db.Column('id', db.Integer, primary_key=True),
	db.Column('cedula', db.Integer, db.ForeignKey('voluntario.cedula')),
	db.Column('idevento', db.Integer, db.ForeignKey('evento.id'))
)

VoluntarioXActividad = db.Table('voluntarioxactividad',
	db.Column('id', db.Integer, primary_key=True),
	db.Column('cedula', db.Integer, db.ForeignKey('voluntario.cedula')),
	db.Column('idactividad', db.Integer, db.ForeignKey('actividad.id'))
)

ModuloXTareas = db.Table('moduloxtarea',
	db.Column('id', db.Integer, primary_key=True),
	db.Column('idmodulo', db.Integer, db.ForeignKey('modulo.id')),
	db.Column('idtarea', db.Integer, db.ForeignKey('tarea.id')),
)

UsuarioXGrupos = db.Table('grupoxusuario',
	db.Column('id', db.Integer, primary_key=True),
	db.Column('login', db.Integer, db.ForeignKey('usuario.login')),
	db.Column('idgrupo', db.Integer, db.ForeignKey('group.id')),
)

class Usuario(db.Model):
	__tablename__ = 'usuario'

	login = db.Column(db.String, primary_key=True)
	clave = db.Column(db.String)
	paciente = db.relationship('Paciente')
	grupos = db.relationship('Grupo', secondary=UsuarioXGrupos, backref='Usuario')

class Persona(db.Model):

	__tablename__ = 'persona'

	cedula = db.Column('cedula', db.String, primary_key=True)
	idciudad = db.Column(db.Integer, db.ForeignKey('ciudad.id'))
	ciudad = db.relationship('Ciudad')
	nombre = db.Column(db.String)
	apellido = db.Column(db.String)
	tlfcelular = db.Column(db.String)
	tlffijo = db.Column(db.String)
	edocivil = db.Column(db.String)
	direccion = db.Column(db.String)
	correo = db.Column(db.String)
	fecnacimiento = db.Column(db.Date)
	sexo = db.Column(db.NCHAR)
	profesion = db.Column(db.String)
	estatus = db.Column(db.NCHAR)
	type = db.Column(db.String)
	paciente = db.relationship('Paciente')
	voluntario = db.relationship('Voluntario')

	__mapper_args__ = {
		'polymorphic_on': type,
		'polymorphic_identity':'persona'
	}


class Estado(db.Model):
	__tablename__ = 'estado'

	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String)
	ciudades = db.relationship('Ciudad')
	codigo = db.Column(db.String)

class Ciudad(db.Model):
	__tablename__ = 'ciudad'

	id = db.Column(db.Integer, primary_key=True)
	idestado = db.Column(db.Integer, db.ForeignKey('estado.id'))
	estado = db.relationship('Estado')
	nombre = db.Column(db.String)
	pacientes = db.relationship('Persona')
	lugares = db.relationship('Lugar')
	codigo = db.Column(db.String)

class TipoSeguro(db.Model):
	__tablename__ = 'tiposeguro'

	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String)
	descripcion = db.Column(db.String)
	pacientes = db.relationship('Paciente')
	codigo = db.Column(db.String)

class Paciente(Persona):
	__tablename__ = 'paciente'

	cedula = db.Column('cedula', db.Integer, db.ForeignKey('persona.cedula'), primary_key=True)
	login = db.Column(db.Integer, db.ForeignKey('usuario.login'))
	usuario = db.relationship('Usuario')
	idtiposeguro = db.Column(db.Integer, db.ForeignKey('tiposeguro.id'))
	tiposeguro = db.relationship('TipoSeguro')
	nrohijos = db.Column(db.Integer)
	cedconyugue = db.Column(db.String)
	nombconyugue = db.Column(db.String)
	dirtrabajo = db.Column(db.String)
	apeconyugue = db.Column(db.String)
	fecnacconyugue = db.Column(db.Date)
	segurosocial = db.Column(db.NCHAR)
	nombreseguroparticular = db.Column(db.String)
	tipovivienda = db.Column(db.String)
	nrohabitantes = db.Column(db.Integer)
	tenvivienda = db.Column(db.String)
	precalquiler = db.Column(db.Float)
	lugtrabajo = db.Column(db.String)
	ocupconyugue = db.Column(db.String)
	tlftrabajo = db.Column(db.String)
	ingfamiliares = db.Column(db.Float)
	egrfamiliares = db.Column(db.Float)
	solicitudes = db.relationship('SolicitudAyuda')

	__mapper_args__ = { 
		'polymorphic_identity':'paciente',
		'inherit_condition': (cedula == Persona.cedula) 
	}


class EstudioXSolicitudAyuda(db.Model):

	__tablename__ = 'estudioxsolicitudayuda'

	id = db.Column(db.Integer, primary_key=True)
	idestudio = db.Column(db.Integer, db.ForeignKey('estudio.id'))
	estudio = db.relationship('Estudio')
	idsolicitudayuda = db.Column(db.Integer, db.ForeignKey('solicitudayuda.id'))
	solicitudayuda = db.relationship('SolicitudAyuda')

	__table_args__ = {
	'extend_existing': True
	}

class Cita(db.Model):
	__tablename__ = 'cita'

	id = db.Column(db.Integer, primary_key=True)
	idestudioxsolicitudayuda = db.Column(db.Integer, db.ForeignKey('estudioxsolicitudayuda.id'))
	estudioxsolicitudayuda = db.relationship('EstudioXSolicitudAyuda')
	fechaasignacion = db.Column(db.Date)
	fechacita = db.Column(db.Date)
	fechaentregacomprobante = db.Column(db.Date)
	hora = db.Column(db.Time)
	estatus = db.Column(db.NCHAR)
	codigo = db.Column(db.String)

class Patologia(db.Model):
	__tablename__ = 'patologia'

	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String)
	observacion = db.Column(db.String)
	solicitudes_ayuda = db.relationship('SolicitudAyuda')
	codigo = db.Column(db.String)

class SolicitudAyuda(db.Model):
	__tablename__ = 'solicitudayuda'

	id = db.Column(db.Integer, primary_key=True)
	cedula = db.Column(db.Integer, db.ForeignKey('paciente.cedula'))
	paciente = db.relationship('Paciente')
	idpatologia = db.Column(db.Integer, db.ForeignKey('patologia.id'))
	patologia = db.relationship('Patologia')
	idcausa = db.Column(db.Integer, db.ForeignKey('causa.id'))
	causa = db.relationship('Causa')
	porcaprobacion = db.Column(db.Float)
	fecaprobacion = db.Column(db.Date)
	fecsolicitud = db.Column(db.Date)
	observacion = db.Column(db.String)
	codigo = db.Column(db.String)
	estatus = db.Column(db.NCHAR)
	estudios = db.relationship('Estudio', secondary=EstudioXSolicitudAyudaTable, backref='SolicitudAyuda')

class TipoEstudio(db.Model):
	__tablename__ = 'tipoestudio'

	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String)
	descripcion = db.Column(db.String)
	codigo = db.Column(db.String)

class Estudio(db.Model):
	__tablename__ = 'estudio'

	id = db.Column(db.Integer, primary_key=True)
	rif = db.Column(db.Integer, db.ForeignKey('clinica.rif'))
	clinica = db.relationship('Clinica')
	idtipoestudio = db.Column(db.Integer, db.ForeignKey('tipoestudio.id'))
	monto = db.Column(db.Float)
	tipoestudio = db.relationship('TipoEstudio')
	solicitudes_ayuda = db.relationship('SolicitudAyuda', secondary=EstudioXSolicitudAyudaTable, backref='Estudio')
	codigo = db.Column(db.String)	

class Voluntario(Persona):
	__tablename__ = 'voluntario'

	cedula = db.Column(db.Integer, db.ForeignKey('persona.cedula'), primary_key=True)
	login = db.Column(db.Integer, db.ForeignKey('usuario.login'))
	usuario = db.relationship('Usuario')
	cargo = db.Column(db.String)
	lugtrabajo = db.Column(db.String)
	tlfoficina = db.Column(db.String)
	dirtrabajo = db.Column(db.String)
	referidopor = db.Column(db.String)
	comisiones = db.relationship('Comision', secondary=VoluntarioXComision, backref='Voluntario')
	eventos = db.relationship('Evento', secondary=VoluntarioXEvento, backref='Voluntario')
	actividades = db.relationship('Actividad', secondary=VoluntarioXActividad, backref='Voluntario')

	__mapper_args__ = { 'polymorphic_identity':'voluntario'}

class Clinica(db.Model):
	__tablename__ = 'clinica'

	rif = db.Column(db.String, primary_key=True)
	nombre = db.Column(db.String)
	direccion = db.Column(db.String)
	tlffijo = db.Column(db.String)
	estudios = db.relationship('Estudio')

class TipoColaboracion(db.Model):
	__tablename__ = 'tipocolaboracion'

	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String)
	codigo = db.Column(db.String)

class Colaboracion(db.Model):

	__tablename__ = 'colaboracion'

	id = db.Column(db.Integer, primary_key=True)
	idevento = db.Column(db.Integer, db.ForeignKey('evento.id'))
	rif = db.Column(db.Integer, db.ForeignKey('patrocinador.rif'))
	idtipocolaboracion = db.Column(db.Integer, db.ForeignKey('tipocolaboracion.id'))
	cantidad = db.Column(db.Float)
	evento = db.relationship('Evento')
	fecha = db.Column(db.Date)
	patrocinador = db.relationship('Patrocinador')
	tipocolaboracion = db.relationship('TipoColaboracion')
	codigo = db.Column(db.String)

class Lugar(db.Model):
	__tablename__ = 'lugar'

	id = db.Column(db.Integer, primary_key=True)
	idciudad = db.Column(db.Integer, db.ForeignKey('ciudad.id'))
	idtipolugar = db.Column(db.Integer, db.ForeignKey('tipolugar.id'))
	tipolugar = db.relationship('TipoLugar')
	nombre = db.Column(db.String)
	tlffijo = db.Column(db.String)
	direccion = db.Column(db.String)
	ciudad = db.relationship('Ciudad')
	eventos = db.relationship('Evento')
	codigo = db.Column(db.String)

class Evento(db.Model):
	__tablename__ = 'evento'

	id = db.Column(db.Integer, primary_key=True)
	idlugar = db.Column(db.Integer, db.ForeignKey('lugar.id'))
	cantentradasesperadasventa = db.Column(db.Integer)
	montorecaudadoesperado = db.Column(db.Float)
	nombre = db.Column(db.String)
	descripcion = db.Column(db.String)
	fecha = db.Column(db.Date)
	observaciones = db.Column(db.String)
	costoentradas = db.Column(db.Float)
	estatus = db.Column(db.NCHAR)
	lugar = db.relationship('Lugar')
	colaboraciones = db.relationship('Colaboracion')
	voluntarios = db.relationship('Voluntario', secondary=VoluntarioXEvento, backref='Evento')
	codigo = db.Column(db.String)

class Patrocinador(db.Model):
	__tablename__ = 'patrocinador'

	rif = db.Column(db.String, primary_key=True)
	nombre = db.Column(db.String)
	idactividadeconomica = db.Column(db.Integer, db.ForeignKey('actividadeconomica.id'))
	actividadeconomica = db.relationship('ActividadEconomica')
	direccion = db.Column(db.String)
	tlffijo = db.Column(db.String)
	tlfcelular = db.Column(db.String)
	nombrerepresentante = db.Column(db.String)
	tlfrepresentante = db.Column(db.String)
	correorepresentante = db.Column(db.String)
	#eventos = db.relationship('Evento', secondary=PatrocinadorXEvento, backref='Patrocinador')

class ActividadEconomica(db.Model):
	__tablename__ = 'actividadeconomica'

	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String)
	descripcion = db.Column(db.String)
	patrocinadores = db.relationship('Patrocinador')
	codigo = db.Column(db.String)

class Causa(db.Model):
	__tablename__ = 'causa'

	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String)
	descripcion = db.Column(db.String)
	codigo = db.Column(db.String)

class SolicitudActividad(db.Model):
	__tablename__ = 'solicitudactividad'

	id = db.Column(db.Integer, primary_key=True)
	idtipoactividad = db.Column(db.Integer, db.ForeignKey('tipoactividad.id'))
	tipoactividad = db.relationship('TipoActividad')
	descripcion = db.Column(db.String)
	nombsolicitante = db.Column(db.String)
	telfsolicitante = db.Column(db.String)
	fecsolicitud = db.Column(db.Date)
	estatus = db.Column(db.NCHAR)
	codigo = db.Column(db.String)

class Actividad(db.Model):
	__tablename__ = 'actividad'

	id = db.Column(db.Integer, primary_key=True)
	idsolicitudactividad = db.Column(db.Integer, db.ForeignKey('solicitudactividad.id'))
	idlugar = db.Column(db.Integer, db.ForeignKey('lugar.id'))
	lugar = db.relationship('Lugar')
	solicitudactividad = db.relationship('SolicitudActividad')
	titulo = db.Column(db.String)
	fechainicio = db.Column(db.Date)
	fechafin = db.Column(db.Date)
	montoesperado = db.Column(db.Integer)
	nroasistentesesperados = db.Column(db.Integer)
	hora = db.Column(db.Time)
	recursosutilizados = db.Column(db.String)
	descripcion = db.Column(db.String)
	observaciones = db.Column(db.String)
	monto = db.Column(db.Float)
	duracion = db.Column(db.Time)
	nroasistentes =db.Column(db.Integer)
	descripcion = db.Column(db.String)
	observaciones = db.Column(db.String)
	estatus = db.Column(db.NCHAR)
	voluntarios = db.relationship('Voluntario', secondary=VoluntarioXActividad, backref='Actividad')
	codigo = db.Column(db.String)

class Publicacion(db.Model):
	__tablename__ = 'publicacion'

	id = db.Column(db.Integer, primary_key=True)
	login = db.Column(db.Integer, db.ForeignKey('usuario.login'))
	fecha = db.Column(db.Date)
	titulo = db.Column(db.String)
	informacion = db.Column(db.String)
	imagen = db.Column(db.LargeBinary)
	imagenes = db.relationship('Imagen')
	codigo = db.Column(db.String)

class Imagen(db.Model):
	__tablename__ = 'imagen'

	id = db.Column(db.Integer, primary_key=True)
	idpublicacon = db.Column(db.Integer, db.ForeignKey('publicacion.id'))
	nombre = db.Column(db.String)
	contenido = db.Column(db.String)
	codigo = db.Column(db.String)

class TipoLugar(db.Model):
	__tablename__ = 'tipolugar'

	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String)
	descripcion = db.Column(db.String)
	lugares = db.relationship('Lugar')
	codigo = db.Column(db.String)

class Comision(db.Model):
	__tablename__ = 'comision'

	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String)
	descripcion = db.Column(db.String)
	voluntarios = db.relationship('Voluntario', secondary=VoluntarioXComision, backref='Comision')
	codigo = db.Column(db.String)

class TipoActividad(db.Model):

	__tablename__ = 'tipoactividad'

	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String)
	descripcion = db.Column(db.String)
	idcomision = db.Column(db.Integer, db.ForeignKey('comision.id'))
	comision = db.relationship('Comision')
	codigo = db.Column(db.String)

class MotivoRechazo(db.Model):

	__tablename__ = 'motivorechazo'

	id = db.Column(db.Integer, primary_key=True)
	codigo = db.Column(db.String)
	nombre = db.Column(db.String)
	tipo = db.Column(db.String)
	codigo = db.Column(db.String)

class ResultadoAyuda(db.Model):

	__tablename__ = 'resultadoayuda'

	id = db.Column(db.Integer, primary_key=True)
	idcita = db.Column(db.Integer, db.ForeignKey('cita.id'))
	cita = db.relationship('Cita')
	resultado = db.Column(db.NCHAR)
	gradopatologia = db.Column(db.NCHAR)
	observacion = db.Column(db.String)
	codigo = db.Column(db.String)

class SolicitudRechazada(db.Model):

	__tablename__ = 'solicitudrechazada'

	id = db.Column(db.Integer, primary_key=True)
	idmotivorechazo = db.Column(db.Integer, db.ForeignKey('motivorechazo.id'))
	motivorechazo = db.relationship('MotivoRechazo')
	idsolicitudayuda = db.Column(db.Integer, db.ForeignKey('solicitudayuda.id'))
	solicitudactividad = db.relationship('SolicitudAyuda')
	fecharechazo = db.Column(db.Date)
	descripcion = db.Column(db.String)
	codigo = db.Column(db.String)

class ActividadRechazada(db.Model):

	__tablename__ = 'actividadrechazada'

	id = db.Column(db.Integer, primary_key=True)
	codigo = db.Column(db.String)
	idmotivorechazo = db.Column(db.Integer, db.ForeignKey('motivorechazo.id'))
	motivorechazo = db.relationship('MotivoRechazo')
	idsolicitudactividad = db.Column(db.Integer, db.ForeignKey('solicitudactividad.id'))
	solicitudactividad = db.relationship('SolicitudActividad')
	observacion = db.Column(db.String)

class Visita(db.Model):

	__tablename__ = 'visita'

	id = db.Column(db.Integer, primary_key=True)
	codigo = db.Column(db.String)
	fecha = db.Column(db.Date)
	hora = db.Column(db.Time)
	cedulapersona = db.Column(db.Integer, db.ForeignKey('persona.cedula'))
	persona = db.relationship('Persona')

# =============================================================================
# =============================================================================
# Seguridad Funcional
# =============================================================================
# =============================================================================


class Modulo(db.Model):

	__tablename__ = 'modulo'

	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String)
	descripcion = db.Column(db.String)
	ruta = db.Column(db.String)
	tareas = db.relationship('Tarea', secondary=ModuloXTareas, backref='Modulo')

class Tarea(db.Model):

	__tablename__ = 'tarea'

	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String)
	descripcion = db.Column(db.String)
	tareas = db.relationship('Modulo', secondary=ModuloXTareas, backref='Tarea')

class Grupo(db.Model):

	__tablename__ = 'grupo'

	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String)
	descripcion = db.Column(db.String)
	usuarios = db.relationship('Usuario', secondary=UsuarioXGrupos, backref='Grupo')

class ModuloXTarea(db.Model):

	__tablename__ = 'moduloxtarea'

	id = db.Column(db.Integer, primary_key=True)
	idtarea = db.Column(db.Integer, db.ForeignKey('tarea.id'))
	tarea = db.relationship('Tarea')
	idmodulo = db.Column(db.Integer, db.ForeignKey('modulo.id'))
	modulo = db.relationship('Modulo')

	__table_args__ = {
	'extend_existing': True
	}


class Operaciones(db.Model):

	__tablename__ = 'operaciones'

	id = db.Column(db.Integer, primary_key=True)
	idgrupo = db.Column(db.Integer, db.ForeignKey('grupo.id'))
	grupo = db.relationship('Grupo')
	idmoduloxtarea = db.Column(db.Integer, db.ForeignKey('moduloxtarea.id'))
	moduloxtarea = db.relationship('ModuloXTarea')

class GrupoXUsuario(db.Model):

	__tablename__ = 'grupoxusuario'

	id = db.Column(db.Integer, primary_key=True)
	idgrupo = db.Column(db.Integer, db.ForeignKey('grupo.id'))
	grupo = db.relationship('Grupo')
	login = db.Column(db.Integer, db.ForeignKey('usuario.login'))
	usuario = db.relationship('Usuario')

	__table_args__ = {
	'extend_existing': True
	}



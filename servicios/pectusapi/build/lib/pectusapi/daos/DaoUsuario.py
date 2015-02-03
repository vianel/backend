from pectusapi.App import db
from pectusapi.model.Model import Usuario
from pectusapi.daos.DaoGenerico import DaoGenerico
from pectusapi.daos.DaoGrupo import DaoGrupo
from pectusapi.daos.DaoOperaciones import DaoOperaciones



class DaoUsuario(DaoGenerico):

	__ENTIDAD__ = Usuario
	__IDENTIFICADOR__ = 'login'

	@classmethod
	def crear(self, parametros):
		return super(DaoUsuario, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoUsuario, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoUsuario, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoUsuario, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoUsuario, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoUsuario, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoUsuario, self).actualizar(self.__ENTIDAD__, id, parametros)

	@classmethod
	def agregarGrupo(self, usuario, grupo):
		result = db.engine.execute(
			"""INSERT INTO grupoxusuario(login, idgrupo) VALUES('""" + usuario.login + """', """ + str(grupo.id) + """)"""
		)

	@classmethod
	def permisos(self, usuario):

		perm = dict()
		lt = list()

		for grupo in usuario.grupos:
			perm[grupo.nombre] = {
				'idgrupo' : grupo.id,
				'modulos': dict()
			}
			operaciones = DaoOperaciones.buscarPorArgumentos({'idgrupo': grupo.id})
			for operacion in operaciones:
				perm[grupo.nombre]['modulos'][operacion.moduloxtarea.modulo.nombre] = {
					'idmodulo': operacion.moduloxtarea.modulo.id,
					'nombremodulo': operacion.moduloxtarea.modulo.nombre,
					'rutamodulo': operacion.moduloxtarea.modulo.ruta,
					'tareasmodulo': [dict(id=tarea.id, nombre=tarea.nombre) for tarea in operacion.moduloxtarea.modulo.tareas]
				}

			ax = list()

			for mod_, value in perm[grupo.nombre]['modulos'].iteritems():
				ax.append(value)

			perm[grupo.nombre]['modulos'] = ax

		for (key, value) in perm.iteritems():
			value['nombregrupo'] = key
			lt.append(value)

		return lt

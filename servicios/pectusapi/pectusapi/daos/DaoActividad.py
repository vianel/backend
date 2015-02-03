from pectusapi.App import db
from pectusapi.model.Model import Actividad
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoActividad(DaoGenerico):

	__ENTIDAD__ = Actividad

	@classmethod
	def crear(self, parametros):
		return super(DaoActividad, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoActividad, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoActividad, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoActividad, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoActividad, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoActividad, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoActividad, self).actualizar(self.__ENTIDAD__, id, parametros)

	@classmethod
	def agregarVoluntario(self, actividad, voluntario):
		result = db.engine.execute(
			"INSERT INTO voluntarioxactividad(idactividad, cedula) VALUES({}, {})".format(actividad.id, voluntario.cedula)
		)
from pectusapi.model.Model import SolicitudActividad
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoSolicitudActividad(DaoGenerico):

	__ENTIDAD__ = SolicitudActividad

	@classmethod
	def crear(self, parametros):
		return super(DaoSolicitudActividad, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoSolicitudActividad, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoSolicitudActividad, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoSolicitudActividad, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoSolicitudActividad, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoSolicitudActividad, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoSolicitudActividad, self).actualizar(self.__ENTIDAD__, id, parametros)
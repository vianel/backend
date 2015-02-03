from pectusapi.model.Model import SolicitudRechazada
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoSolicitudRechazada(DaoGenerico):

	__ENTIDAD__ = SolicitudRechazada

	@classmethod
	def crear(self, parametros):
		return super(DaoSolicitudRechazada, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoSolicitudRechazada, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoSolicitudRechazada, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoSolicitudRechazada, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoSolicitudRechazada, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoSolicitudRechazada, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoSolicitudRechazada, self).actualizar(self.__ENTIDAD__, id, parametros)
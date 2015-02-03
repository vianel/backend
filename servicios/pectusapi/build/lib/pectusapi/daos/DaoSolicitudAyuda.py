from pectusapi.model.Model import SolicitudAyuda
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoSolicitudAyuda(DaoGenerico):

	__ENTIDAD__ = SolicitudAyuda

	@classmethod
	def crear(self, parametros):
		return super(DaoSolicitudAyuda, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoSolicitudAyuda, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoSolicitudAyuda, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoSolicitudAyuda, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoSolicitudAyuda, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoSolicitudAyuda, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoSolicitudAyuda, self).actualizar(self.__ENTIDAD__, id, parametros)
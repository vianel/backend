from pectusapi.model.Model import ResultadoAyuda
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoResultadoAyuda(DaoGenerico):

	__ENTIDAD__ = ResultadoAyuda

	@classmethod
	def crear(self, parametros):
		return super(DaoResultadoAyuda, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoResultadoAyuda, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoResultadoAyuda, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoResultadoAyuda, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoResultadoAyuda, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoResultadoAyuda, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoResultadoAyuda, self).actualizar(self.__ENTIDAD__, id, parametros)
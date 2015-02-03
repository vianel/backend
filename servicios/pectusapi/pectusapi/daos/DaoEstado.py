from pectusapi.model.Model import Estado
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoEstado(DaoGenerico):

	__ENTIDAD__ = Estado

	@classmethod
	def crear(self, parametros):
		return super(DaoEstado, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoEstado, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoEstado, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoEstado, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoEstado, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoEstado, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoEstado, self).actualizar(self.__ENTIDAD__, parametros)
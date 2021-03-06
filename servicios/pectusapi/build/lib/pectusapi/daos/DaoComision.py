from pectusapi.model.Model import Comision
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoComision(DaoGenerico):

	__ENTIDAD__ = Comision

	@classmethod
	def crear(self, parametros):
		return super(DaoComision, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoComision, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoComision, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoComision, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoComision, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoComision, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoComision, self).actualizar(self.__ENTIDAD__, id, parametros)

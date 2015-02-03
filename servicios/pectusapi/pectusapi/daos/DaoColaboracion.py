from pectusapi.model.Model import Colaboracion
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoColaboracion(DaoGenerico):

	__ENTIDAD__ = Colaboracion

	@classmethod
	def crear(self, parametros):
		return super(DaoColaboracion, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoColaboracion, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoColaboracion, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoColaboracion, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoColaboracion, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoColaboracion, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoColaboracion, self).actualizar(self.__ENTIDAD__, id, parametros)

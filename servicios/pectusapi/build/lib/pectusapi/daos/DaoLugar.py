from pectusapi.model.Model import Lugar
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoLugar(DaoGenerico):

	__ENTIDAD__ = Lugar

	@classmethod
	def crear(self, parametros):
		return super(DaoLugar, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoLugar, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoLugar, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoLugar, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoLugar, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoLugar, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoLugar, self).actualizar(self.__ENTIDAD__, id, parametros)
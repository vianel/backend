from pectusapi.model.Model import Publicacion
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoPublicacion(DaoGenerico):

	__ENTIDAD__ = Publicacion

	@classmethod
	def crear(self, parametros):
		return super(DaoPublicacion, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoPublicacion, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoPublicacion, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoPublicacion, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoPublicacion, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoPublicacion, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoPublicacion, self).actualizar(self.__ENTIDAD__, id, parametros)

from pectusapi.model.Model import Imagen
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoImagen(DaoGenerico):

	__ENTIDAD__ = Imagen

	@classmethod
	def crear(self, parametros):
		return super(DaoImagen, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoImagen, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoImagen, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoImagen, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoImagen, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoImagen, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoImagen, self).actualizar(self.__ENTIDAD__, id, parametros)
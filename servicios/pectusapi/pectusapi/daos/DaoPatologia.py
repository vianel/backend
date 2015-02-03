from pectusapi.model.Model import Patologia
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoPatologia(DaoGenerico):

	__ENTIDAD__ = Patologia

	@classmethod
	def crear(self, parametros):
		return super(DaoPatologia, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoPatologia, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoPatologia, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoPatologia, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoPatologia, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoPatologia, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoPatologia, self).actualizar(self.__ENTIDAD__, id, parametros)

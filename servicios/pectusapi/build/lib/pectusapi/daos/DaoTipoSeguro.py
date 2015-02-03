from pectusapi.model.Model import TipoSeguro
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoTipoSeguro(DaoGenerico):

	__ENTIDAD__ = TipoSeguro

	@classmethod
	def crear(self, parametros):
		return super(DaoTipoSeguro, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoTipoSeguro, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoTipoSeguro, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoTipoSeguro, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoTipoSeguro, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoTipoSeguro, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoTipoSeguro, self).actualizar(self.__ENTIDAD__, id, parametros)
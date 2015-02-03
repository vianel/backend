from pectusapi.model.Model import TipoLugar
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoTipoLugar(DaoGenerico):

	__ENTIDAD__ = TipoLugar

	@classmethod
	def crear(self, parametros):
		return super(DaoTipoLugar, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoTipoLugar, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoTipoLugar, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoTipoLugar, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoTipoLugar, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoTipoLugar, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoTipoLugar, self).actualizar(self.__ENTIDAD__, id, parametros)
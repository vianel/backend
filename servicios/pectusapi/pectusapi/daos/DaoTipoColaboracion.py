from pectusapi.model.Model import TipoColaboracion
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoTipoColaboracion(DaoGenerico):

	__ENTIDAD__ = TipoColaboracion

	@classmethod
	def crear(self, parametros):
		return super(DaoTipoColaboracion, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoTipoColaboracion, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoTipoColaboracion, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoTipoColaboracion, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoTipoColaboracion, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoTipoColaboracion, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoTipoColaboracion, self).actualizar(self.__ENTIDAD__, id, parametros)
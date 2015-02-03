from pectusapi.model.Model import TipoEstudio
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoTipoEstudio(DaoGenerico):

	__ENTIDAD__ = TipoEstudio

	@classmethod
	def crear(self, parametros):
		return super(DaoTipoEstudio, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoTipoEstudio, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoTipoEstudio, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoTipoEstudio, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoTipoEstudio, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoTipoEstudio, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoTipoEstudio, self).actualizar(self.__ENTIDAD__, id, parametros)
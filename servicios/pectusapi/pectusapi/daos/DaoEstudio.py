from pectusapi.model.Model import Estudio
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoEstudio(DaoGenerico):

	__ENTIDAD__ = Estudio

	@classmethod
	def crear(self, parametros):
		return super(DaoEstudio, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoEstudio, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoEstudio, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoEstudio, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoEstudio, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoEstudio, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoEstudio, self).actualizar(self.__ENTIDAD__, id, parametros)
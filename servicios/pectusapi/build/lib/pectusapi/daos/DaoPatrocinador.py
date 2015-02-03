from pectusapi.model.Model import Patrocinador
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoPatrocinador(DaoGenerico):

	__ENTIDAD__ = Patrocinador

	@classmethod
	def crear(self, parametros):
		return super(DaoPatrocinador, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoPatrocinador, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoPatrocinador, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoPatrocinador, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoPatrocinador, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoPatrocinador, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoPatrocinador, self).actualizar(self.__ENTIDAD__, id, parametros)
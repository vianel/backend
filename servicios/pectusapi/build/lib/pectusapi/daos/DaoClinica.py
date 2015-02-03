from pectusapi.model.Model import Clinica
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoClinica(DaoGenerico):

	__ENTIDAD__ = Clinica
	__IDENTIFICADOR__ = 'rif'

	@classmethod
	def crear(self, parametros):
		return super(DaoClinica, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoClinica, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoClinica, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoClinica, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoClinica, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoClinica, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoClinica, self).actualizar(self.__ENTIDAD__, id, parametros)

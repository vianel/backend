from pectusapi.model.Model import Operaciones
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoOperaciones(DaoGenerico):

	__ENTIDAD__ = Operaciones

	@classmethod
	def crear(self, parametros):
		return super(DaoOperaciones, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoOperaciones, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoOperaciones, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoOperaciones, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoOperaciones, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoOperaciones, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoOperaciones, self).actualizar(self.__ENTIDAD__, id, parametros)
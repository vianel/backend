from pectusapi.model.Model import Diagnostico
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoDiagnostico(DaoGenerico):

	__ENTIDAD__ = Diagnostico

	@classmethod
	def crear(self, parametros):
		return super(DaoDiagnostico, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoDiagnostico, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoDiagnostico, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoDiagnostico, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoDiagnostico, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoDiagnostico, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoDiagnostico, self).actualizar(self.__ENTIDAD__, parametros)

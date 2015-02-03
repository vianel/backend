from pectusapi.model.Model import Paciente
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoPaciente(DaoGenerico):

	__ENTIDAD__ = Paciente
	__IDENTIFICADOR__ = 'cedula'

	@classmethod
	def crear(self, parametros):
		return super(DaoPaciente, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoPaciente, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoPaciente, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoPaciente, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoPaciente, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoPaciente, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoPaciente, self).actualizar(self.__ENTIDAD__, id, parametros)
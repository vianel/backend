from pectusapi.model.Model import Ciudad
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoCiudad(DaoGenerico):

	__ENTIDAD__ = Ciudad

	@classmethod
	def crear(self, parametros):
		return super(DaoCiudad, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoCiudad, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoCiudad, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoCiudad, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoCiudad, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoCiudad, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoCiudad, self).actualizar(self.__ENTIDAD__, id, parametros)

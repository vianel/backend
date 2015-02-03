from pectusapi.App import db
from pectusapi.model.Model import Modulo
from pectusapi.model.Model import ModuloXTarea
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoModulo(DaoGenerico):

	__ENTIDAD__ = Modulo

	@classmethod
	def crear(self, parametros):
		return super(DaoModulo, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoModulo, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoModulo, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoModulo, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoModulo, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoModulo, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoModulo, self).actualizar(self.__ENTIDAD__, id, parametros)

	@classmethod
	def agregarTarea(self, modulo, tarea):
		parametros = {'idmodulo': modulo.id, 'idtarea': tarea.id}
		return super(DaoModulo, self).crear(ModuloXTarea, parametros)
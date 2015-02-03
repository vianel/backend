from pectusapi.model.Model import Tarea
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoTarea(DaoGenerico):

	__ENTIDAD__ = Tarea

	@classmethod
	def crear(self, parametros):
		return super(DaoTarea, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoTarea, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoTarea, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoTarea, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoTarea, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoTarea, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoTarea, self).actualizar(self.__ENTIDAD__, id, parametros)
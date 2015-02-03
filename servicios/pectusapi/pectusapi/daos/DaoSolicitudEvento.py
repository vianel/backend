from pectusapi.model.Model import Evento
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoSolicitudEvento(DaoGenerico):

	__ENTIDAD__ = Evento

	@classmethod
	def crear(self, parametros):
		return super(DaoSolicitudEvento, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoSolicitudEvento, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoSolicitudEvento, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoSolicitudEvento, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoSolicitudEvento, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoSolicitudEvento, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoSolicitudEvento, self).actualizar(self.__ENTIDAD__, id, parametros)
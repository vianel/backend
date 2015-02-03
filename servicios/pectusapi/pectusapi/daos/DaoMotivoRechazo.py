from pectusapi.model.Model import MotivoRechazo
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoMotivoRechazo(DaoGenerico):

	__ENTIDAD__ = MotivoRechazo

	@classmethod
	def crear(self, parametros):
		return super(DaoMotivoRechazo, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoMotivoRechazo, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoMotivoRechazo, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoMotivoRechazo, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoMotivoRechazo, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoMotivoRechazo, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoMotivoRechazo, self).actualizar(self.__ENTIDAD__, id, parametros)
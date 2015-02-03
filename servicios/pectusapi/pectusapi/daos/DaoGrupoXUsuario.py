from pectusapi.model.Model import GrupoXUsuario
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoGrupoXUsuario(DaoGenerico):

	__ENTIDAD__ = GrupoXUsuario

	@classmethod
	def crear(self, parametros):
		return super(DaoGrupoXUsuario, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoGrupoXUsuario, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoGrupoXUsuario, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoGrupoXUsuario, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoGrupoXUsuario, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoGrupoXUsuario, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoGrupoXUsuario, self).actualizar(self.__ENTIDAD__, id, parametros)
from pectusapi.App import db
from pectusapi.model.Model import Voluntario
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoVoluntario(DaoGenerico):

	__ENTIDAD__ = Voluntario
	__IDENTIFICADOR__ = 'cedula'

	@classmethod
	def crear(self, parametros):
		return super(DaoVoluntario, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoVoluntario, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoVoluntario, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoVoluntario, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoVoluntario, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoVoluntario, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoVoluntario, self).actualizar(self.__ENTIDAD__, id, parametros)

	@classmethod
	def agregarComision(self, voluntario, comision):
		result = db.engine.execute(
			"INSERT INTO voluntarioxcomision(idcomision, cedula) VALUES({}, {})".format(comision.id, voluntario.cedula)
		)
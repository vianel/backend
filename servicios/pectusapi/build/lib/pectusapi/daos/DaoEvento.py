from pectusapi.App import db
from pectusapi.model.Model import Evento
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoEvento(DaoGenerico):

	__ENTIDAD__ = Evento

	@classmethod
	def crear(self, parametros):
		return super(DaoEvento, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoEvento, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoEvento, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoEvento, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoEvento, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoEvento, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoEvento, self).actualizar(self.__ENTIDAD__, id, parametros)

	@classmethod
	def agregarVoluntario(self, evento, voluntario):
		result = db.engine.execute(
			"INSERT INTO voluntarioxevento(idevento, cedula) VALUES({}, {})".format(evento.id, voluntario.cedula)
		)
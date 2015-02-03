from pectusapi.model.Model import Grupo
from pectusapi.daos.DaoGenerico import DaoGenerico
from pectusapi.daos.DaoOperaciones import DaoOperaciones

class DaoGrupo(DaoGenerico):

	__ENTIDAD__ = Grupo

	@classmethod
	def crear(self, parametros):
		return super(DaoGrupo, self).crear(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarPorId(self, id):
		return super(DaoGrupo, self).buscarPorId(self.__ENTIDAD__, id)

	@classmethod
	def buscarPorArgumentos(self, parametros):
		return super(DaoGrupo, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def buscarTodos(self):
		return super(DaoGrupo, self).buscarTodos(self.__ENTIDAD__)

	@classmethod
	def eliminarPorId(self, id):
		return super(DaoGrupo, self).buscarTodos(self.__ENTIDAD__, id)

	@classmethod
	def eliminarPorArgumentos(self, parametros):
		return super(DaoGrupo, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

	@classmethod
	def actualizar(self, id, parametros):
		return super(DaoGrupo, self).actualizar(self.__ENTIDAD__, id, parametros)

	@classmethod
	def modulos(self, grupo):
		perm = dict()
		lt = list()

		operaciones = DaoOperaciones.buscarPorArgumentos({'idgrupo': grupo.id})
		for operacion in operaciones:

			perm[operacion.moduloxtarea.modulo.id] = operacion.moduloxtarea.modulo


		for key in perm:
			lt.append({'id': key,
								'nombre': perm[key].nombre})

		return lt
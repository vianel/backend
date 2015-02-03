from pectusapi.model.Model import ActividadRechazada
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoActividadRechazada(DaoGenerico):

  __ENTIDAD__ = ActividadRechazada

  @classmethod
  def crear(self, parametros):
    return super(DaoActividadRechazada, self).crear(self.__ENTIDAD__, parametros)

  @classmethod
  def buscarPorId(self, id):
    return super(DaoActividadRechazada, self).buscarPorId(self.__ENTIDAD__, id)

  @classmethod
  def buscarPorArgumentos(self, parametros):
    return super(DaoActividadRechazada, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

  @classmethod
  def buscarTodos(self):
    return super(DaoActividadRechazada, self).buscarTodos(self.__ENTIDAD__)

  @classmethod
  def eliminarPorId(self, id):
    return super(DaoActividadRechazada, self).buscarTodos(self.__ENTIDAD__, id)

  @classmethod
  def eliminarPorArgumentos(self, parametros):
    return super(DaoActividadRechazada, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

  @classmethod
  def actualizar(self, id, parametros):
    return super(DaoActividadRechazada, self).actualizar(self.__ENTIDAD__, id, parametros)
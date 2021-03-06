from pectusapi.model.Model import TipoActividad
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoTipoActividad(DaoGenerico):

  __ENTIDAD__ = TipoActividad

  @classmethod
  def crear(self, parametros):
    return super(DaoTipoActividad, self).crear(self.__ENTIDAD__, parametros)

  @classmethod
  def buscarPorId(self, id):
    return super(DaoTipoActividad, self).buscarPorId(self.__ENTIDAD__, id)

  @classmethod
  def buscarPorArgumentos(self, parametros):
    return super(DaoTipoActividad, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

  @classmethod
  def buscarTodos(self):
    return super(DaoTipoActividad, self).buscarTodos(self.__ENTIDAD__)

  @classmethod
  def eliminarPorId(self, id):
    return super(DaoTipoActividad, self).buscarTodos(self.__ENTIDAD__, id)

  @classmethod
  def eliminarPorArgumentos(self, parametros):
    return super(DaoTipoActividad, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

  @classmethod
  def actualizar(self, id, parametros):
    return super(DaoTipoActividad, self).actualizar(self.__ENTIDAD__, id, parametros)
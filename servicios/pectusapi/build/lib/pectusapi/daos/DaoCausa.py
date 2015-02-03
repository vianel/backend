from pectusapi.model.Model import Causa
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoCausa(DaoGenerico):

  __ENTIDAD__ = Causa

  @classmethod
  def crear(self, parametros):
    return super(DaoCausa, self).crear(self.__ENTIDAD__, parametros)

  @classmethod
  def buscarPorId(self, id):
    return super(DaoCausa, self).buscarPorId(self.__ENTIDAD__, id)

  @classmethod
  def buscarPorArgumentos(self, parametros):
    return super(DaoCausa, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

  @classmethod
  def buscarTodos(self):
    return super(DaoCausa, self).buscarTodos(self.__ENTIDAD__)

  @classmethod
  def eliminarPorId(self, id):
    return super(DaoCausa, self).buscarTodos(self.__ENTIDAD__, id)

  @classmethod
  def eliminarPorArgumentos(self, parametros):
    return super(DaoCausa, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

  @classmethod
  def actualizar(self, id, parametros):
    return super(DaoCausa, self).actualizar(self.__ENTIDAD__, id, parametros)
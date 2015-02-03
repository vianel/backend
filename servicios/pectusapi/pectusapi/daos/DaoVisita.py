from pectusapi.model.Model import Visita
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoVisita(DaoGenerico):

  __ENTIDAD__ = Visita

  @classmethod
  def crear(self, parametros):
    return super(DaoVisita, self).crear(self.__ENTIDAD__, parametros)

  @classmethod
  def buscarPorId(self, id):
    return super(DaoVisita, self).buscarPorId(self.__ENTIDAD__, id)

  @classmethod
  def buscarPorArgumentos(self, parametros):
    return super(DaoVisita, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

  @classmethod
  def buscarTodos(self):
    return super(DaoVisita, self).buscarTodos(self.__ENTIDAD__)

  @classmethod
  def eliminarPorId(self, id):
    return super(DaoVisita, self).buscarTodos(self.__ENTIDAD__, id)

  @classmethod
  def eliminarPorArgumentos(self, parametros):
    return super(DaoVisita, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

  @classmethod
  def actualizar(self, id, parametros):
    return super(DaoVisita, self).actualizar(self.__ENTIDAD__, id, parametros)

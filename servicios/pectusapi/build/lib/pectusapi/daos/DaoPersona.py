from pectusapi.model.Model import Persona
from pectusapi.daos.DaoGenerico import DaoGenerico

class DaoPersona(DaoGenerico):

  __ENTIDAD__ = Persona
  __IDENTIFICADOR__ = 'cedula'

  @classmethod
  def crear(self, parametros):
    return super(DaoPersona, self).crear(self.__ENTIDAD__, parametros)

  @classmethod
  def buscarPorId(self, id):
    return super(DaoPersona, self).buscarPorId(self.__ENTIDAD__, id)

  @classmethod
  def buscarPorArgumentos(self, parametros):
    return super(DaoPersona, self).buscarPorArgumentos(self.__ENTIDAD__, parametros)

  @classmethod
  def buscarTodos(self):
    return super(DaoPersona, self).buscarTodos(self.__ENTIDAD__)

  @classmethod
  def eliminarPorId(self, id):
    return super(DaoPersona, self).buscarTodos(self.__ENTIDAD__, id)

  @classmethod
  def eliminarPorArgumentos(self, parametros):
    return super(DaoPersona, self).eliminarPorArgumentos(self.__ENTIDAD__, parametros)

  @classmethod
  def actualizar(self, id, parametros):
    return super(DaoPersona, self).actualizar(self.__ENTIDAD__, id, parametros)
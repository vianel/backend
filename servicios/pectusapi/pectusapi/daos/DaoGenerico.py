from pectusapi.App import app, db

class DaoGenerico(object):

	__IDENTIFICADOR__ = 'id'

	@classmethod
	def crear(self, Entity, parametros):

		ret = None

		
		nentidad = Entity()

		for key in parametros:
			setattr(nentidad, key, parametros[key])

		db.session.add(nentidad)
		db.session.commit()
		db.session.flush()
		ret = nentidad
		#except:
		#	app.logger.debug('Ha ocurrido un error')
			
		return ret

	@classmethod
	def buscarPorId(self, Entity, id):

		id_param = {
			self.__IDENTIFICADOR__ : id

		}

		return Entity.query.filter_by(**id_param).first()

	@classmethod
	def buscarPorArgumentos(self, Entity, parametros):
		return Entity.query.filter_by(**parametros).all()

	@classmethod
	def buscarTodos(self, Entity):
		return Entity.query.all()

	@classmethod
	def eliminarPorId(self, Entity, id):

		dentity.estatus = False
		db.session.merge(dentity)
		db.session.commit()

	@classmethod
	def eliminarPorArgumentos(self, Entity, parametros):

		dentities = Entity.query.filter_by(**parametros).all()

		for dentity in dentities:
			db.session.merge(dentity)
		
		db.session.commit()

	@classmethod
	def actualizar(self, Entity, id, parametros):

		id_param = { self.__IDENTIFICADOR__ : id }
		uentity = Entity.query.filter_by(**id_param).first()

		for key in parametros:
			setattr(uentity, key, parametros[key])

		db.session.merge(uentity)
		db.session.commit()

		return uentity
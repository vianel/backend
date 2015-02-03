from flask import jsonify, Blueprint, request

from pectusapi.daos.DaoTipoSeguro import DaoTipoSeguro
from pectusapi.schemas.Schema import TipoSeguroSchema, serializar_a_json

tipo_seguro_servicio = Blueprint('tipo_seguro_servicio', __name__)

@tipo_seguro_servicio.route('/tipo-seguro/todos')
def tipoSeguroTodos():
	seguros = DaoTipoSeguro.buscarTodos()
	return serializar_a_json(TipoSeguroSchema, 'tiposeguros', seguros)

@tipo_seguro_servicio.route('/tipo-seguro/buscar')
def tipoSeguroBuscar():

	parametros = {}

	for key in request.args:
		if request.args.get(key):
			parametros[key] = request.args.get(key)

	tipo_seguros = DaoTipoSeguro.buscarPorArgumentos(parametros)
	return serializar_a_json(TipoSeguroSchema, 'tiposeguros', tipo_seguros, muchos=True)

@tipo_seguro_servicio.route('/tipo-seguro/editar')
def tipoSeguroEditar():
  id = request.args.get('id')
  parametros = dict()
  respuesta = {'ok' : False}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)
      
  tipo_seguro = DaoTipoSeguro.actualizar(id, parametros)

  if tipo_seguro:
    respuesta['ok'] = True

  return jsonify(respuesta)

@tipo_seguro_servicio.route('/tipo-seguro/agregar')
def motivoRechazoAgregar():

  parametros = {}
  respuesta = {'ok' : False}

  for key in request.args:
    if request.args.get(key):
      parametros[key] = request.args.get(key)

  tipo_seguro = DaoTipoSeguro.crear(parametros)

  if tipo_seguro:
    respuesta['ok'] = True

  return jsonify(respuesta)
from flask import jsonify, Blueprint, request
from pectusapi.schemas.Schema import serializar_a_json

seguridad_funciona_servicio = Blueprint('seguridad_funciona_servicio', __name__)
from urlparse import parse_qs

def parsear_url_parametros (parametros_str):

  parametros = parse_qs(parametros_str)
  parametrosr = dict()

  for key, value in parametros.iteritems():
    if value:
      parametrosr[key] = value[0]

  return parametrosr

def encriptar(clave):
  import hashlib

  m = hashlib.md5()
  m.update(clave.encode('utf-8'))
  return m.hexdigest()
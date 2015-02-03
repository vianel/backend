import unittest
from pectusapi.daos.DaoPaciente import DaoPaciente

class TestPersona(unittest.TestCase):

	"""
	def test_creacion(self):
		count = len(DaoPaciente.buscarTodos())
		DaoPaciente.crear({
			'nombre': 'Nombre Test',
			'cedula': '20322361',
			'apellido': 'Apellido Test'
		})

		self.assertEqual(len(DaoPaciente.buscarTodos()), count + 1)

	def test_buscar_por_argumento(self):

		paciente = DaoPaciente.buscarPorArgumentos({
			'nombre': 'Nombre Test'
		})[0]

		self.assertEqual(paciente.nombre, 'Nombre Test')

	def test_buscar_todos(self):

		count = len(DaoPaciente.buscarTodos())

		self.assertEqual(count > 0, False)
	"""

	def test_buscar_por_id(self):

		paciente = DaoPaciente.buscarPorId('20322361')

		self.assertEqual(paciente.cedula, '20322361')
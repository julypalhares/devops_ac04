from unittest import TestCase
from com.juliana.Elevador import Elevador

class TestElevador(TestCase):

	def setUp(self):
		# Objeto elevador com capacidade de 5 pessoas e para um predio com 20 andares
		self.elevador = Elevador(5, 20)


def test_elevador1():
    self.assertEqual(elevador.andar_atual, 0, 'Deveria ser 0')
    self.assertEqual(elevador.quantidade_pessoas, 0, 'Deveria ser 0')

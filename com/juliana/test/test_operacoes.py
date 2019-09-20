from unittest import TestCase
from com.juliana.operacoes import operacoes

class TestOperacaoes(TestCase):
	def setUp(self):
		self._operacoes = operacoes ()
		
	def test_soma (self):
		self.assertEqual(self._operacoes.soma ([1,5]), 6, "Should be 6") 
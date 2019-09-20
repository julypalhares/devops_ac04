from unittest import TestCase
from com.juliana.operacoes import operacoes

class TestOperacaoes(TestCase):
	def setup(self):
		self.operacoes = operacoes ()
		
	def test_soma (self):
		self.assertEqual(self.operacoes.soma ([1,5]), 6, "Should be 6") 
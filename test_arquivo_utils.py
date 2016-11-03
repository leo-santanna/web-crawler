import os
import unittest
from arquivo_utils import *


class Arquivo_UtilsTests(unittest.TestCase):
	"""docstring for Arquivo_UtilsTests"""
	def test_gera_arquivo_csv(self):
		# Preparar
		arquivo = 'teste_arquivo.csv'
		nomes_campos = ['campo_1', 'campo_2']
		dados = [{'campo_1':'dado_1', 'campo_2':'dado_2'}]

		# Agir
		gerar_csv(arquivo, nomes_campos, dados)

		# Aferir
		arquivo_existe = os.path.isfile('teste_arquivo.csv')
		self.assertTrue(arquivo_existe)

		# Limpar
		os.remove('teste_arquivo.csv')
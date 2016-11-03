import unittest
from main import *


class MainTests(unittest.TestCase):
	"""docstring for MainTests"""
	def test_processa_lista_links_marcas(self):
		# Preparar
		url = 'http://www.epocacosmeticos.com.br/marcas'
		ocorreu_excecao = False

		# Agir
		try:
			obter_lista_links_marcas(url, None)
		except:
			ocorreu_excecao = True

		# Aferir
		self.assertFalse(ocorreu_excecao)

	def test_processa_lista_links_produtos(self):
		# Preparar
		url = 'http://www.epocacosmeticos.com.br/adidas'
		ocorreu_excecao = False

		# Agir
		try:
			obter_lista_links_marcas(url, None)
		except:
			ocorreu_excecao = True

		# Aferir
		self.assertFalse(ocorreu_excecao)

	def test_processa_dados_produto(self):
		# Preparar
		url = 'http://www.epocacosmeticos.com.br/pure-game-eau-de-toilette-adidas-perfume-masculino/p'
		urls_nao_processadas = []
		ocorreu_excecao = False

		# Agir
		try:
			obter_dados_produto(url, urls_nao_processadas, None)
		except:
			ocorreu_excecao = True

		# Aferir
		self.assertFalse(ocorreu_excecao)

	def test_processa_dados_produto_metodo_sincrono(self):
		# Preparar
		url = 'http://www.epocacosmeticos.com.br/pure-game-eau-de-toilette-adidas-perfume-masculino/p'
		ocorreu_excecao = False

		# Agir
		try:
			obter_dados_produto_sync(url)
		except:
			ocorreu_excecao = True

		# Aferir
		self.assertFalse(ocorreu_excecao)
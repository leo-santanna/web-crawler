import unittest
from http_utils import *


class Http_UtilsTests(unittest.TestCase):
	"""docstring for Http_UtilsTests"""
	def test_requests_retorna_pagina_quando_url_informada(self):
		# Preparar
		url = 'http://www.google.com.br'

		# Agir
		pagina = obter_url_requests(url)

		# Aferir
		self.assertIsNotNone(pagina)

	def test_aiohttp_retorna_pagina_quando_url_informada(self):
		# Preparar
		url = 'http://www.google.com.br'

		# Agir
		pagina = obter_url(url)

		# Aferir
		self.assertIsNotNone(pagina)
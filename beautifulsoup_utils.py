from bs4 import BeautifulSoup


# Retorna o objeto BeautifulSoup parseado
# referente à página informada
def parsear_pagina(pagina, limitador_parse):
    try:
        return BeautifulSoup(pagina, 'lxml', parse_only=limitador_parse)
    except Exception as e:
        raise e

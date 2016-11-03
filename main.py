import http_utils
import visual_utils
import arquivo_utils
import beautifulsoup_utils
import aiohttp
import asyncio
from tqdm import tqdm
from bs4 import SoupStrainer


# Variáveis globais
links_marcas = []
links_produtos = []
dados_produtos = []


# Analisa a página que contém todas as marcas da loja
# e retorna os links para as páginas de cada marca
@asyncio.coroutine
def obter_lista_links_marcas(url, connector):
    pagina = yield from http_utils.obter_url(url, compress=True, connector=connector)

    limitador_parse_pagina_marcas = SoupStrainer('div', class_='brandFilter')
    pagina_parseada = beautifulsoup_utils.parsear_pagina(
        pagina, limitador_parse_pagina_marcas)
    try:
        ancoras_marcas = pagina_parseada.find(
            'div', class_='brandFilter').find_all('a')

        for ancora in ancoras_marcas:
            links_marcas.append(ancora['href'])
    except Exception as e:
        raise e


# Analisa a página que contém todos os produtos da marca
# e retorna os links para as páginas de cada produto
@asyncio.coroutine
def obter_lista_links_produtos(url, connector):
    pagina = yield from http_utils.obter_url(url, compress=True, connector=connector)

    limitador_parse_pagina_produtos = SoupStrainer(
        'div', class_='prateleira vitrine interna')
    pagina_parseada = beautifulsoup_utils.parsear_pagina(
        pagina, limitador_parse_pagina_produtos)
    try:
        ancoras_produtos = pagina_parseada.find_all('a', class_='productImage')

        for ancora in ancoras_produtos:
            links_produtos.append(ancora['href'])
    except Exception as e:
        raise e


# Analisa a página que contém os detalhe do produto
# e retorna o dicionário com os dados relevantes
@asyncio.coroutine
def obter_dados_produto(url, urls_nao_processadas, connector):
    pagina = ""
    try:
        pagina = yield from http_utils.obter_url(url, compress=True, connector=connector)
    except Exception:
        urls_nao_processadas.append(url)
        pass

    if pagina != "":
        pagina_parseada = beautifulsoup_utils.parsear_pagina(pagina, None)
        try:
            titulo_pagina_produto = '< Não encontrado >'
            container_titulo_pagina_produto = pagina_parseada.find('title')
            if container_titulo_pagina_produto is not None:
                titulo_pagina_produto = container_titulo_pagina_produto.text

            nome_produto = '< Não encontrado >'
            container_nome_produto = pagina_parseada.find(
                'div', class_='productName')
            if container_nome_produto is not None:
                nome_produto = container_nome_produto.text

            dados = [{'titulo_pagina_produto': titulo_pagina_produto,
                  'nome_produto': nome_produto, 'url_produto': url}]

            dados_produtos.extend(dados)
        except Exception as e:
            raise e


# Processa a página com os dados do produto utilizando a biblioteca
# requests, ao invés da aiohttp
def obter_dados_produto_sync(url):
    pagina = http_utils.obter_url_requests(url)

    pagina_parseada = beautifulsoup_utils.parsear_pagina(pagina.text, None)
    try:
        titulo_pagina_produto = '< Não encontrado >'
        container_titulo_pagina_produto = pagina_parseada.find('title')
        if container_titulo_pagina_produto is not None:
            titulo_pagina_produto = container_titulo_pagina_produto.text

        nome_produto = '< Não encontrado >'
        container_nome_produto = pagina_parseada.find(
            'div', class_='productName')
        if container_nome_produto is not None:
            nome_produto = container_nome_produto.text

        dados = [{'titulo_pagina_produto': titulo_pagina_produto,
              'nome_produto': nome_produto, 'url_produto': url}]

        dados_produtos.extend(dados)
    except Exception as e:
        raise e


if __name__ == '__main__':

    url_todas_marcas = "http://www.epocacosmeticos.com.br/marcas"

    loop = asyncio.get_event_loop()
    connector = aiohttp.TCPConnector(
        loop=loop, force_close=True, conn_timeout=5)
    loop.run_until_complete(
        obter_lista_links_marcas(url_todas_marcas, connector))
    connector.close()

    if len(links_marcas) > 0:
        descricao_processo = 'Obtendo links para todos os produtos'
        loop = asyncio.get_event_loop()
        connector = aiohttp.TCPConnector(
            loop=loop, force_close=True, conn_timeout=10)
        processo_pagina_produtos = visual_utils.wait_with_progress(
            [obter_lista_links_produtos(url_marca, connector) for url_marca in links_marcas], descricao_processo)
        loop.run_until_complete(processo_pagina_produtos)
        connector.close()

        if len(links_produtos) > 0:
            urls_nao_processadas = []
            descricao_processo = 'Obtendo dados de todos os produtos'
            loop = asyncio.get_event_loop()
            connector = aiohttp.TCPConnector(
                loop=loop, force_close=True, conn_timeout=50)
            processo_pagina_produto = visual_utils.wait_with_progress(
                [obter_dados_produto(url_produto, urls_nao_processadas, connector) for url_produto in links_produtos], descricao_processo)
            loop.run_until_complete(processo_pagina_produto)
            connector.close()

            # Tratamento síncrono das URLs que não puderam ser processadas.
            # O processo será mais lento, porém garantirá o resultado.
            if len(urls_nao_processadas) > 0:
                descricao_processo = 'Obtendo dados dos produtos restantes sincronamente (mais lento)'
                for url_produto in tqdm(urls_nao_processadas, desc=descricao_processo):
                    obter_dados_produto_sync(url_produto)

            if len(dados_produtos) > 0:
                nomes_campos = ['titulo_pagina_produto',
                                'nome_produto', 'url_produto']
                arquivo = 'resultado.csv'
                arquivo_utils.gerar_csv(arquivo, nomes_campos, dados_produtos)

                print('Processamento concluído! Foram encontrados {0} produtos.'.format(
                    len(dados_produtos)))

import aiohttp
import asyncio
import requests


# Obtém a página através de requisição GET
@asyncio.coroutine
def obter_url(*args, **kwargs):
    data = ""
    try:
        yield from asyncio.sleep(1)
        response = yield from aiohttp.request('GET', *args, **kwargs)
    except Exception as exc:
        raise exc
    else:
        data = (yield from response.text())
        response.close()

    return data


# Obtém a página através de requisição GET utilizando a biblioteca requests
def obter_url_requests(url):
    try:
        return requests.get(url)
    except Exception as e:
        raise e

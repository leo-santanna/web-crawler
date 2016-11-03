# Web Crawler Época Cosméticos

Web Crawler desenvolvido em Python para obter informações de todos os produtos da loja virtual Época Cosméticos.

### Pré Requisitos

Linguagem

```
Python 3.4.3
```

Bibliotecas extras

```
BeautifulSoup 4
```
```
lxml
```
```
aiohttp
```
```
asyncio
```
```
Requests
```
```
tqdm
```

### Installing

Para que o crawler funcione é necessário instalar as bibliotecas externas das seguintes formas:

Instalando o BeautifulSoup4

```
pip install beautifulsoup4
```

Instalando o motor de parse lxml

```
pip install lxml
```

Instalando o aiohttp

```
pip install aiohttp
```

Instalando o asyncio

```
pip install asyncio
```

Instalando o Requests

```
pip install requests
```

Instalando a biblioteca para exibição de barra de progresso na execução do crawler (tqdm)

```
pip install tqdm
```

## Executando os testes

Para executar os testes unitários automatizados da aplicação, será necessário executar os seguintes arquivos:

```
python -m unittest test_arquivo_utils.py
```
```
python -m unittest test_beautifulsoup_utils.py
```
```
python -m unittest test_http_utils.py
```
```
python -m unittest test_main.py
```

### Detalhamento dos testes

Os testes são responsáveis pelas seguintes coberturas:

- test_arquivo_utils.py
Verifica se o arquivo .csv é gerado

- test_beautifulsoup_utils.py
Verifica se o parse da página é realizado com a url informada
Verifica se o parse da página é realizado com a url e limitador de parse informados

- test_http_utils.py
Verifica se a biblioteca aiohttp requisita a página por GET
Verifica se a biblioteca requests requisita a página por GET

- test_main.py
Verifica se as urls das marcas são obtidos da página de todas as marcas
Verifica se as urls dos produtos são obtidos da página de produtos
Verifica se a página de produtos é processada em busca dos dados necessários (forma assíncrona)
Verifica se a página de produtos é processada em busca dos dados necessários (forma síncrona)


## Execução

Para iniciar o crawler, basta executar o seguinte comando:

```
python main.py
```

Ao fim da execução, será gerado um arquivo "resultado.csv" com os dados obtidos. O arquivo estará na raiz do projeto.

## Autor

* **Leonardo Sant'Anna**


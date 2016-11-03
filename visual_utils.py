import asyncio
from tqdm import tqdm


# Coroutina para exibir barra de progresso durante processamentos
@asyncio.coroutine
def wait_with_progress(coros, descricao):
    for f in tqdm(asyncio.as_completed(coros), total=len(coros), desc=descricao):
        yield from f

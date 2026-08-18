import asyncio
from concurrent.futures import ThreadPoolExecutor

async def run_in_pool(func, *args):
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        return await loop.run_in_executor(pool, func, *args)

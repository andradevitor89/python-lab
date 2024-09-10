import asyncio
import trio
from print import print_async, print_async_trio, print_sync

def start_many_sync(count=1):
    for _ in range(count):
        print_sync()

async def start_many_async(count:int):
    tasks = [print_async() for _ in range(count)]
    results = await asyncio.gather(*tasks)


async def start_many_async_trio(count:int):

    async with trio.open_nursery() as nursery:
        for _ in range(count):
            nursery.start_soon(print_async_trio)



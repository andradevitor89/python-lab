import asyncio
import trio
from fetch import fetch_async, fetch_async_trio, fetch_sync

def start_many_sync(count=1):
    results=[]
    for i in range(count):
        results.append(fetch_sync(i+1))
    print("length of results", len(results))    


async def start_many_async(count:int):
    tasks = [fetch_async(i+1) for i in range(count)]
    results = await asyncio.gather(*tasks)
    print("length of results", len(results))    


async def start_many_async_trio(count:int):
    results = []
    async with trio.open_nursery() as nursery:
        for i in range(count):
            nursery.start_soon(fetch_async_trio, i+1, results)

    print("length of results", len(results))    



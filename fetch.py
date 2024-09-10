import asyncio
import aiohttp
import requests
import httpx
import trio

def fetch_sync(i:int)->str:
    print(f"Sync fetching pokemon {i}")
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}')
    name = response.json()["name"]
    print(f"Pokemon {i}: {name}")
    return name

async def fetch_async(i:int)->str:
    print(f"Async fetching pokemon {i}")
    try:    
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://pokeapi.co/api/v2/pokemon/{i}') as response:
                # When dealing with async code, it's important to await the method response
                # to give back control to the event loop.
                #  Event loop is a loop that runs async code and manages the execution of async code.
                name = (await response.json())["name"]
                print(f"Pokemon {i}: {name}")
                return name
    except asyncio.CancelledError as e:
        print("Task was cancelled")


async def fetch_async_trio(i:int,results:list[str])->str:
    print(f"Async fetching pokemon {i}")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f'https://pokeapi.co/api/v2/pokemon/{i}')
            name = response.json()['name']
            print(f"Pokemon {i}: {name}")
            results.append(name)
            return name
    except trio.Cancelled as e:
        print("Task was cancelled")
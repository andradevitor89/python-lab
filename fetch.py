import asyncio
import aiohttp
import requests


def fetch_sync(i: int) -> str:
    print(f"Sync fetching pokemon {i}")
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}')
    name = response.json()["name"]
    print(f"Pokemon {i}: {name}")
    return name


async def fetch_async(i: int) -> str:
    print(f"Async fetching pokemon {i}")
    async with aiohttp.ClientSession() as session:
        # Context switch
        async with session.get(f'https://pokeapi.co/api/v2/pokemon/{i}') as response:
            await asyncio.sleep(1)
            # When dealing with async code, it's important to await the method response
            # to give back control to the event loop.
            #  Event loop is a loop that runs async code and manages the execution of async code.
            name = (await response.json())["name"]  # Context switch
            print(f"Fetched pokemon {i}: {name}")
            return name


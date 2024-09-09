import aiohttp
import requests

def print_sync():
    response = requests.get('https://pokeapi.co/api/v2/pokemon/2')
    print(response.text[:10])

async def print_async():
    print("Starting async request")
    async with aiohttp.ClientSession() as session:
        async with session.get('https://pokeapi.co/api/v2/pokemon/2') as response:
            # When dealing with async code, it's important to await the method response
            # to give back control to the event loop.
            #  Event loop is a loop that runs async code and manages the execution of async code.
            text = await response.text()
            print(text[:10])


import asyncio
import aiohttp
import requests
import httpx
import trio

def print_sync()->str:
    response = requests.get('https://pokeapi.co/api/v2/pokemon/2')
    result = response.text[:10]
    print(result)
    return result

async def print_async()->str:
    print("Starting async request")
    try:    
        async with aiohttp.ClientSession() as session:
            async with session.get('https://pokeapi.co/api/v2/pokemon/2') as response:
                # When dealing with async code, it's important to await the method response
                # to give back control to the event loop.
                #  Event loop is a loop that runs async code and manages the execution of async code.
                text = await response.text()
                result = text[:10]
                print(result)
                return result
    except asyncio.CancelledError as e:
        print("Task was cancelled")


async def print_async_trio()->str:
    print("Starting async request")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get('https://pokeapi.co/api/v2/pokemon/2')
            result = response.text[:10]
            print(result)
            return result
    except trio.Cancelled as e:
        print("Task was cancelled")
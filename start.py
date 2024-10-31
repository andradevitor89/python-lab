import asyncio
from fetch import fetch_async, fetch_sync
import time


def timeit(func: callable) -> callable:
    async def async_wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result

    def sync_wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result

    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    else:
        return sync_wrapper


@timeit
def start_many_fetch_sync(count: int):
    results = []
    for i in range(count):
        results.append(fetch_sync(i+1))
    print("length of results", len(results))


@timeit
async def start_many_fetch_async(count: int):
    tasks = []
    #  TaskGroup automatically cancels all tasks if one fails and ensures all tasks are managed together.
    async with asyncio.TaskGroup() as g:
        tasks = [g.create_task(fetch_async(i + 1)) for i in range(count)]
        
    results = [task.result() for task in tasks]
    print("length of results", len(results))

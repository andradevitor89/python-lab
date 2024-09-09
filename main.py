import sys
import time
import asyncio
import trio
from start import start_many_async, start_many_sync

if __name__ == "__main__":
    args = sys.argv[1:]
    mode = args[0]
    count = int(args[1])
    if mode == "sync":
        time_start = time.time()
        start_many_sync(count=count)
        time_end = time.time()
        print(f"Time taken: {time_end - time_start}")   
        
    elif mode == "async":
        time_start = time.time()
        asyncio.run(start_many_async(count=count))
        time_end = time.time()
        print(f"Time taken: {time_end - time_start}")   

    elif mode == "trio":
        time_start = time.time()
        asyncio.run(start_many_async(count=count))
        time_end = time.time()
        print(f"Time taken: {time_end - time_start}")   

    elif mode == "trio":
        time_start = time.time()
        trio.run(start_many_async(count=count))
        time_end = time.time()
        print(f"Time taken: {time_end - time_start}")

import sys
import time
import asyncio
from start import start_many_fetch_async, start_many_fetch_sync
import threading


async def _another_async_task(count: int):
    for i in range(count):
        print(f"Running another async task {i +1}")
        await asyncio.sleep(0.3)
        print(f"Another async task {i + 1} completed.")


if __name__ == "__main__":
    args = sys.argv[1:]
    mode = args[0]
    count = int(args[1])
    try:
        if mode == "sync":
            start_many_fetch_sync(count=count)

        elif mode == "async":
            asyncio.run(start_many_fetch_async(count=count))

        elif mode == "async-multi-loops":
            def _run_start_many_async_event_loop():
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(start_many_fetch_async(count=count))
                loop.close()

            def _run_another_async_task_event_loop():
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(_another_async_task(count=count))
                loop.close()

            thread_1 = threading.Thread(
                target=_run_start_many_async_event_loop, name="Thread-1")
            thread_2 = threading.Thread(
                target=_run_another_async_task_event_loop, name="Thread-2")

            thread_1.start()
            thread_2.start()

            thread_1.join()
            thread_2.join()


    except Exception as e:
        print(f"Exception caught: {e}.")
        sys.exit(1)

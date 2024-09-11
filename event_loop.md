### Context ###
Say I need to 2 tasks: get tickets for a concert and text a friend.

In a synchronous model I would get tickets and then text my friend.

That's, however, not the **most efficient** way to do things.

### Multithread v Asynchronous ###
 
 - In a multithreaded model, I would clone myself and have one clone get tickets while I sends the message.
 - In an asynchronous model, I would get tickets and while I wait in line I would send the message.

[Show sync method for fetching Pokemon]

Asyncio is the most standard library for asynchronous programming in Python. It is widely adopted and supported, with many third-party libraries and frameworks built on top of it.

### Asychronous Programming with Asyncio ###

- Uses an event loop to manage the execution of asynchronous tasks in a single thread.
- Uses cooperative multitasking to switch between tasks. This means that tasks voluntarily yield control back to the event loop, allowing other tasks to run.

[Show async methods (fetch.py and start.py) for fetching Pokemon]

In main.py we can't simply call the async method because async methods can only be called from other async methods. So we need to use the `asyncio.run()` function to run the async method.
asyncio.run() starts an event loop, runs the async function, and then stops the event loop when the function is done.




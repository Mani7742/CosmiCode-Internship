# Create a program to use Python's asyncio library to
#  perform asynchronous I/O operations.

import asyncio

async def fetch_data(delay, name):
    print(f"Start fetching {name}...")
    await asyncio.sleep(delay)
    print(f"Finished fetching {name} after {delay} seconds.")
    return f"Data from {name}"

async def main():
    task1 = asyncio.create_task(fetch_data(2, "Resource 1"))
    task2 = asyncio.create_task(fetch_data(3, "Resource 2"))
    task3 = asyncio.create_task(fetch_data(1, "Resource 3"))

    results = await asyncio.gather(task1, task2, task3)
    print("Results:", results)
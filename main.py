
import asyncio
import random

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

async def yield_function(x): # async generator
    yield x

async def randon_numbers(count: int) -> list:
    data = []
    for i in range(count):
        await asyncio.sleep(2)
        data.append(random.randint(0, 10))
    return data

if __name__ == "__main__":
    # asyncio.run(main())
    data = asyncio.run(randon_numbers(3))
    print(data)

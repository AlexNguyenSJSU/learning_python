import asyncio
import time

async def output(sleep, text):
    await asyncio.sleep(sleep)
    print(text)

async def main():
    print(f"Started: {time.strftime('%X')}")
    await asyncio.gather(output(10, 'First'), output(5, 'Second'), output(3, 'Third'))
    print(f"Ended: {time.strftime('%X')}")

asyncio.run(main())

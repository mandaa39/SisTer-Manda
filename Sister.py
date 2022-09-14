import asyncio
import time
 
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
 
# Showing use of asyncio.run()
# Total runtime is 3 seconds
async def main1():
    print(f"started at {time.strftime('%X')}")
 
    await say_after(1, 'hello')
    await say_after(2, 'world')
 
    print(f"finished at {time.strftime('%X')}")
 
asyncio.run(main1())
 
async def main2():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))
 
    task2 = asyncio.create_task(
        say_after(2, 'world'))
 
    print(f"started at {time.strftime('%X')}")
 
    await task1
    await task2
 
    print(f"finished at {time.strftime('%X')}")
 
asyncio.run(main2())
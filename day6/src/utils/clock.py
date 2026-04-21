import asyncio
import time
async def create_clock():
    while True:
        print(time.strftime("%H:%M:%S", time.localtime()))
        """
        Pauses the execution of the current task for 1 second, allowing other tasks to run concurrently. This is useful for creating a clock that updates every second without blocking the entire program.
        """
        await asyncio.sleep(1)
if __name__ == "__main__":
    asyncio.run(create_clock())
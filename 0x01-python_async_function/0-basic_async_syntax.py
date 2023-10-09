#!/usr/bin/env python3
'''asyncronous input/output in python.'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''coroutine that waits for a given random delay time and returns it.
      args:
         max_delay (float, optional): The maximum delay in
                    seconds (inclusive). Default is 10.
      Returns:
         float: The random delay between 0 and max_delay (inclusive).
    '''
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

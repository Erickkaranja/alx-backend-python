#!/usr/bin/env python3
'''asyncronous input/output in python'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''spawns wait_random n times with a delay of max_delay
       args:
           n (int): number of times to spawn wait_random.
           max_delay (int): maximum delay of spawning wait_random.
       Returns:
           a list of floats generated from running wait_random.
    '''
    my_list: List[float] = []
    corotines = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(corotines):
        result = await task
        my_list.append(result)
    return my_list

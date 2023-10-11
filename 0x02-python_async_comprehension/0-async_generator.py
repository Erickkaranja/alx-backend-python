#!/usr/bin/env python3
'''asynchronous generators and comprehension.'''
from typing import Iterator
import random
import asyncio


async def async_generator() -> Iterator[float]:
    '''coroutine that loops 10 times and asynchronously sleep for 1 second.
       Returns:
            a random number between 0 and 10.
    '''
    my_list = []
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

#!/usr/bin/env python3
'''asyncronous input/output in python.'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''coroutine that waits for a given random delay time and returns it.'''
    x = random.uniform(0, max_delay)
    return x

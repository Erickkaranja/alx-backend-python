#!/usr/bin/env python3
'''asyncronous generators and comprehension.'''
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''collects 10 random numbers over async_generator.
       Returns:
           10 random numbers.
    '''
    return [number async for number in async_generator()][:10]

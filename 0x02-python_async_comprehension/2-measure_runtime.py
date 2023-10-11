#!/usr/bin/env python3
'''asyncronous generators and complehension.'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measures the runtime of four asyncronous function.
       Returns:
           time of operation.
    '''
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime

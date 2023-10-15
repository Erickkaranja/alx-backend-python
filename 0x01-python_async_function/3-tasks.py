#!/usr/bin/env python3
'''asyncronous input output in python.'''
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    '''creates asyncio task
       args:
           max_delay (int): input integer.
       Returns
           asyncronous function.
    '''

    return asyncio.create_task(wait_random(max_delay))

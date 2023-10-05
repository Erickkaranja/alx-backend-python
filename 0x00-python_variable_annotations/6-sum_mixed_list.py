#!/usr/bin/python3
'''implementing type annotations'''

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[float | int]]) -> float:
    '''calculates the sum of both integers and floats in mxd_lst
       args:
           mxd_list(list): a mixture of both integers and floats.
       return:
           returns: sum as a floating datatype .
    '''
    total = sum(mxd_lst)
    return float(total)

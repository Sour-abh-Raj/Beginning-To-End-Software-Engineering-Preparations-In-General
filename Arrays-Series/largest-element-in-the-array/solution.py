from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:

    # Write your code from here.
    curr_lar_el = arr[0]
    if (n==0):
        return []
    elif (n==1):
        return curr_lar_el
    else :
            for i in range(1, n):
                if arr[i] > curr_lar_el :
                    curr_lar_el = arr[i]
            return curr_lar_el

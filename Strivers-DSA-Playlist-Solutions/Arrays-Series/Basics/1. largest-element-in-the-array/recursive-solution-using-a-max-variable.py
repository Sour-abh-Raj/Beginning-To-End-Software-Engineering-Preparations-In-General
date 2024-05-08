from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:
    max = arr[0]
    for i in range(0, n):
        if (max < arr[i]):
            max = arr[i]
    return max

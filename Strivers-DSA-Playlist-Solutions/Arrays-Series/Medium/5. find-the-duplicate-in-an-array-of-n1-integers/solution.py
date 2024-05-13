# Solution using Floyd's Tortoise and Hare (Cycle Detection) Algorithm
# Time complexity: O(n)
# Space complexity: O(1)
# Runtime : 36ms

from typing import List
def findDuplicate(arr: List[int]) -> int:
    # Find the intersection point of the two runners.
    tortoise = arr[0]
    hare = arr[0]
    while True:
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]
        if tortoise == hare:
            break

    # Find the "entrance" to the cycle.
    ptr1 = arr[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = arr[ptr1]
        ptr2 = arr[ptr2]

    return ptr1


if __name__ == "__main__":
    arr = [1, 3, 4, 2, 3]
    print("The duplicate element is ", findDuplicate(arr))
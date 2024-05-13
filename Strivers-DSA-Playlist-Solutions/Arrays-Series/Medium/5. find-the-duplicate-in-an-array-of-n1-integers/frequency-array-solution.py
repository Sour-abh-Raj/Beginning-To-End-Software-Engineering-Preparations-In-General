from typing import List
def findDuplicate(arr: List[int]) -> int:
    n = len(arr)
    freq = [0] * (n + 1)
    for i in range(n):
        if freq[arr[i]] == 0:
            freq[arr[i]] += 1
        else:
            return arr[i]
    return 0


if __name__ == "__main__":
    arr = [1, 3, 4, 2, 3]
    print("The duplicate element is ", findDuplicate(arr))
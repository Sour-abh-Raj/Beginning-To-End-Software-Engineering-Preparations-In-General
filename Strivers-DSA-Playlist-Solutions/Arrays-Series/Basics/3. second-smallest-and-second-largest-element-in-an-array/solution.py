def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    if n < 2:
        return [-1]
    else:
        arr = [0, 0]
        large = float('-inf')
        sec_large = float('-inf')
        small = float('inf')
        sec_small = float('inf')
        
        for i in range(n):
            if (a[i] > large):
                sec_large = large
                large = a[i]
            elif (a[i] > sec_large and a[i] != large):
                sec_large = a[i]     
            if (a[i] < small):
                sec_small = small
                small = a[i]
            elif (a[i] < sec_small and a[i] != small):
                sec_small = a[i]
                
        arr[0] = sec_large
        arr[1] = sec_small
    return arr

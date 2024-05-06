def isSorted(n: int,  a: [int]) -> int:
    if (n==0 or n==1) :
        return 1
    elif (n==2):
        if (a[0] < a[1] or a[0] == a[1]) :
            return 1
        else :
            return 0
    else :
        el_1 = a[0]
        el_2 = a[1]
        for i in range(2,n) :
            if (el_1 > el_2) :
                return 0
            el_1 = el_2
            el_2 = a[i]
        return 1
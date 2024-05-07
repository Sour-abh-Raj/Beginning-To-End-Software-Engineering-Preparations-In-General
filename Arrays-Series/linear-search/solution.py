def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

def main():
    arr = [1, 2, 3, 4, 5]
    target = 4
    print(linear_search(arr, target))

if __name__ == "__main__":
    main()
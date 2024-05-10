class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        unique = set()
        dups = 0
        unique.add(nums[0])
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            for i in range(1, n):
                if nums[i] not in unique:
                    unique.add(nums[i])
                    nums[i - dups] = nums[i]
                else:
                    dups += 1
            for i in range(n - dups, n):
                nums[i] = '_'
            return len(unique)

if __name__ == '__main__':
    arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(arr))
    print(arr)
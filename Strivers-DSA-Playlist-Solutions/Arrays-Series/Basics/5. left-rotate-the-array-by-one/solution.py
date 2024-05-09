# This solution uses a more optimal approach to solve the problem.
# Since we only need to rotate the array by one, we can store the first element in a temporary variable and then shift all the elements of the array to the left by one.
# Finally, we can store the temporary variable in the last index of the array.
# This way we can find the solution with only using constant space.
# The time complexity of this solution is O(n) and the space complexity is O(1).
# This is the optimal solution for this problem.
# We solved this problem using a temporary variable because the problem statement specified that we only need to left rotate the array by one.
# If we need to left rotate the array by k elements, we can use the same approach but with a slight modification that would not require any extra space.
# But the time complexity would be O(n*k) in that case.
# So this solution is the optimal solution for this problem.
# You can find that solution at Arrays-Basic/1.%20left-rotate-the-array-by-k-elements/solution.py

def Solution(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp
    for i in range(n):
        arr[i] = temp
    return arr
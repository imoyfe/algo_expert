#Two Number Sum

arr = [-1, 6, 3, 11, 1, 5, -4, 8]


# O(nlog(n)) | O(1) space
def twoNumberSum(arr, targetSum):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        currSum = arr[left] + arr[right]
        if currSum == targetSum:
            return [arr[left], arr[right]]
        elif currSum < targetSum:
            left += 1
        elif currSum > targetSum:
            right -= 1
    return []

print(twoNumberSum(arr, 5)) # Play with targetNum
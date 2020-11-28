
def findThreeLargestNumbers(arr):
    max_three = [0]*3
    for val in arr:
        if val >= max_three[2]:
            max_three[0] = max_three[1]
            max_three[1] = max_three[2]
            max_three[2] = val
            
        elif val >= max_three[1]:
            max_three[0] = max_three[1]
            max_three[1] = val

        elif val >= max_three[0]:
            max_three[0] = val

    return max_three



#TO_DO: Create condition function (to escalate and update arrays of 4 or 5 max numbers.
def create_condition(num):
    pass

arr1 = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(findThreeLargestNumbers(arr1))
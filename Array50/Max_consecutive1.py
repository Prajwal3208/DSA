# Maximum consecutive one’s (or zeros) in a binary array
# Last Updated : 09 Jul, 2024
# Given a binary array, find the count of a maximum number of consecutive 1s present in the array.

# Examples : 

# Input: arr[] = {1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1}
# Output: 4
# Explanation: The maximum number of consecutive 1’s in the array is 4 from index 8-11.


# Input: arr[] = {0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1}
# Output: 1
# Explanation: The maximum number of consecutive 0’s in the array is 1 from index 0-1.


def consicative(arr):
    n = len(arr)
    count = 0
    result = 0
    for i in range(n):
        if arr[i] == 0:
            count = 0
        else:
            count += 1
            result = max(result,count)
    return result

arr = [1,1,1,0,1,0,1]
print(consicative(arr))
        

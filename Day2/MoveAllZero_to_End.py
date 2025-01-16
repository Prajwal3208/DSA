# You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

# Examples:

# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: There are three 0s that are moved to the end.
# Input: arr[] = [10, 20, 30]
# Output: [10, 20, 30]
# Explanation: No change in array as there are no 0s.
# Input: arr[] = [0, 0]
# Output: [0, 0]
# Explanation: No change in array as there are all 0s.
# Constraints:
# 1 ≤ arr.size() ≤ 105
# 0 ≤ arr[i] ≤ 105
# The code you provided is time-consuming because it involves removing elements from a list (`arr.remove(arr[i])`) and appending them to the end (`arr.append(0)`), both of which are inefficient when done repeatedly inside a loop.

# A more efficient approach is to use the **two-pointer technique** to move all the zeros to the end of the array in a single pass. Here's how you can do it:

# ### Optimized Code
# ```python
# class Solution:
#     def pushZerosToEnd(self, arr):
#         n = len(arr)
#         non_zero_index = 0  # Pointer to place the next non-zero element

#         # Traverse the array
#         for i in range(n):
#             if arr[i] != 0:
#                 # Swap the non-zero element with the element at non_zero_index
#                 arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
#                 non_zero_index += 1

#         return arr  # Return the modified array (if needed)
# ```

# ### Explanation
# 1. **Two Pointers**:
#    - `non_zero_index` keeps track of the position where the next non-zero element should be placed.
#    - `i` iterates through the array.

# 2. **Swap Non-Zero Elements**:
#    - If the current element (`arr[i]`) is non-zero, it is swapped with the element at `non_zero_index`, and `non_zero_index` is incremented.

# 3. **Efficiency**:
#    - Time Complexity: \(O(n)\), where \(n\) is the size of the array. Each element is processed only once.
#    - Space Complexity: \(O(1)\), as the operation is done in-place without using additional space.

# ### Example
# ```python
# arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
# solution = Solution()
# result = solution.pushZerosToEnd(arr)
# print(result)
# ```

# ### Output
# ```
# [1, 9, 8, 4, 2, 7, 6, 9, 0, 0, 0, 0, 0]
# ```

# This approach is faster and avoids the inefficiencies of repeatedly removing and appending elements.

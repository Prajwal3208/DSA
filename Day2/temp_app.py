    def pushZerosToEnd(self, arr):
        n = len(arr)
        non_zero_index = 0  # Pointer to place the next non-zero element

        # Traverse the array
        for i in range(n):
            if arr[i] != 0:
                # Swap the non-zero element with the element at non_zero_index
                arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
                non_zero_index += 1

        return arr  # Return the modified array (if needed)
      arr = [1,2,0,4,3,0,5,0]
      print(pushZerosToEnd(arr))

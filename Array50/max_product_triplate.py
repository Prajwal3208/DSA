def product_max3(arr):
    n = len(arr)
    if n < 3:
        return -1
    
    arr.sort()
    
    return max(arr[0]*arr[1]*arr[n-1],arr[n-1]*arr[n-2]*arr[n-3])

arr = [-10, -3, 5, 6, -20] 
print(product_max3(arr))

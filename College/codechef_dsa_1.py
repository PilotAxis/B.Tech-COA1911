def resize_array(arr):
    # Calculate the sum of the even and odd elements
    even_sum = sum(x for x in arr if x % 2 == 0)
    odd_sum = sum(x for x in arr if x % 2 != 0)
    
    # Append the negative of the sums to the array
    if even_sum != 0:
        arr.append(-even_sum)
    if odd_sum != 0:
        arr.append(-odd_sum)
    
    return arr

# Test the function
arr = [1, 2, 3, 4, 5]
print(resize_array(arr))  # Output: [1, 2, 3, 4, 5, -6, -9]

# Time Complexity: O(n)
# Space Complexity: O(n)

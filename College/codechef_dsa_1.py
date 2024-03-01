def resize_array(arr):
    even_sum = sum(x for x in arr if x % 2 == 0)
    odd_sum = sum(x for x in arr if x % 2 != 0)
    
    num_add = even_sum - odd_sum
    return num_add

arr = [1,2,3,4,5]
print(resize_array(arr))  

'''
1. Calculate the sum of even and odd numbers in the array: Iterate over the array and for each number, check if it is even or odd. If it's even, add it to the sum of even numbers. If it's odd, add it to the sum of odd numbers.
2. Find the difference between the sum of even and odd numbers: Subtract the sum of odd numbers from the sum of even numbers. The result is the number that needs to be added to the array to balance it.
'''
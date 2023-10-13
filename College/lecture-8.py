#1.
# By me
'''def chkprime(x):
    if x == 0 or x == 1 :
        return "not a prime nor composite"
    elif x%2!=0 or x == 2:
        return "a prime"
    else:
        return "not a prime"
num = int(input("Enter a number :"))
print("The number is", chkprime(num), 'number')'''
# By GPT
'''def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, (number**0.5) + 1):
        if number%i == 0:
            return False
    return True
try :
    num = int(input("Enter a number :"))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
except ValueError:
    print("Enter a valid integer.")
'''
#2.
'''def squarelst(lst):
    for i in range(1, 31):
        val = i**2
        lst.append(val)
    return lst
st = []
print(squarelst(st))
'''
#3.
'''def distinctlst(input_list):
    dlst = []
    for item in input_list:
        if item not in dlst:
            dlst.append(item)
    return dlst
lst = [1,2,3,2,3,4,4,4,1,2]
print("Unique List :", distinctlst(lst))
'''
#4.
'''def maximum(num1, num2, num3) :
    m = max(num1, num2, num3)
    return m
a = float(input("Enter a number :"))
b = float(input("Enter a number :"))
c = float(input("Enter a number :"))
print("Maximum is :", maximum(a, b, c))
'''
#5.
'''def count(st):
    u = 0
    l = 0
    for char in st:
        if char.isupper():
            u += 1
        elif char.islower():
            l += 1
    return u, l
string = "The country INDIA"
upper, lower = count(string)
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
'''
x = int(input("Enter a number :"))
y = int(input("Enter a number :"))
z = int(input("Enter a number :"))

sum1 = sum2 = 0

sum1 = x + y + z

if x != y and x != z:
    sum2 += x
elif y != x and y != z:
    sum2 += y
elif z != x and z != y:
    sum2 += z

print(sum1, sum2)
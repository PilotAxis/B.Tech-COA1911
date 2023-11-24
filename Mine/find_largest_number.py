x = int(input("Enter a number :"))
y = int(input("Enter a number :"))
z = int(input("Enter a number :"))
max = x
if x < y :
    max = y
elif y < z :
    max = z
elif x < z :
    max = z
print(max)

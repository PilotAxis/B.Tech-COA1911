num = int(input("Enter a number :"))
sum = 0
l = num + 1
for i in range(1, l):
    if i % 2 != 0 :
        sum += i
print("Sum is :", sum)

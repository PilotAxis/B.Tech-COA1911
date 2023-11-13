lst = [1, 2, 3, 1, 2, 3, 1, 2, 3]
lst1 = []
num = int(input("Enter a number to find the indices :"))
for i in range(0, len(lst)):
    if num == lst[i]:
        lst1.append(i)
print(lst1)
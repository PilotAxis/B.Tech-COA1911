#Case - 1
n1 = int(input("Enter a number :"))
n2 = int(input("Enter a number :"))
n3 = int(input("Enter a number :"))
print("Before swapping :", n1, n2, n3)
n1, n2, n3 = n2, n3, n1
print("After swapping :", n1, n2, n3)

#Case - 2
n1 = int(input("Enter a number :"))
n2 = int(input("Enter a number :"))
n3 = int(input("Enter a number :"))
print("Before swapping :", n1, n2, n3)
n1, n2, n3 = n1, n1+n2, n1+n2+n3
print("After swapping :", n1, n2, n3)
num = int(input("Enter a number :"))

lim = int(num/2) + 1

for i in range(2, lim):
    rem = num % i
    if rem == 0 :
        print("not Prime number")
        break
else:
    print("prime number")

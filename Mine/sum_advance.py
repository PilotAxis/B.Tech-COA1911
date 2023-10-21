count = sumn = 0
ans = "y"
while ans == "y":
    num = int(input("Enter a number :"))
    if num < 0 :
        print("Number inputed is below zero, Aborting!")
        break
    sumn += num
    count += 1
    ans = input("Want to continue press y otherwise n :")
else:
    print("You have entered", count, "numbers so far!")
print("Sum of numbers :", sumn)
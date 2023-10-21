n = int(input("Enter a number :"))
ctr = 1
sum_even = sum_odd = 0
while ctr <= n :
    if ctr % 2 == 0 :
        sum_even += ctr
        ctr += 1
    else:
        sum_odd += ctr
        ctr += 1
print("Sum of even numbers :", sum_even)
print("Sum of odd numbers :", sum_odd)
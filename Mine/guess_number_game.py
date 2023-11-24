import random

number = random.randint(10, 50)
ctr = 1
while ctr < 5 :
    guess = int(input("Enter a number :"))
    if guess == number :
        print("You Win!")
        break
    else:    
        ctr += 1

if not ctr < 5:
    print("You Lose!")
    print("Number was :", number)

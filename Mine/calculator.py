x = int(input("Enter a number :"))
y = int(input("Enter a number :"))

ch = input("Enter operator [+ - * / %] :")

result = 0

if ch == "+":
    result = x + y
elif ch == "-":
    result = x - y
elif ch == "*":
    result = x * y
elif ch == "/" :
    result = x/y
elif ch == "%":
    result = x%y

print(result)
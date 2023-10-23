import math
a, b, c = 17, 23, 30
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle :", area)
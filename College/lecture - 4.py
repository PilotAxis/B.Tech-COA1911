#1.
'''import math
num = int(input("Enter a number :"))
sq = math.sqrt(num)
print(sq)'''

#2.
"""base = float(input("Enter base :"))
height = float(input("Enter height :"))
area = 0.5*base*height
print("Area :", area)"""

#4.
"""tup = (1, 2, 3, 4, 5)
rev = tup[::-1]
print(rev)"""

'''tup = (1, 2, 3)
tup1 = (0, 4, 6)
tup2 = tup + tup1
print(tup2)'''

#5.
# Define sets for students who like Football, Cricket, and Hockey
Football = {'A', 'B', 'C', 'D'}
Cricket = {'B', 'D', 'E', 'F'}
Hockey = {'A', 'C', 'G', 'F'}

# a. Students who like both Football and Hockey
both_football_and_hockey = Football.intersection(Hockey)
print("Students who like both Football and Hockey:", both_football_and_hockey)

# b. Students who like only one of the three sports
only_football = Football.difference(Cricket, Hockey)
only_cricket = Cricket.difference(Football, Hockey)
only_hockey = Hockey.difference(Football, Cricket)
print("Students who like only Football:", only_football)
print("Students who like only Cricket:", only_cricket)
print("Students who like only Hockey:", only_hockey)

# Question 2 Write a program that totals every number between 10 and 50, and outputs the subtotal on a separate line. Example:
# 10
# 21
# 33
# etc...

total = 0

for x in range(10, 51, 1):
    total = total + x
    print(total)
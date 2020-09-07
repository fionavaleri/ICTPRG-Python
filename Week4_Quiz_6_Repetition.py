# Question 6 Write a program that can output the following shape to the console:
# xxxxx
# xxxxx
# xxxxx
# xxxxx
# xxxxx
# Please ensure that you only have the following print statements within your application:
# print("x", end='')
# print("")
# You will need to use two loops for this to work.

rows = int(input("Please enter the number of rows for the rectangle:" + " " ))
columns = int(input("Please enter the number of columns for the rectangle:" + " "))

if rows == columns:
    print("That's a square, try again")
    rows = int(input("Please enter the number of rows for the rectangle:" + " " ))
    columns = int(input("Please enter the number of columns for the rectangle:" + " "))

if rows != columns: 
    for x in range(rows):
        for y in range(columns):
            print('*', end = ' ')
        print()

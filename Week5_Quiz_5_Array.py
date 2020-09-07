# Write a program that can accept many numbers from the user, until they enter an x. Example:
# Enter a number: 5
# Enter a number: 9
# Enter a number: 3
# Enter a number: 12
# Enter a number: x
# You entered: [5, 9, 3, 12]

numlist = []
num = input("Please enter a number.  Press x to stop: ")
numlist.append(num)

while num != 'x':
    num = input("Please enter a number.  Press x to stop: ")
    if num != 'x':
        numlist.append(num)
    if num == 'x':
        print("You entered: ", numlist)

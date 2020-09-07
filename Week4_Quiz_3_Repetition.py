# Question 3 Write a program that keeps asking a user for a number, until the number is within the range of 50 and 70. Example:
# Enter a number: 42
# Not within range.
# Enter a number:53
# Within range.

range(50,71)

user = int(input("Please enter a number" + " "))

while user not in range(50,71):
    print("Not within range")
    user = int(input("Please enter a number" + " "))
if user in range(50,71):
        print("Within range")

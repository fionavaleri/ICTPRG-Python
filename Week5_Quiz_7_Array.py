# Write a program to ask the user for numbers, and then print any repeating numbers in a list. Example:
# Enter a number: 5
# Enter a number: 2
# Enter a number: 6
# Enter a number: 98
# Enter a number: 7
# Enter a number: 6
# Enter a number: 5
# Enter a number: x
# Repeating numbers: [5, 6]

nums = []

while True:
    num = input("Enter a number (press x to stop): ")
    if num == 'x':
        break
    else:
        nums.append(num)

repeat = []

for x in nums:
    if nums.count(x) > 1: 
        repeat.append(x)

print("Repeating Numbers: ", repeat)
# Write a program that asks the user for a large number, and then sums all of the digits in that number: Example:
# Enter a large number: 29834892
# Sum of the digits: 2 + 9 + 8 + 3 + 4 + 8 + 9 + 2 = 45
nums = input("Please enter a large number: ")

total = sum(int(num) for num in str(nums))
print("The sum of the numbers: " + "+".join(str(nums)) + "=" + str(total))
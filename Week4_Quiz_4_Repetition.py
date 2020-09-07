# Question 4 Write a program that counts from 0 to 25, outputting each number on the same line, separated by commas.

output = "0"

for x in range(0,26):
    output = output + "," + str(x)
print(output)

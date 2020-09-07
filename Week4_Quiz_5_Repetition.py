# Question 5 Write a program that keeps asking the user for a number, and adds it to a total. Ensure that pressing x stops entering numbers. Example:
# Enter some numbers (Press x to stop): 
# 1
# 3
# 66
# x
# Total: 70
# (Reference your algorithm made in the 'Introduction to Algorithms' Quiz)

total = 0
while True:
    number = input('Enter some numbers (Press x to stop): ')
    if number != 'x':
        total += int(number)
    else:
        print('Total: ' + str(total))
        break

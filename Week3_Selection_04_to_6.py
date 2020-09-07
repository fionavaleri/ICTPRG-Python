# 4 Strings are compared using the ASCII values A to Z are represented by numbers 65 to 90. 
# a to z are represented by 97 to 122
# Digits 0 to 9 are stored in memory as characters by numbers 48 to 57. 
# Blank space by 32
# What will be the output of this code?
# if ‘z’ < ‘a’:
#   print ("z is less than a”)
#else:
#   print("z is not less than a")

# Answer - z is not less than a

# 5 Write a program that asks the user for the salary and the time in the job. The minimum salary for the sanction of a bank loan is an annual salary of $50000 
# and the person has to be on the current job for at least 3 years. The program should decide whether the person can be given a loan. Use nested if statement with else. 
salary = int(input("What is your yearly salary?"))
job = int(input("How many years have you been in current job?"))

if salary >= 50000 and job >= 3:
    print("Congratulations - Loan approved")
else:
    print("Loan application unsuccessful")

# 6 Convert the code to if-elif-else statement
# If number == 10:
#    print(‘ten’)
# else:  
# if  number == 11:
#    print(‘Eleven’)
# else:
# if number ==  12:
#    print(‘Twelve’)
# else:
#    print(“ the number is unknown”)
number = int(input("Please enter a number"))
if number == 10:
    print("ten")
else:
    if number == 11:
        print("Eleven")
    if number == 12:
        print("Twelve")
    else:
        print("the number is unknown")
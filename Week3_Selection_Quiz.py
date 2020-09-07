# Question 1 Write a program that asks the user for their name, checks if their name is either "frank" or "george" and if it is, greet them by their name.
# (Reference your algorithm from the 'Introduction to Algorithms' Quiz)

#name = input("Please enter your name")
#if (name == "Frank" and "George"):
#    print("G'day" + " " + name)
#else:
#    print("Your name is not Frank or George!")

# Question 2 Write a program that asks the user for their year of birth, checks if they are of legal drinking age, and tells the user to come into the bar. Example:
# What is your Year of birth: 1995 
# You are: 25 Years old
# Come in and have a drink!
# or
# What is your Year of birth: 2003
# You are: 17 Years old
# Go away. Child.

#year = 2020
#birth = int(input("What year were you born?"))
#age = year - birth
#if age >= 18:
#    print("You are:" + " " + str(age))
#    print("Come in and have a drink!")
#else:
#    if age < 18:
#        print("You are:" + " " + str(age) + " " + "Years old")
#        print("Go away - You're too young!")

# Question 3 
# Write a program that could be used for an (unsecure) login, with a username and password. For example:
# Enter username: bob | Enter password: password1234 | Access Granted! | Enter username: frank | Enter password: invalidpass | Access Denied!

#username = input("Enter your username")
#password = input("Enter your password")

#if (username == 'Bob' and password == 'password1234') or (username == 'Fiona' and password == 'Python'):
#    print("Access Granted!")
#else:
#    print("Access Denied!")

# Question 4
# Copy and Modify Question 3, to support the following username password combinations:
#bob : password1234 | fred : happyPass122 | lock: passwithlock44 | Please ensure that the password only works with the corresponding username.

#username = input("Enter your username")
#password = input("Enter your password")

#if (username == 'bob' and password == 'password1234') or (username == 'fred' and password == 'happyPass122') or (username == 'lock' and password == 'passwithlock44'):
#    print("Access Granted!")
#else:
#    print("Access Denied!")

# Question 5 Write a program that can grade a student based upon a percentage grade. Example:
# What was your grade: 99 - You will receive a "High Distinction"
# High Distinction: 100-90 | Distinction: 89-80 | Credit: 79-70 | Pass: 69-50

grade = int(input("What was your grade?"))
Grade_A = 90
Grade_B = 80
Grade_C = 70
Grade_D = 50

if grade >= Grade_A:
    print("You will receive a High Distinction")
elif grade >= Grade_B:
    print("You will receive a Distinction" )
elif grade >= Grade_C:
    print("You will receive a Credit")
elif grade >= Grade_D:
    print("You will receive a Pass")
else:
    print("You have failed")
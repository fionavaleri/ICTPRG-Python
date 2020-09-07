# 1a Write an if statement that assigns 9 to x if y equals 20
y=20
if y == 20:
    x = 9
# 1b Write an if statement that assigns a value of 20 to x and if y is greater than 100. it gives a value of 40 to X.
x=20
if y > 100:
    x=40
else:
    x=20
####
x = 20
if y > 100:
    x = 40

# 2 Write a program that asks the user for three scores out of 100. It then calculates the average. If the average is greater than 90, congratulate the user. 
# Write a pseudocode before you write the Python program.
# request 3 inputs from user out of 100
# calculate the average of 3 inputs - need to ensure change string to integer to allow sum option
# if avg > 90 congratulate the user

score1 = int(input("Please enter your first score out of 100"))
score2 = int(input("Please enter your second score out of 100"))
score3 = int(input("Please enter your third score out of 100"))

avg = (score1 + score2 + score3)
if avg > 90:
    print("Congratulations!")

# 3 Write a program to compare two strings. Get a password from the user. If the password is “Rela238#” accept the password. 
# Otherwise inform the user that the password is incorrect. Set the password using a variable at the start of the program.
password = input("Please enter your password")
correctPass = "Rela238#"
if password == correctPass:
    print("Password Correct")
else:
    print("Invalid Password")

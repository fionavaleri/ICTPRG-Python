# Design a program which will ask the user to enter the date in the form dd/mm/yyyy. Example 23/08/2019
# The date will be printed like below:
# Date: 23
# Month : 08
# Year: 2019

date = input("Please enter the date in the following format, dd/mm/yyyy: ")
# originally had the below - print on separate lines, then tried using new line in 1 print - so simplfied
#print("Date: ", date[0:2])
#print("Month: ", date[3:5])
#print("Year: ", date[6:10])

print("Date: ",date[0:2],'\n'"Month: ", date[3:5],'\n'"Year: ", date[6:10])
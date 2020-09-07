# 7 Here is a code with many nested –if statements. The indentation is not correct. Rewrite the code such that the program works.
#if score >= A_score:
#    print(“Your grade is A”)
#elif:
#    score >= B_score
#        print(‘Your grade is B’)
#    else:
#        if score >= C_score:
#            print(‘your grade is C’)
#        else:
#            if score >= D_score:
#                print(‘Your grade is D’)
#            else:
#                print(‘your grade is F’)

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

# 8 Modify this program with the value for the different scores
# A_score = 90
# B_score = 80
# C_score = 70
# D_score = 60
# Anything below 60 is F (fail)
#A_score >= 90
#B_score >= 80 and <= 89
#C_score >= 70 and <= 79
#D_score >= 60 and <= 69
#F = < 60
#grade = int(input("What was your grade?"))
#Grade_A = 90
#Grade_B = 80
#Grade_C = 70
#Grade_D = 50
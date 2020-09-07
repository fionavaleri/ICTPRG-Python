# Take guesses from user for number between 1 and 25 and disply if greater/less than random number.  User has 7 guesses. 
# If number guessed correct, stop asking and show user the numbers they guessed
# If number less/more than then tell that add guess to list and tell how many guesses left

# num = 17 # user trying to guess (can this be a random generated number? - Yes found a random inbuilt option via google)
import random # random number generator
num = random.randint(1, 25)  

guesslist = [] # list to hold guesses
guesses = 0  # number of guesses/chances

# get guess from user
print("Let's play a guessing game. I'm thinking of a number between 1 and 25, you have 7 chances to guess the number.")
guess = int(input("Enter your Guess: ")) 

guesslist.append(guess) #add guess to guesslist - before commencing while loop
guesses += 1 # add guess to guesses count - before commencing while loop

# while loop to commence the guessing game and compare each guess to the random number
while guesses < 7:  
        
    if guess == num: # if guess by user is same as num, break from loop, print win and tell how many guesses it took and what guesses were 
        print("Damn. You win!",'\n'"The number was indeed", num,'\n'"You guessed in",len(guesslist) ,"guesses",'\n'"Your guess log:",'\n',guesslist)
        break
    
    elif guess < num:  # check if guess is less than num, if is, ask for another guess and tell how many guesses left
        print("Nope, its greater than that",'\n'"You have ",str(7-(len(guesslist))), "guesses left!")
        guess = (int(input("Enter your Guess: ")))
    
    elif guess > num:  # check if guess is more than num,if is, ask for another guess and tell how many guesses left    
        print("Nope, its less than that",'\n'"You have ",str(7-(len(guesslist))), "guesses left!")
        guess = (int(input("Enter your Guess: ")))

    guesslist.append(guess) # add guess to guesslist after each pass through the loop
    guesses += 1  # add 1 to each guess try after each pass through the loop

if guesses == 7:  # if 7 guesses used, ends loop with cheeky text and provides the correct num and what is in the guesslist
    print("You have 0 guesses left!",'\n'"Ah Ha Ha Ha YOU LOSE!",'\n'"The number was",num, "you fool.",'\n'"Your guess log: ",'\n',guesslist)

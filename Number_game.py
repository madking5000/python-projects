import random
import math 

lower = int(input("Enter the Lower bound: "))

upper = int(input("Enter the upper bound: "))


#generating the random number between the upper and lower 

x = random.randint(lower, upper)

print("\n\tYou've only ", 
      round(math.log(upper - lower + 1, 3)), 
" Chances to guess the integer!\n")


#initializing the number of guesses 
count = 0 

while count < math.log(upper - lower +1, 3):
    count += 1
    #take a guessing number as input 

    guess = int(input("Guess a number:  "))

    #condition testing 

    if x == guess: 
        print ("Congratulations you did it in ", count, "Try")

        #once guessed, the looop will break 
        break
    elif x > guess:
        print(" You guessed too small")

    elif x < guess: 
        print("you guessed too High!")


#if guessing is more than required guesses, shows the output 
        

if count >= math.log(upper - lower + 1, 3):
    print("\nThe number is %d" % x)
    print('\tBetter luck next time!')
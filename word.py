import random 

#library that we use in order to choose 
#on random words from a list of words

name = input("what is your name: ")

#the user is asked to enter the name first 

print("Good luck! ", name)

words = [ 'rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 
         'reverse', 'water', 'board', 'geeks']

#function will choice one random word from a list of words

word = random.choice(words)

print("guess the characters")

guesses = ''

#any number of turns that can be used here 

turns = 12

while turns > 0:
    
    #counts the number of users fails

    failed = 0

    #all characters from the input, word taking one at a time

    for char in word:

        #comparing that character with the character in guesses 
        if char in guesses:
            print(char, end="")

        else:
            print("_")
            #for every failure 1 will be incremeted in  failure 
            failed += 1

    if failed == 0:
        #user will wil the game if failure is 0
        #and "you win" will be given as an output 
        print("you win")

        #this prints the correct word
        print("The word is: ", word)
        break


    #if user has input the wrong alphabet the it will ask user to enter another alphabet 

    print()
    guess = input("Guess a character: ")


    #every input character will be stored in guesses 
    guesses += guess 

    #check input the character in word 

    if guess is not word:
        turns -=1 

        #if the character doesnt match the word
        # then wrong will be given as output 

        print("wrong")

        #this will print the number of turns left for the user 

        print("You have ", + turns, "more guesses")

        if turns == 0:
            print("You loose")








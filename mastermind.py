import random
#creating display function for displaying instructions
def disp():
    #printing the greeting and instruction for the gamer
    print(" ~ Welcome to Mastermind Game ~~~")
    print("Hi gamer, welcome to the Mastermind game ")
    name = input ("What is your name? ")
    print ("Hello, " +name+ ",Please follow the given instruction to play the game.")
    print ("""         ~~~GAME INSTRUCTION~~~
     I am thinking of a 3-digit number. Try to guess what it is.
     Here are some clues:
     When I say:         That means:
     Yellow              One digit is correct but in the wrong position.
     Green               One digit is correct and in the right position.
     Red                 No digit is correct.""")

#function for generating random number
def getsecret_num(numDigits):
    num = list(range(10))
    random.shuffle(num)
    secret_num = ''
    for i in range(numDigits):
        secret_num += str(num[i])
    return secret_num

#funtion for clues
def getClues(guess, secret_num):
    if guess == secret_num:
        return 'Congratulation! You got it!'
    clue = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clue.append('Green')
        elif guess[i] in secret_num:
            clue.append('Yellow')
    if len(clue) == 0:
        return 'Red'
    clue.sort()
    return ' '.join(clue)

#function for check the number
def isOnlyDigits(num):
    if num == '':
        return False
    
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            print ("Invalid input!")
            return False
    return True

#function to play again
def playAgain():
    choice = str(input("Do you want to play again? (Y or N)"))
    if(choice.lower()=="y"):
        return choice.lower().startswith('y')
    elif(choice.lower()=="n"):
        print(" Thank you for playing. ")
    else:
        print(" Wrong Input. Please enter 'y' or 'n'. ")
        playAgain()


NUMDIGITS = 3
MAXGUESS = 10
disp()
while True:
    secret_num = getsecret_num(NUMDIGITS)
    print('I have thought of a number. You have %s guesses to guess it' %(MAXGUESS))
    numGuesses = 1
    while numGuesses <= MAXGUESS:
        guess = ''
        while len(guess) != NUMDIGITS or not isOnlyDigits(guess):
            print('Guess #%s: ' % (numGuesses))
            guess = input()
        clue = getClues(guess, secret_num)
        print(clue)
        numGuesses += 1
        if guess == secret_num:
            break
        if numGuesses > MAXGUESS:
            print('You ran out of guesses. The answer was %s. ' %(secret_num))
    if not playAgain():
        break

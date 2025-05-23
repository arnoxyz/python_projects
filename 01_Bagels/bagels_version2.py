# Different Implementation of the bagels game

# Implementation details:
# user input as string
# get values with [0][1][2]
# so there is string comparison instead of integer comparison

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print("Bagels")
    
    while True: 
        secretNum = getSecretNum()
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))
        numGuesses = 1

        while numGuesses < MAX_GUESSES:
            guess = ''
            while (len(guess) != NUM_DIGITS or not guess.isdecimal()):
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

                clues = getClues(guess, secretNum)
                print(clues)
                numGuesses += 1

                if guess == secretNum:
                    break
                if numGuesses > MAX_GUESSES:
                    print('You lost')
                    print('The answer was {}.'.format(secretNum))
            print('Play again? (Y/N)') 
            if not input('> ').lower().startswith('y'):
                break


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    main()

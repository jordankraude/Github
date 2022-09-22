import random
import time

with open("Parachute_game\wordlist.txt") as word_list:
    lines = word_list.readlines()

print('\nWelcome to Hangman!')
name = input('Enter your name: ')
print(f'Hello {name}! Best of Luck!')
time.sleep(2)
print("The game is about to start!\nLet's play Hangman!")
time.sleep(3)

word = random.choice(lines)
word_final = word.replace('\n', '')
guesses = []
turns = 10

while turns > 0:
    failed = 0
    for char in word_final:
        if char in guesses:
            print(f'{char}')
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("Congratulations! You Won!")
        break

    print('')
    valid = False
    while not valid:
        guess = input('Guess a letter: ').lower()
        if len(guess) > 1:
            valid = False
            print('Please make sure the guess is only "1" letter!')
        elif len(guess) == 0:
            valid = False
            print('Please make sure the guess is only "1" letter!')
        else:
            guesses += guess
            valid = True


    if guess not in word_final:
        turns -= 1
        print('Wrong!')
        print(f'You have {turns} more guesses')

    if turns == 0:
        print('You Lose')
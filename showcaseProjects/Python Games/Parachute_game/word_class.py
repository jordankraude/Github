import random

class Word:
    '''This initializes itself and opens a txt file to create a wordlist for itself.'''
    def __init__(self) -> None:
        self.guess_list = []
        with open("Parachute_game\wordlist.txt") as word_list:
            self._list = word_list.readlines()
        
        
    '''This function selects a word from the wordlist and seperates it into a seperate list where every
    character is its own place in the list that can be reached'''
    def _getword(self):
        self._word = random.choice(self._list)
        self._word_final = self._word.replace('\n', '')
        self._word_as_list = [char for char in self._word_final]

        return self._word_as_list
    
    def _guesses(self, guess):
        self.guess_list.append(guess)
        return self.guess_list



    ##def _updateDisplay(self, letter_guess):
    ##char = letter_guess
    ##    letters_left = 0
    ##    for char in self.word_final:
      ##      if char in self.guesses:
       ##         print(f'{char}')
         ##   else:
           ##     letters_left += 1
        
       ## if letters_left == 0:
         ##   print("Congratulations! You Won!")

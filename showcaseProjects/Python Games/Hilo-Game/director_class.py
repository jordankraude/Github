from card_class import Card
from validaterClass import validater
validater = validater()

class director:
    """The responsibility of the director is to direct the game of Hilo"""
    def __init__(self):
        #Initializes itself
        self.score = 300

        self.card = Card()
        self.card.card_draw()
    
    def start_game(self):
        #Creates loop for the game
        play = validater.validate_input('Would you like to play Hilo? ', "Y/N")
        if play == "Y":
            self.isplaying = True
        else:
            self.isplaying = False

        while self.isplaying:
            old_value = self.get_input()
            self.updates(old_value)
            self.outputs()

    
    def get_input(self):
        #Lets user choose if he wants to play
        if self.isplaying:
            old_value = self.card.value
        #Lets the user choose higher or lower
            print(f'\nThe value of the card is "{self.card.value}"')
            self.HorL = validater.validate_input('Higher or Lower? ', "H/L")

        #Needs to return the variable so it can become global to be inputed into the updates function
            return old_value
        
        else:
            return

    def updates(self, old_value):
        #Sets new cards value
        self.card.card_draw()
        #Stores new cards value
        new_value = self.card.value
        print(f'Next card was: "{self.card.value}"')

        #Connotation for comparing the new value with the old value
        #Updates to the scoring
        if self.HorL == "H" and new_value > old_value:
            self.score += 100
        elif self.HorL == "L" and new_value < old_value:
            self.score += 100
        elif new_value == old_value:
            self.score = self.score
        else:
            self.score -= 75
        
        #Print updated score
        print(f'Your score is: {self.score}')

    def outputs(self):
        #Input for everyone if they want to play again.
        if self.score <= 0:
            self.isplaying = False
        #Ends Program if they reach zero
            print('')
            print('You Lose... You reached 0 or lower... Better Luck Next Time!')
            play = input('Would you like to play again? [Y/N]: ').upper()
            print('')
            print('')
            self.isplaying = (play == 'Y')
            self.score = 300
            self.card.card_draw()

        else:
            play = validater.validate_input('Would you like to draw again? ', "Y/N")
            self.isplaying = (play == 'Y')
            

        pass
    
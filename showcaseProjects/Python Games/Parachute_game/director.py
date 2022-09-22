from word_class import Word
from person import Person
from parachute import Parachute
from display import Display


class Director:

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.person = Person()
        self._is_playing = True
        self._word_list = Word()
        self._word = self._word_list._getword()
        self._person = Person()
        self._display = Display()
        self._parachute = Parachute()
        self._gameover = self._parachute.parachute
        self._empty_list = Display().set_blanks(self._word)
        self.start_game()
        self._guess_list = []

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._do_outputs()
            guess = self._get_inputs()
            self._do_updates(guess)
            

    def _get_inputs(self):
        """

        Args:
            self (Director): An instance of Director.
        """
        valid = False
        while not valid:
            guess = input("Guess a letter [a-z]: ").lower()
            print('')
            if len(guess) > 1:
                valid = False
                print("Please make sure the guess is only '1' letter!")
            elif len(guess) == 0:
                valid = False
                print("Please make sure the guess is only '1' letter!")
            elif guess in self._guess_list:
                print('You have guessed this already!')
                valid = False
            else:
                return guess
       
    def _do_updates(self, guess):
        """

        Args:
            self (Director): An instance of Director.
        """
        self._guess_list.append(guess)
        if bool(self._gameover):
            pass
        else:
            self._is_playing = False

        # Replaces each spot in the word with the correct letter
        if guess in self._word:
            for i in range(len(self._word)):
                if self._word[i] == guess:
                    self._empty_list[i] = guess
        else:
            self._parachute.break_chute()

        if self._is_playing:
            failed = 0
            for char in self._word:
                if char in self._empty_list:
                    pass
                else:
                    failed += 1
            if failed == 0:
                print("Congratulations! You Won!")
                self._is_playing = False
            

    def _do_outputs(self):
        """ 

        Args:
            self (Director): An instance of Director.
        """
        print(*self._empty_list)
        for i in self._parachute.parachute:
            print(i)
        self.person.draw_person()
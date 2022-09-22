class Director:
    #Creates specified Video and Keyboard services
    def __init__(self, keyboard_service, video_service):
        self.__keyboard_service = keyboard_service
        self.__video_service = video_service

    def start_game(self):
        #start of game
        self.__video_service.open_window()
        #loop and game condition
        while self.__video_service.is_window_open():
            #This space if for things that must happen constantly during the game.
            self.inputs()
        #end of game
        self.__video_service.close_window()


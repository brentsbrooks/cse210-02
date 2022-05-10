from game.card import Card


class Director:
'''
The responsibility of a Director is to control the sequence of play.
'''


    def _init_self():
        
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        self.is_playing = True
        self.points = 0

    def start_game():
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """


        while self.is_playing:
            self.do_inputs()
            self.do_updates()
            self.do_outputs()

    def do_inputs(self):
        """
        asks the user whether the card is high or low
        """
        
        
        play_again = input("Do you want to play again? [y/n] ")
        self.is_playing = (play_again == "y")
        print('Playing....')
    
    def do_inputs(self):

        if not self.is_playing:
            return 
        
        

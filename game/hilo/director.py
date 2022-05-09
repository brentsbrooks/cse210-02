from game.card import Card


class Director:

    def _init_self():

        self.is_playing = True
        self.points = 0

    def start_game():


        while self.is_playing:
            self.do_inputs()
            self.do_updates()
            self.do_outputs()

    def do_inputs(self):
        """asks the user whether the card is high or low"""
        play_again = input("Do you want to play again? [y/n] ")
        self.is_playing = (play_again == "y")
        print('Playing....')
    
    def do_inputs(self):

        if not self.is_playing:
            return 
        
        
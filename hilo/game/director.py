from game.card import Card


class Director:

    def _init_self():

        self.is_playing = True
        self.total_score = 300

    def start_game():


        while self.is_playing:

            self.show_card()
            self.do_inputs()
            self.do_outputs()

    def show_card(self):
        card1 = self.value
        print(f"The card is : {card1}")
    
    def get_inputs(self):
        high_or_low = input("High or low? [h/l]: ")
        return high_or_low
    
    def do_outputs(self):
        if high_or_low == "h":
            card2 = self.new_value
            if card2 >= card1:
                self.points += self.total_score
                score = self.points
            else:
                self.point -= self.total_score

        elif high_or_low == "l":
            card2 = self.new_value
            if card2 <= card1:
                self.points += self.total_scores
            else:
                self.point -= self.total_score
                score = self.point
        print(f"Your score is {score}")
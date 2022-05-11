from game.card import Card


class Director:

  def __init__(self):

    self.is_playing = True
    self.total_score = 300
    self.score = 0
    self.higher_or_lower = ""

  def start_game(self):

    while self.is_playing or self.total_score > 0:

      self.show_card()
      self.get_input()

  def show_card(self):

    card1 = Card.draw_card(self)
    print(f"The card is: {card1}")

  def get_input(self):

    self.higher_or_lower = input("Do you want to go higher or lower? [h/l] ") 
    return self.higher_or_lower   

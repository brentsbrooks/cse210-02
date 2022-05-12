import random

class Card:

    def _init_self():

        self.value = 0
        self.new_value = 0
        self.points = 300


    def draw_card(self):
# Creates a instance to draw a card.
# Random.randint generates a new random value.

        self.value = random.randint(1, 13)
        self.new_value = random.random(1,13)

        if self.new_value >= self.value:
            points += 100
        else:
            points -= 75

        if self.new_value <= self.value:
            points += 100
        else:
            points -= 75

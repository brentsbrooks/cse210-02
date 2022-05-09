import random

class Card:

    def _init_self():

        self.new_card_number = 0
        self.points = 300

    def check(self):

# Loop that keeps game going as long as points are more than 0
        while points > 0:

  # Draws random card between 1 and 13
            card_number = random.randint(1, 13)
            print(f"The card is: {card_number}")

  # Asks user if they want to go higher or lower
            high_or_low = input("Higher or lower? [h/l] ")

  # if "h" is chosen
            if high_or_low == "h":
                new_card_number = random.randint(1, 13)
                print(f"Next card was: {new_card_number}")
            if new_card_number >= card_number:
                points += 100
            else:
                points -= 75
            print(f"Your score is: {points}")

  # if "l" is chosen
            if high_or_low == "l":
                new_card_number = random.randint(1, 13)
                print(f"Next card was: {new_card_number}")
            if new_card_number <= card_number:
                points += 100
            else:
                points -= 75
                print(f"Your score is: {points}")

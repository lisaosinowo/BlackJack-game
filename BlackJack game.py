# BLACKJACK GAME - CAPSTONE PROJECT

import random

def main():

    def random_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        # str_cards = [str(x) for x in cards]
        random_card = random.choice(cards)
        return random_card

    def blackjack():
        logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""

        your_cards = [] # The random cards for the user will be put in this empty list
        computer_cards = [] # The random cards for the computer will be put in this empty list

        print(logo)

        for card in range(1, 3, 1):
            your_cards.append(random_card())  # Two random numbers are added to the empty list for the user

        computer_cards.append(random_card())  # Two random numbers are added to the empty list for the computer's starting deck

        user_total = sum(your_cards)
        comp_total = sum(computer_cards)
        print(f"Your cards: {your_cards}, Current score: {user_total} ") # For visuals
        print(f"Computer's first card: {computer_cards[0]} ") # For visuals

        def comp_17():
            # while comp_total <= 17 and user_total > 17:
            #     computer_cards.append(random_card())

            while comp_total <= user_total:
                computer_cards.append(random_card())

        another_card = True
        while another_card:
            decision = input("Type 'y' to get another card, type 'n' to pass. ").lower()

            if decision == "y":
                your_cards.append(random_card()) # Everytime the user types 'y' a random card is added to the user's deck
                user_total = sum(your_cards) # This adds the cards to get a total

                print(f"Your cards: {your_cards}, Current score: {user_total} ")
                print(f"Computer's first card: {computer_cards[0]} ")
                # print(f"Computer's first card: {comp_actual_cards[0]} ")

                if user_total > 21:
                    another_card = False
                    print("You went bust! YOU LOSE!")

            elif decision == "n":
                while sum(computer_cards) < 17:
                    computer_cards.append(random_card())

                print(f"Your final hand: {your_cards}, Final score: {user_total} ")
                print(f"Computer's final hand: {computer_cards}, Final score: {sum(computer_cards)} ")

                if user_total > sum(computer_cards) and user_total <= 21:
                    print("YOU WIN!")
                elif user_total < sum(computer_cards) and sum(computer_cards) <= 21:
                    print("YOU LOSE!")
                elif user_total == sum(computer_cards) and user_total <= 21 and sum(computer_cards) <= 21:
                    print("It's a DRAW!")
                elif sum(computer_cards) > 21:
                    print("Opponent went bust! YOU WIN!")

                again = input("Do you want to play a game of BlackJack? press 'y' or 'n': ").lower()
                if again == "y":
                    blackjack()

                else:
                    print("Goodbye!")

                another_card = False

            else:
                print("Try again.")

    blackjack()

main()

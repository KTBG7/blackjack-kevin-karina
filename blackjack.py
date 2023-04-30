from dealer import Dealer
from player import Player
from deck import Deck

class Blackjack:

    def __init__(self):
       pass

    def final_cards(self, dealer:Dealer, player:Player):
        print(f'The dealers cards are {dealer.getCurrentCards()}')
        print(f'Your cards are {player.getCurrentCards()}')
        print(f'Your total is {player.get_total()} the dealers total is {dealer.get_total()}')
        print(f'The winner is {"the player!" if player.get_total() > dealer.get_total() and player.get_total() <= 21 else "the dealer!"}')
        return None

    def driver(self, dealer:Dealer, player:Player):
        self.dealer = dealer
        self.player = player
        response = input("Are you ready to play BlackJack? 'Y' for Yes or 'N' for No: ")
        if response.lower() == "n":
            print(f'Thanks for visiting!')
            return None
        if response.lower() == "y":
            while response.lower() != "n":
                self.dealer.shuffleDeck()
                self.dealer.dealCards(self.player)
                print(f"The dealers card is {self.dealer.getvisibleCard()}")
                if self.player.get_total() > 21:
                    print(f"You busted!")
                    self.final_cards(self.dealer, self.player)
                    break
                elif self.player.get_total() == 21:
                    print(f"Congrats you got BLACKJACK!")
                    self.final_cards(self.dealer, self.player)
                    break
                else:
                    response = input(f"Your cards are {self.player.getCurrentCards()}. Would you like to 'hit' for another card or 'stay'. Enter 'h' for hit or 's' to stay or 'n' to quit. ")

                while response.lower() == "h":
                    if self.player.get_total() < 21:
                        self.dealer.hit_me(self.player)
                        if self.player.get_total() < 21:
                            response = input(f"Your cards are {self.player.getCurrentCards()}. Would you like to 'hit' for another card or 'stay'. Enter 's' to stay or 'h' to hit or 'n' to quit. ")
                    else:
                        self.final_cards(self.dealer, self.player)
                        return None

                if response.lower() == "s":
                    self.final_cards(self.dealer, self.player)
                    return None   
                self.final_cards(self.dealer, self.player)




game = Blackjack()
player_1 = Player()
deck = Deck()
dealer = Dealer(deck)

game.driver(dealer, player_1)




        




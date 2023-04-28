from deck import Deck
from player import Player
import random
class Dealer:
    
    def __init__(self, deck: Deck):
        self.deck = deck
        self._currentCards = []
        self.visibleCard = []

    def shuffleDeck(self) -> None:
        for suit in self.deck.deck_of_cards:
            random.shuffle(suit['cards'])

    def setCurrentCards(self, cards: list) -> None:
        for card in cards:
            self._currentCards.append(card)
        self.visibleCard.append(self._currentCards[random.randomint(0,1)])
    
    def getCurrentCards(self) -> list:
        return self._currentCards
    
    def dealCards(self, player: Player):
        cards_dealt =0
        player_cards = []
        dealer_cards = []
        while cards_dealt <1:
            player_suit = random.randint(0,3)
            player_suit = self.deck[player_suit]
            player_card = random.randint(0,12)
            player_card = player_suit['cards'][player_card]
            player_cards.append({player_suit['suit']: player_card})
            dealer_suit = random.randint(0,3)
            dealer_suit = self.deck[dealer_suit]
            dealer_card = random.randomint(0,12)
            dealer_card = dealer_suit['cards'][dealer_card]
            dealer_cards.append({dealer_suit['suit']: dealer_card})
        player.setCurrentCards(player_cards)
        self.setCurrentCards(dealer_cards)
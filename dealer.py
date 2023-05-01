from deck import Deck
from player import Player
import random
class Dealer:
    
    def __init__(self, deck: Deck):
        self.deck = deck.deck_of_cards
        self._currentCards = []
        self.visibleCard = []

    def shuffleDeck(self) -> None:
        for suit in self.deck:
            random.shuffle(suit['cards'])
        return None 

    def get_total(self) -> int:
       count = 0
       for card in self.getCurrentCards():
            for val in card.values():
                count += val
       return count

    def setCurrentCards(self, cards: list) -> None:
        for card in cards:
            self._currentCards.append(card)
        self.visibleCard.append(self._currentCards[0])
        return None
    
    def getCurrentCards(self) -> list:
        return self._currentCards
    
    def getvisibleCard(self) -> list:
        return self.visibleCard   
    
    def dealCards(self, player: Player):
        cards_dealt =0
        player_cards = []
        dealer_cards = []
        while cards_dealt <=1:
            player_suit = random.randint(0,3)
            player_suit = self.deck[player_suit]
            player_card = random.randint(0,12)
            player_card = player_suit['cards'][player_card]
            player_cards.append({player_suit['suit']: player_card})
            dealer_suit = random.randint(0,3)
            dealer_suit = self.deck[dealer_suit]
            dealer_card = random.randint(0,12)
            dealer_card = dealer_suit['cards'][dealer_card]
            dealer_cards.append({dealer_suit['suit']: dealer_card})
            cards_dealt += 1
        player.setCurrentCards(player_cards)
        self.setCurrentCards(dealer_cards)
        return None
    
    def hit_me(self, player:Player) -> bool:
        player_cards = player.getCurrentCards()
        player_suit = random.randint(0,3)
        player_suit = self.deck[player_suit]
        player_card = random.randint(0,12)
        player_card = player_suit['cards'][player_card]
        player_cards.append({player_suit['suit']: player_card})
        player.setCurrentCards(player_cards)
        return True
     
class Player:

    def __init__(self):
        self._currentCards = []

    def setCurrentCards(self, cards: list) -> None:
        self._currentCards = []
        for card in cards:
            self._currentCards.append(card)
        return None
    
    def getCurrentCards(self) -> list:
        return self._currentCards
    
    def get_total(self) -> int:
       count = 0
       for card in self.getCurrentCards():
            for val in card.values():
                count += val
       return count
    
    def can_hit(self) -> bool:
        return True if self.get_total() < 21 else False

    

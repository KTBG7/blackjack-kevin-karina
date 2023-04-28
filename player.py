class Player:

    def __init__(self):
        self._currentCards = []

    def setCurrentCards(self, cards: list) -> None:
        for card in cards:
            self._currentCards.append(card)
    
    def getCurrentCards(self) -> list:
        return self._currentCards
    

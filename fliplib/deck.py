from .scryfall import getApi
from .printer import printMessage

class Deck:
    def __init__(self):
        self.mainboard = []
        self.sideboard = []
        self.extra = []
        self.api = getApi()
    
    def addCardToMainboard(self, amount, cardname):
        card = self.api.findCard(cardname)
        self.mainboard.append((amount, card))

    def printDecklist(self):
        for cardEntry in self.mainboard:
            amount = cardEntry[0]
            card = cardEntry[1]
            printMessage(str(amount) + ' ' + card.name())

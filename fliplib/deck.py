from .scryfall import getApi
from .printer import printMessage

class Deck:
    def __init__(self, name):
        self.mainboard = []
        self.sideboard = []
        self.extra = []
        self.api = getApi()
        self.name = name
    
    def addCardToMainboard(self, amount, cardname):
        card = self.api.findCard(cardname)
        self.mainboard.append((amount, card))

    def printDecklist(self):
        """
        Spits the out the decklist information for debugging
        """
        for cardEntry in self.mainboard:
            amount = cardEntry[0]
            card = cardEntry[1]
            printMessage(str(amount) + ' ' + card.name())

    def generateTTSDeckObject(self):
        """
        Generates the JSON deck object that TTS uses.
        """
        ttsDeckObject = {'Transform': {'posX':1.0,'posY':1.0,'posZ':-0.0,'rotX':0,'rotY':180,'rotZ':180,'scaleX':1,'scaleY':1,'scaleZ':1}}
        ttsDeckObject['Name'] = 'DeckCustom'
        ttsDeckObject['Nickname'] = self.name

        containedObjects = []
        deckIds = []
        cardId = 100

        for cardTuple in self.mainboard:
            amount = cardTuple[0]
            card = cardTuple[1]
            cardObject = card.getTTSCardObject(cardId)

            # TODO Figure out how to put several copies of similar card into the deck, maybe this is wrong?
            containedObjects.append(cardObject)
            for _ in range(amount):
                deckIds.append(cardId)
            cardId += 1

            # This was to shuffle things around with the images? Skips from 169 to 200 and so on.
            if int(str(cardId)[1:]) == 69:
                cardId += 31

        ttsDeckObject['ContainedObjects'] = containedObjects
        ttsDeckObject['DeckIds'] = deckIds

        customDeck = {}
        for deckImage in getDeckImages():
            customDeck[deckImage.index] = deckImage.getCustomDeckObject()
        ttsDeckObject['CustomDeck'] = customDeck

        return ttsDeckObject
    
    def getDeckImages(self):
        return []

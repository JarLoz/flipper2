from .scryfall import getApi
from .printer import printMessage

class Deck:
    def __init__(self, name):
        self.mainboard = []
        self.sideboard = []
        self.extra = []
        self.api = getApi()
        self.name = name
        self.nextCardId = 100
    
    def addCardToMainboard(self, amount, cardname):
        card = self.api.findCard(cardname)
        card.cardId = self.nextCardId
        self.mainboard.append((amount, card))

        self.nextCardId += 1
        # This was to shuffle things around with the images? Skips from 169 to 200 and so on.
        if int(str(self.nextCardId)[1:]) == 69:
            self.nextCardId += 31

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

        for cardTuple in self.mainboard:
            amount = cardTuple[0]
            card = cardTuple[1]
            cardObject = card.getTTSCardObject()
            # TODO Figure out how to put several copies of similar card into the deck, maybe this is wrong?
            containedObjects.append(cardObject)
            for _ in range(amount):
                deckIds.append(cardObject.cardId)

        ttsDeckObject['ContainedObjects'] = containedObjects
        ttsDeckObject['DeckIds'] = deckIds

        customDeck = {}
        for deckImage in getDeckImages():
            customDeck[deckImage.index] = deckImage.getCustomDeckObject()
        ttsDeckObject['CustomDeck'] = customDeck

        return ttsDeckObject
    
    def getDeckImages(self):
        imageIndex = 0
        deckImageNames = []
        for i in range(0,len(self.mainboard),69) :
            chunk = self.mainboard[i:i+69]
            imageNames = list(map(lambda cardTuple: cardTuple[1].imageName(), chunk))
            # TODO Create DeckImages here.
            deckImageName = deckName+'_image_'+str(imageIndex)+".jpg"
            deckImageNames.append([deckImageName])
            callMontage(imageNames, deckImageName, hires, output)
            imageIndex += 1
        return deckImageNames

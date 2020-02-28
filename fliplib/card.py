import os
from .scryfall import getApi

class Card:

    def __init__(self, cardname):
        self.name = cardname
        self.selectedPrinting = None
        self.printings = None

    def imageName(self, scryId = None):
        if (scryId == None):
            scryId = self.selectedPrinting
        imageName = 'imageCache/front_' + scryId + '.jpg'
        if (not os.path.isfile(imageName)):
            # Image not downloaded.
            api = getApi()
            url = self.printings[scryId]['image_uris']['normal']
            api.downloadImage(url, imageName)
        return imageName

    def getTTSCardObject(self):
        return {
            'Name':'Card',
            'Nickname':self.name(),
            'CardID':self.cardId,
            'Transform':{
                'posX':2.5,
                'posY':2.5,
                'posZ':3.5,
                'rotX':0,
                'rotY':180,
                'rotZ':180,
                'scaleX':1,
                'scaleY':1,
                'scaleZ':1
                }
            }

def createCard(cardname):
    api = getApi()
    scryfallData = api.findCard(cardname)
    card = Card(cardname)
    card.selectedPrinting = scryfallData['id']
    if ('prints_search_uri' in scryfallData.keys()):
        printings = api.findPrintings(scryfallData['oracle_id'])
    else:
        printings = {scryfallData['id'] : scryfallData}
    card.printings = printings

    return card

import requests
from .card import Card
from time import sleep

_api = None

class Scryfall:
    def __init__(self):
        self.apiUrl = "https://api.scryfall.com"
        self.namedEndpoint = self.apiUrl + '/cards/named'
        self.cache = {}

    def findCard(self, cardname):
        if (not cardname in self.cache.keys()):
            response = requests.get(self.namedEndpoint,{'exact':cardname})
            sleep(0.1) # Let's be nice with scryfall's API.

            if (response.status_code == 200):
                self.cache[cardname] = response.json()
            else:
                raise ApiError("Card not found!")

        card = Card(cardname)
        card.scryfallData = self.cache[cardname]

    def downloadImage(self, url, outfile):
        response = requests.get(url, stream=True)
        with open(self._imageName, "wb") as outfile:
            shutil.copyfileobj(response.raw, outfile)
        del response
        sleep(0.1) # Still being very nice with scryfall.
        return True

class ApiError(Exception):
    def __init__(self, message):
        self.message = message


def getApi():
    global _api
    if (_api == None):
        _api = Scryfall()
    return _api

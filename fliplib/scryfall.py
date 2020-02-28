import requests
import shutil
from time import sleep

_api = None

class Scryfall:
    def __init__(self):
        self.nameCache = {}
        self.printCache = {}
        self.apiUrl = "https://api.scryfall.com"
        self.namedEndpoint = self.apiUrl + '/cards/named'
        self.searchEndpoint = self.apiUrl + '/cards/search'

    def findCard(self, cardname):
        if (not cardname in self.nameCache.keys()):
            response = requests.get(self.namedEndpoint,{'exact':cardname})
            sleep(0.1) # Let's be nice with scryfall's API.

            if (response.status_code == 200):
                self.nameCache[cardname] = response.json()
            else:
                raise ApiError("Card not found!")

        return self.nameCache[cardname]

    def findPrintings(self, oracleId):
        response = requests.get(self.searchEndpoint,{'order':'released','q':'oracleid:'+oracleId,'unique':'prints'})
        sleep(0.1)
        if (response.status_code == 200):
            printingsResponse = response.json()
            printings = {}
            for printing in printingsResponse['data']:
                printings[printing['id']] = printing
            return printings
        else:
            return None

    def downloadImage(self, url, imageName):
        response = requests.get(url, stream=True)
        with open(imageName, "wb") as outfile:
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

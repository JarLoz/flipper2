import requests
from .card import Card
from time import sleep

class Scryfall:
    def __init__(self):
        self.apiUrl = "https://api.scryfall.com"
        self.namedEndpoint = self.apiUrl + '/cards/named'

    def findCard(self, cardname):
        response = requests.get(self.namedEndpoint,{'exact':cardname})
        sleep(0.1) # Let's be nice with scryfall's API.

        if (response.status_code == 200):
            return Card(response.json())
        else:
            raise ApiError("Card not found!")


class ApiError(Exception):
    def __init__(self, message):
        self.message = message

_api = Scryfall()

def getApi():
    return _api

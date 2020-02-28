class Card:
    scryfallData = None

    def __init__(self, scryfallData):
        self.scryfallData = scryfallData

    def name(self):
        return self._getScryfallData('name')

    def _getScryfallData(self, key):
        if (self.scryfallData == None):
            return None
        else:
            return self.scryfallData[key]

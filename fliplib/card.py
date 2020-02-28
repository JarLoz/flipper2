import os
import requests
import shutil

class Card:
    scryfallData = None
    _imageName = None

    def __init__(self, scryfallData):
        self.scryfallData = scryfallData

    def name(self):
        return self.scryfallData['name']

    def imageName(self):
        if (self._imageName == None):
            self._imageName = 'imageCache/front_' + self.scryfallData['id'] + '.jpg'
        if (not os.path.isfile(self._imageName)):
            # Image not downloaded.
            url = self.scryfallData['image_uris']['normal']
            response = requests.get(url, stream=True)
            with open(self._imageName, "wb") as outfile:
                shutil.copyfileobj(response.raw, outfile)
            del response
        return self._imageName

    def getTTSCardObject(self, cardId):
        return {
            'Name':'Card',
            'Nickname':self.name(),
            'CardID':cardId,
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

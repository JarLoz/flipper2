class DeckImage:
    def __init__(self, index, url):
        self.index = index
        self.faceUrl = url
        self.backUrl = 'https://i.imgur.com/P7qYTcI.png'
        self.uniqueBack = False

    def getCustomDeckObject(self):
        return {'NumWidth':10,'NumHeight':7,'FaceUrl':self.faceUrl,'BackUrl':self.backUrl,'UniqueBack':self.uniqueBack}

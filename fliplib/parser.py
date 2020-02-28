import re
from .deck import Deck
from .scryfall import ApiError
from .printer import printMessage

def readDecklist(filename):
    """
    Reads a decklist from a file
    """
    try:
        with open(filename,encoding="utf8") as decklistfile:
            decklist = decklistfile.readlines()
        return parseDecklist(decklist)
    except FileNotFoundError:
        printMessage("File not found!")
        return None

def parseDecklist(decklist):
    """
    Parses a given decklist (list of lines) into a Deck object containing Card objects.
    """
    newDeck = Deck()
    for line in decklist:
        amount, cardname = parseDecklistLine(line)
        if (cardname):
            try:
                newDeck.addCardToMainboard(amount, cardname)
            except ApiError as exception:
                printMessage(exception.message)
    return newDeck


def parseDecklistLine(line):
    """
    Parses the relevant information from a decklist line.
    """
    splitLine = line.split()
    if (len(splitLine) < 1):
        return (None, None)
    if (re.match('\d+$',splitLine[0])):
        # A digit means a count. I hope.
        amount = int(splitLine[0])
        cardname = ' '.join(splitLine[1:])
    else:
        # No digit, assuming count of one.
        amount = 1
        cardname = line
    return (amount, cardname)

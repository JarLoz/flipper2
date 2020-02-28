from fliplib.parser import readDecklist
import os

def initializeCaches():
    os.makedirs('imageCache', exist_ok=True)
    os.makedirs('apiCache', exist_ok=True)


initializeCaches()
deck = readDecklist("decklist.txt")
deck.printDecklist()


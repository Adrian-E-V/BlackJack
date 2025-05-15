import bj_util
import random

deck = []
numDecks = 1

def startGame():
    global numDecks
    global deck
    numDecks = int(input("How many decks would you like to play with? "))
    deck = bj_util.multipleDecks(numDecks)
    # print("deck has been created")

def dealCard():
    global deck
    # print("accessed the dealCard function")
    if not deck: #checks if the deck has run out of cards. If so, reshuffles
        reshuffle()
    index = random.randrange(len(deck))
    return deck.pop(index)

    
def reshuffle():
    global deck
    # print("Accessed reshuffle function")
    deck = bj_util.multipleDecks(numDecks)
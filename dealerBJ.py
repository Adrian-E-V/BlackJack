import bj_util
import random

deck = []
numDecks = 1

def startGame():
    global numDecks
    global deck
    numDecks = int(input("How many decks would you like to play with? "))
    deck = bj_util.multipleDecks(numDecks)
    if (numDecks == 1):
        print("We will be playing with 1 deck.")
    else:
        print("We will be playing with " + str(numDecks) + " decks.")
    print("You will be starting with $1000. Your goal is to have $2500.")
    print("Let's begin. \n")

def dealCard():
    global deck
    # print("accessed the dealCard function")
    if not deck: #checks if the deck has run out of cards. If so, reshuffles
        reshuffle()
    index = random.randrange(len(deck))
    # for card in deck:
    #     print(card)
    return deck.pop(index)

    
def reshuffle():
    global deck
    # print("Reshuffling...")
    deck = []
    deck = bj_util.multipleDecks(numDecks)
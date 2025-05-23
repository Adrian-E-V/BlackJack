#This file allows for the creation of cards, decks, and multiple decks. These are used by the dealer and player files to play blackjack

class Card:
    #This is my constructor. Each card must have a rank and a suit.
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    #Accessor methods:
    def getRank(self):
        return self.rank
    def getSuit(self):
        return self.suit
    
    #Python has a toString() just like Java!
    def __str__(self):
        return "This is a " + str(self.rank) + " of " + self.suit + "\n" 

#Creates a deck w/ all 52 cards, 13 of each suit
def createDeck():
    deck = []
    suits = {"Hearts", "Spades", "Diamonds", "Clubs"}
    for suit in suits:
        for i in range(2, 15):
            if (i > 10):
                if (i == 11):
                    card = Card("Jack", suit)
                if (i == 12):
                    card = Card("Queen", suit)
                if (i == 13):
                    card = Card("King", suit)
                if (i == 14):
                    card = Card("Ace", suit)
            else:
                card = Card(i, suit)
            deck.append(card)
    return deck

#Blackjack decks have multiple decks shuffled together
def multipleDecks(num: int):
    megaDeck = []
    for i in range(0, num):
        megaDeck.extend(createDeck())
    return megaDeck


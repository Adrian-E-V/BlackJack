import dealerBJ as dealer
import bj_util

#this is a simple version of PlayerBJ.py that the bot will be able to interact with
dlrHand = []
plrHand = []

def countTotal(hand):
    total = 0
    aces = False
    count = 0
    for card in hand:
        if (card.getRank() == "Ace"):
            aces = True
            count += 1
        else:
            try:
                total += card.getRank()
            except TypeError:
                total += 10
    if aces:
        i = 0
        while i < count:
            total += 1
            if ((total + 10) <= 21):
                total += 10
            i += 1
    return total

def getState():
    #a tuple with plrTotal, dealerCard, and AcesPresent
    global plrHand
    global dlrHand
    plrTotal = countTotal(plrHand)

    #tracks if aces are present
    aces = False
    for card in plrHand:
        if card.getRank() == "Ace":
            aces = True

    tupState = (plrTotal, dlrHand[0].getValue(), aces)
    return tupState


def round():
    #sets up the game
    global dlrHand
    global plrHand
    dealer.reshuffle()
    dlrHand = []
    plrHand = []
    dlrHand.append(dealer.dealCard())
    plrHand.append(dealer.dealCard())
    dlrHand.append(dealer.dealCard())
    plrHand.append(dealer.dealCard())
    #somewhere else we'll check whether they got a blackjack
    
    return getState()

def action(act):
    global dlrHand
    global plrHand
    if (act == 1):
        plrHand.append(dealer.dealCard())
        if (countTotal(plrHand) > 21):
            return (getState(), -1, True)
        else:
            return (getState(), 0, False)
    
    #Dealer deals itself if necessary
    dlrTotal = countTotal(dlrHand)
    while (dlrTotal<17):
        dlrHand.append(dealer.dealCard())
        dlrTotal = countTotal(dlrHand)
    plrTotal = countTotal(plrHand)
    
    if (dlrTotal <= 21):
        if (plrTotal > dlrTotal):
            return (getState(), 1, True)
        
        if (dlrTotal > plrTotal):
            return (getState(), -1, True)
        
        if (plrTotal == dlrTotal):
            return (getState(), 0, True)
    else:
        return (getState(), 1, True)
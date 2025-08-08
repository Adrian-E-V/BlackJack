import dealerBJ as dealer
import bj_util
import math
import time

#Ideas for additional improvement:
# - Double and Split functionality
# - Insurance when dealer is showing an Ace

#Run the game from this file
dealer.startGame()
cash = 1000

def placeBets():
    global cash
    bet = input("Place your bets (enter number or 'ALL IN'): ")
    if (bet == "QUIT"):
        quit()
    if (bet == "ALL IN"):
        return cash  
    else:
        #The following checks if user input is an int
        skip = False
        try:
            num = int(bet)
        except ValueError:
            print("Not a valid bet.")
            skip = True

        #If it is a valid bet value, then...
        if (not skip):
            bet = int(bet)
            #More valid bet checks:
            if (bet <= 0):
                print("Cannot make bets of zero or lower. Try again.")
                bet = -1
            elif (bet > cash):
                print("This is more than you have! Try again.")
                bet = -1
            #officially a valid bet
            else:
                return bet
        return placeBets()

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
        #for EACH Ace in the player's hand, we must add 1
        #In addition, if adding 10 more (total of 11) doesn't put the player over 21, then add 10.
        #Do these for each ace in the player's hand (the count)
        i = 0
        while i < count:
            total += 1
            if ((total + 10) <= 21):
                total += 10
            i += 1
    return total

def win(bet: int, blackJack=False):#call this when the player wins
    global cash
    if (blackJack):
        cash += math.ceil(bet/2)
        print(f"Blackjack! You now have ${cash} \n")
    else:
        cash += bet
        print(f"You win! You now have ${cash} \n")

def lose(bet: int):#call when player loses
    global cash
    cash -= bet
    if (cash <= 0):
        return
    else:
        print(f"You lose! You now have ${cash} \n")
    
def round():
    global cash
    bet = placeBets()
    print()

    #Set up for player and dealer hands
    #Will deal first to the dealer, then the player, and back and forth, like in actual blackjack.
    dlrHand = []
    plrHand = []
    dlrHand.append(dealer.dealCard())
    plrHand.append(dealer.dealCard())
    dlrHand.append(dealer.dealCard())
    plrHand.append(dealer.dealCard())

    print(f"Dealer is showing a {dlrHand[0]}")
    print(f"You have: {plrHand[0]}, {plrHand[1]}")
    plrTotal = countTotal(plrHand)
    print(f"Your total: {plrTotal}")
    if (plrTotal == 21):
        win(bet, True)
        return
    print()
    

    
    #figure out how to do aces
    #Include player total (if ace do hard / soft)
    action = ""
    while(action != "STAND"):
        action = input("Do you HIT or STAND? ")
        if (action == "HIT"):
            plrHand.append(dealer.dealCard())
            plrTotal = countTotal(plrHand)
            print("You have:", end=" ")
            i = 0
            while (i < len(plrHand)):
                if (i == (len(plrHand) - 1)):
                    print(plrHand[i])
                else:
                    print(plrHand[i], end=", ")
                i += 1
            print(f"Your total: {plrTotal}")
            if (plrTotal > 21):
                lose(bet)
                return
            print()

        elif (action == "STAND"):
            print()
        else:
            action = ""
            print("Invalid action, try again.")
     
    #After the part where the player gambles, this is where we calculate whether they have won or lost
    dlrTotal = countTotal(dlrHand)
    print(f"Dealer has: {dlrHand[0]}, {dlrHand[1]}")
    time.sleep(0.5)
    while (dlrTotal<17):
        time.sleep(1.5)
        print("Dealer draws...")
        dlrHand.append(dealer.dealCard())
        dlrTotal = countTotal(dlrHand)
        time.sleep(1.5)
        print(dlrHand[-1])
        time.sleep(0.5)
    print(f"Dealer's total: {dlrTotal}")
    time.sleep(0.5)
    
    if (dlrTotal <= 21):
        if (plrTotal > dlrTotal):
            #player wins!
            win(bet)
            return
        if (dlrTotal > plrTotal):
            #player loses
            lose(bet)
            return
        if (plrTotal == dlrTotal):
            print(f"Push! You keep your money. You have ${cash}\n")
            return
    else:
        win(bet)
        return
    

while (cash>0 and cash<2500):
    round()
    time.sleep(1.5)
if (cash <= 0):
    print("You lose! You have lost all your cash.")
else:
    print("You've beaten BlackJack!")
import dealerBJ as dealer
import bj_util

#Ideas for additional improvement:
# - Double and Split functionality
# - Insurance when dealer is showing an Ace

#Run the game from this file
dealer.startGame()
cash = 1000

def placeBets():
    global cash
    bet = input("Place your bets (enter number or 'ALL IN'): ")
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
    action = ""
    print()
    #figure out how to do aces
    #Include player total (if ace do hard / soft)
    
    while(action != "STAND"):
        action = input("Do you HIT or STAND? ")
        if (action == "HIT"):
            plrHand.append(dealer.dealCard())
            print("You have:", end=" ")
            i = 0
            while (i < len(plrHand)):
                if (i == (len(plrHand) - 1)):
                    print(plrHand[i])
                else:
                    print(plrHand[i], end=", ")
                i += 1
            print()
        elif (action == "STAND"):
            print()
        else:
            action = ""
            print("Invalid action, try again.")
     
    #After the part where the player gambles, this is where we calculate whether they have won or lost
    #I need to see if they lose from hitting. This is a check that needs to be performed earlier, probably when a player HITs
    


round()
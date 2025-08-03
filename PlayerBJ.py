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
    # print(type(bet))
    # print("bet is " + str(bet))
    
    


round()
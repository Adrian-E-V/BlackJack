import simpleBJ
import random
import pandas as pd

#this will be the code for our bot's learning
#We'll be using reinforcement learning with Q-learning
#The many comments are moreso notes for myself, to make sure I understand what is going on

Q = {}
#This dictionary will be where we keep track of the situtation (state -> key) and
# the possible rewards from each action (value)

def getQ(state):
    #helper function that checks if we have already come across this state before
    if (state not in Q):
        Q[state] = [0.0, 0.0]
    return Q[state]
    
def getAction(state, epsilon=0.1):
    #this is the bot's choice of which action to take in a certain scenario
    q0, q1 = getQ(state) #at the top to make sure a state always has at least a Q of 0.0, 0.0

    #pick a number at random, if it's less than epsilon, make a random decision, otherwise go based on Q-table values
    num = random.random()
    if (num < epsilon):
        return random.randint(0, 1)
    
    #going based on Q-values
    if (q0 > q1):
        return 0
    elif (q0 < q1):
        return 1
    else:
        return random.randint(0, 1) #settles ties randomly
    
def learning(state, action, reward, newState, done, alpha = 0.2, gamma = 0.9):
    #There's a lot here that I'm still wrapping my head around, but this is essentially how our bot learns
    #constants like alpha and gamma control how much our bot cares about past info and how much it cares about the future, respectively
    #new_state is actually our present state. 'state' is where we were before the bot took its action. We go back and update state, as if saying
    #"Was the decision we made really worth it, or, would the other route have been better?"
    #This is why the rewards matter so much! They assign points to whether the bot's decision was worth while. The bot learns by trial and error

    #state -> where we WERE at
    #action -> the action we took at that point
    #reward -> the reward we got for that action
    #newState -> the state we're at after our action
    #done -> if we are done, we don't need to consider the future possible rewards (thus, ignore gamma*max)
    #alpha -> how much we want the bot to consider this new outcome; "step size of learning"
    #gamma -> how much the bot values future rewards (hence why this is multiplied by the best possible reward in our state)
    
    if done:
        Q[state][action] = Q[state][action] + alpha*(reward - Q[state][action])
        return
    
    maxNum = max(getQ(newState))
    Q[state][action] = Q[state][action] + alpha*(reward + (gamma*maxNum) - Q[state][action])

def playRounds(rounds, epsilon=0.1, alpha=0.2, gamma=0.9, debug=False, text=False):
    wins = 0
    losses = 0
    for _ in range(rounds):
        state = simpleBJ.round()
        done = False

        if text:
            print(f"Dealer: {state[1]}")
            print(f"Player: {state[0]}")

        if debug:
            print(state)

        while not done:
            act = getAction(state, epsilon)
            if text:
                if (act == 0):
                    print("Stand!")
                else:
                    print("Hit!")

            if debug:
                print(act)

            newState, reward, done = simpleBJ.action(act)
            if debug:
                print(newState, reward, done)
            
            if text:
                print(f"Player: {newState[0]}")

            learning(state, act, reward, newState, done, alpha, gamma)

            if (reward==1):
                wins += 1
                if text:
                    print("Win! \n")
            elif (reward<0):
                losses += 1
                if text:
                    print("Lose! \n")
            elif done and text:
                print("Tie! \n")

            state = newState
    print(f"The bot had {wins} wins and {losses} losses!")



# This is the code for the tables that show up at the end of the agent's rounds


def makeTables(ace):
    # making a subset of Q:
    # dictStats = {k: v for k, v in Q.items() if (k[2] == ace)}
    # print(list(dictStats.items()))

    dealerRange = range(2, 12)
    playerRange = range(2, 22)
    bjStats = pd.DataFrame(columns=dealerRange, index=playerRange)
    bjStats.columns.name = "Dealer Up Card"
    bjStats.index.name = "Player Total"

    for dlr in dealerRange:
        for plr in playerRange:
            action = getAction((plr, dlr, ace), 0)
            #calling this function does exactly what we want here. We need the preferred action at a specific state
            #we pass 0 for epsilon so there is no randomness in the result, purely what the agents it should do in that state
            if (action == 1):
                bjStats.at[plr, dlr] = "H"
            elif (action == 0):
                bjStats.at[plr, dlr] = "S"

    

    print(bjStats)
    

playRounds(1000000, debug=False, text=False)
print("\nHere are tables showing the agent's preferred action in different states.")
print("Hard Hands - the agent does not have an ace")
makeTables(False)
print("\nSoft Hands - the agent has an ace")
makeTables(True)


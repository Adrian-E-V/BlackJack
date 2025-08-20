import simpleBJ
import random

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

def playRounds(rounds, epsilon=0.1, alpha=0.2, gamma=0.9, debug=False):
    wins = 0
    losses = 0
    for _ in range(rounds):
        state = simpleBJ.round()
        done = False

        if debug:
            print(state)

        while not done:
            act = getAction(state, epsilon)
            if debug:
                print(act)

            newState, reward, done = simpleBJ.action(act)
            if debug:
                print(newState, reward, done)
            
            learning(state, act, reward, newState, done, alpha, gamma)

            if (reward==1):
                wins += 1
            elif (reward<0):
                losses += 1

            state = newState
    print(f"The bot had {wins} wins and {losses} losses!")

playRounds(1000000, debug=False)

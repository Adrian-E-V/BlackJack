# Blackjack Reinforcement Learning Agent

This project implements a reinforcement learning agent that learns to play Blackjack through trial and error. It uses a simplified Blackjack environment for agent interaction and a Q-learning loop to train a policy over many simulated rounds.

## Description
- [`bj_util.py`](./bj_util.py) defines the core card and deck mechanics used by the environment, including single and multi-deck creation.
- [`dealerBJ.py`](./dealerBJ.py) stores functions that manipulate the deck in play by dealing cards and reshuffling.
- [`PlayerBJ.py`](./PlayerBJ.py) allows the user to play Blackjack for themself in the terminal.
- [`simpleBJ.py`](./simpleBJ.py) provides a lightweight Blackjack environment designed for programmatic interaction rather than human play. It manages player and dealer hands, state representation, and game resolution.  
- [`qbot.py`](./qbot.py) contains the Q-learning agent, training loop, and reporting functions. The agent learns optimal actions (hit or stand) using an ε-greedy policy and displays strategy tables after training.

## Techniques of Interest
- **Custom classes and object modeling**: `Card` encapsulates card state and behavior, including a [`__str__`](https://docs.python.org/3/reference/datamodel.html#object.__str__) method for human-readable output.  
- **Deck generation**: [`createDeck`](./bj_util.py) and [`multipleDecks`](./bj_util.py) generate standard and multi-deck Blackjack setups, using Python iteration and list extension.  
- **State representation**: The Blackjack state is reduced to a tuple `(player total, dealer up-card, usable ace)` for compact reinforcement learning input.  
- **Q-learning update rule**: Implements the [temporal difference update](https://en.wikipedia.org/wiki/Q-learning), balancing immediate reward with estimated future value.  
- **ε-greedy exploration**: Chooses random actions with probability ε to avoid local optima ([`random.random()`](https://docs.python.org/3/library/random.html#random.random)).  
- **Tabular visualization**: Uses [pandas `DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) to generate strategy tables, showing the agent’s preferred action across player totals and dealer up-cards.

## Technologies and Libraries
- **Python Standard Library**  
  - [`random`](https://docs.python.org/3/library/random.html) for arbitrary action selection.  
- **[pandas](https://pandas.pydata.org/)** for tabular output of learned policies.
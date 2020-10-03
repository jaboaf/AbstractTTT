# Welcome to my most beloved project!

### The 1 liner:
#### An Algorithm that plays NxN Tic-Tac-Toe perfectly without searching the game tree- a new development in positional games.

## Partitioning This Page
### * Intro
### * Methods
### * Results
### * Discussion

Why are we interested in how to optimally play tic-tac-toe?

"It's so easy- you just don't lose" is what most people say. But nonetheless people will go a couple rounds of tic-tac-toe and some one will in fact lose. And as easy as it is to come up with "good moves" or identify "bad moves", but stitching together heuristics that are optimal a high proportion of time is unsatisfying. We still somehow don't know a rule/process/function/algorithm that can be presented any board state and return an optimal move without searching the game tree.

Precisely, we make the following distinction
A game is a pair, (G, F) 

This is the distinction between ∃ f:{0, 1, 2}³ˣ³ → (x₁, x₂) s.t. ∀ (G, F)

, when applied to a board state, will

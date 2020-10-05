# Welcome to my most beloved project!

### The 1 liner:
#### An Algorithm that plays NxN Tic-Tac-Toe perfectly without searching the game tree- a new development in positional games.

## Partitioning This Page
* ### Intro
* ### Methods
* ### Results
* ### Discussion


## Intro!
Why are we interested in how to optimally play tic-tac-toe?

"It's so easy- you just don't lose" is what most people say. But nonetheless people will go a couple rounds of tic-tac-toe and some one will in fact lose. And as easy as it is to come up with "good moves" or identify "bad moves", but stitching together heuristics that are optimal a high proportion of time is unsatisfying. We still somehow don't know a rule/process/function/algorithm that can be presented any board state and return an optimal move without searching the game tree.

A game is (𝑋,𝐹), where 𝑋 is the board and 𝐹 ⊆ 𝒫(𝑋) where 𝒫(A) denotes the powerset of A.

𝕊
A game state is a function, 𝑆: 𝑋 → {0,1,2}, that assigns a value to each point on the board, ie.
* if x ∈ 𝑋 and G(x) = 0, then x is unoccupied
* if x ∈ 𝑋 and G(x) = 1, then x is occupied by player 1
* if x ∈ 𝑋 and G(x) = 2, then x is occupied by player 2

𝕊 ≔ { 𝑆 s.t. |𝑆⁻¹(1)| ≤ |𝑆⁻¹(2)| ≤ |𝑆⁻¹(1)| + 1 }

Precisely, this is the distinction between

        ∃ f: 𝕊 → 𝑋 s.t. ∀ 𝑆 ∈ 𝕊 f(𝑆) is optimal

and

        ∀ 𝑆 ∈ 𝕊  ∃ f: 𝕊 → 𝑋 s.t. f(𝑆) is optimal

, when applied to a board state, will


Precisely, we make the following distinction
A positional game is a 4-tuple, (𝑋, 𝐹, a, b), where:
* 𝑋 is the board
* 𝐹 is a set of winning lines
* a is the number of moves the first player can make in one turn
* b is the number of moves the second player can make in one turn

https://people.inf.ethz.ch/smilos/mSt-thesis.pdf

For our purposes, we will set a = b = 1 and denote a game with the 2-tuple (𝑋, 𝐹).
Can we describe 𝑋 as something more specific than "the board"? Not really. Perhaps one could say that it is a set of the spots on the board, but surely we could construct an equivalent board using a vector x ∈ ℝⁿ.
For the 3x3 tic-tac-toe (TTT) game we all know, we have a couple options for 𝑋:

        𝑋 ≔ {  1, 2, 3,
                4, 5, 6,
                7, 8, 9 }

or

        𝑋 ≔ {  (1,1), (1,2), (1,3),
                (2,1), (2,2), (2,3),
                (3,1), (3,2), (3,3)     }

or the 0-based indexing version of either of these, among many other options.

We will use the the 2nd option. There are many reasons for this, and all of them will hopefully become clear as we abstract from the 3x3 TTT game. In essence your choice is simply a way to index our board. And while our 3x3 board or even a 3x3x3 board may be easy to visualize and understand, this is not nessisarilty as we get more abstract and discuss boards such as, NxN = N² or NxNxN = N³ or NxNxNx...xN = Nᵏ.

Generally, we will construct the TTT board as a k-dimensional lattice N₁ x N₂ x … x N\_k where nᵢ denotes the size of the iᵗʰ dimension and range of values,  {1, … , nᵢ}, that a coordinate can take in  the iᵗʰ dimension. So, boards will be denoted by a k-tuple, (N₁, N₂, … , N\_k). Though it is not possible to distinguish the board, 𝑋 ≔ (N₁, N₂, … , N\_k), from the point, (n₁, n₂, … , n\_k) ∈ 𝑋, the meaning should be clear from the context. To resolve is ambiguity we will use "𝑋 ≔" in front of a k-tuple to denote a board.

Now that that's out of the way,


"spots" is a vague,

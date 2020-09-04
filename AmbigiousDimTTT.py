from __future__ import division
'''
A board is structured as follows:

[	[ii, ij, ik],
	[ji, jj, jk],
	[ki, kj, kk]	]
where ab = {'X' if player X played in row a col b, 'O' if player O played row a col b, 0 otheriwse}
for a,b in {i,j,k}

A good question is: Are there better data srtcutures for this?
	A very simple change of lists to tuples leaves us with:
		(	( [ii] , [ij] , [ik] ),
			( [ji] , [jj] , [jk] ),
			( [ki] , [kj] , [kk] )	)

	Or we could use a dict with :
		{ 	(i,i): f(i,i), (i,j): f(i,j), (i,k): f(i,k),
			(j,i): f(j,i), (j,j): f(j,j), (j,k): f(i,k),
			(k,i): f(i,i), (k,j): f(k,j), (k,k): f(k,k) 	}

		where f(a,b) = {'X' if player X played in row a col b, 'O' if player O played row a col b, 0 otheriwse}
		for a,b in {i,j,k}

The list construction seem best because we are managing half as much information as the dict construction.
We also don't have to negotiate with immutability of elements in tuples.
And when looking at rows, we can take advantage of list:
 	checking membership (elem in array), counting the number of memebers ( array.count(elem) )

The tuple construction seems like a less fun version of the list construction.

The dict construction, however, is compelling when we encounter higher dimensional boards.
	for example, for a 3x3x3 board our list construction of a board will look like:
		[	[ [iii,	iij, iik] , [iji, ijj, ijk] , [iki, ikj, ikk] ],
			[ [jii,	jij, jik] , [jji, jjj, jjk] , [jki, jkj, jkk] ],
			[ [kii,	kij, kik] , [kji, kjj, kjk] , [kki, kkj, kkk] ]	]
		where abc = {'X' if player X played in row a col b height c, 'O' if player O played row a col b height c, 0 otheriwse}
		for a,b,c in {i,j,k}

	when we move from 2 dimensions to 3 dimensions, iterating through any "line" in the cube gets increasingly difficult.
	Even iterating through our board to get the diagnols on the bottom level isn't super smooth.
		Board[i][i][i], Board[j][j][i] , Board[k][k][i]
		Board[i][k][i], Board[j][j][i] , Board[k][i][i]
	Why? Because we have to go as deep into our data structure as it exists:
	So even if we want a diagnol that lives in 2 dimensions, from a 4 dimensional board we must use Board[][][][]

	The bottom line is that if we can figure out how to generate the coordinates, we don't want to do more work to implememt that.
	In the list construction we have to do that, but if we have a dictionary:
		Board[coord] for coord in [ (x,  x  ,i) for x in [i,j,k] ]
		Board[coord] for coord in [ (x,k-x+i,i) for x in [i,j,k] ]

	understandably this may seem more complex but lets go to 6D
	Our List construction gets... complicated
		Board[i][i][i][i][i][i], Board[j][j][i][i][i][i] , Board[k][k][i][i][i][i]
		Board[i][k][i][i][i][i], Board[j][j][i][i][i][i] , Board[k][i][i][i][i][i]
	vs. the dict construction
		Board[coord] for coord in [ (x,  x  ,i,i,i,i) for x in [i,j,k] ]
		Board[coord] for coord in [ (x,k-x+i,i,i,i,i) for x in [i,j,k] ]

So, with a dict construction, attempting a low dimension task on a high dimension board requires low-dimension effort.

What happens when we attempt a high dimensional task?
	with lists we still run into the problem of (would you like to play on a 100-D board): Board[][]...[]
	with a dict we can generate coordingates (which does require some sophistication), but we don't have to deal with iterating in multiple dimensions
'''

'''
Let us
input = (in-a-row, [size d1, size d2, ... , size dn])
'''
'''
(how many tokens in a row to win, )
ie. ( |f| $_forall$  )
'''

# %% codecell
from sympy import *
from sympy import init_session
x,y,z = symbols('x y z')
Integral( 1/sqrt(x), x )

# %% codecell
input = (3, [4,4,4,4] )
inarow = input[0]
inarow
Ndim = len(input[1])
Ndims
dims = input[1]
dimss
import itertools

rangeDims = [ range(d) for d in dims]
rangeDims
spots = list(itertools.product(*rangeDims))

board = dict.fromkeys(spots, 0)
board

def openSpots(board):
	spots = []
	for spot,val in enumerate(board):
		if val == 0: spots.append(spot)
	return spots

def spotNAwayInDir(spt, n, drct):
	coord = []
	for i in range(Ndims):
		coord[i] = spt[i] + n*drct[i]


directions = list(itertools.product( *[ [0,1] for n in range(Ndims)] ))
def playEndedGame(board, lastMoveCoordinate):
	lastMoveCoordinate = LMC
	board[lastMoveCoordinate] = player
	for dir in direction:
		for n in range(-inarow-1, inarow +1 ):
			spotOnLine = [lastMoveCoordinate + n*dir[i] for i in range(Ndims)]
			if board[spotOnLine] == player: longestSeq += 1
			else: longestSeq = 0


'''
[sum([v[n] for v in vectorCombos]) for n in range(N)] for vectorCombos in combos]

board = {}
for v in list(itertools.product(range(2), repeat=4)):
	for n in N:
		if v[n] == 1:
			for k in range(1, dims[n]+1):



#Create the board
for n in len(dims):
	for dn in len(dims:
		for i in d:
spots = []
'''

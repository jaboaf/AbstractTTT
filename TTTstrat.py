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


def openSpots(board):
	spots = []
	for row in range( len(board) ):
		for col in range( len(board[row]) ):
			if board[row][col] == 0:
				spots.append( (row,col) )
	return spots

def upDiag(board):
	d = []
	for i in range( len(board) ):
		d.append( board[len(board)-1 - i][i] )
	return d

def downDiag(board):
	d = []
	for i in range( len(board) ):
		d.append( board[i][i] )
	return d

def P2W(board, player):
	if player == 'X':
		opp = 'O'
	elif player == 'O':
		opp = 'X'
	else:
		return -1

	lines = 0
	intersectPoints = 0
	points = dict.fromkeys(openSpots(board), 0)

	for c in range(len(board)):
		col = [ board[i][c] for i in range(len(board)) ]
		if opp not in col:
			if player in col:
				w = col.count(player)
				lines += 1
				for r in range(len(board)):
					if (r,c) in points:
						points[(r,c)] += (w+1)**2
			else:
				for r in range(len(board)):
					if (r,c) in points:
						points[(r,c)] += 1

	for r in range(len(board)):
		row = board[r]
		if opp not in row:
			if player in row:
				w = row.count(player)
				lines += 1
				for c in range(len(board)):
					if (r,c) in points:
						points[(r,c)] += (w+1)**2
			else:
				for c in range(len(board)):
					if (r,c) in points:
						points[(r,c)] += 1

	if opp not in upDiag(board):
		if player in upDiag(board):
			w = upDiag(board).count(player)
			lines += 1
			for i in range(len(board)):
				r = len(board) -1 -i
				c = i
				if (r,c) in points:
					points[(r,c)] += (w+1)**2
		else:
			for i in range(len(board)):
				r = len(board) -1 -i
				c = i
				if (r,c) in points:
					points[(r,c)] += 1

	if opp not in downDiag(board):
		if player in downDiag(board):
			w = downDiag(board).count(player)
			lines += 1
			for i in range(len(board)):
				if (i,i) in points:
					points[(i,i)] += (w+1)**2
		else:
			for i in range(len(board)):
				if (i,i) in points:
					points[(i,i)] += 1

	for v in points.values():
		if v >= 4:
			intersectPoints += 1

	return lines, intersectPoints, points

board = [	[0,0,0,0],
		[0,0,0,0],
		[0,0,0,0],
		[0,0,0,0] ]
'''
board = [	['X','O','X','X'],
			[0,'X',0,'O'],
			['X',0,'O',0],
			['O',0,0,'X'] ]
'''
b = [
[0,0,0],
[0,0,0],
[0,0,0]
]




val = {}
v = {}
v['X'] = P2W(board, 'X')[2]
v['O'] = P2W(board, 'O')[2]
maxs = {}

for point in openSpots(board):
	val[point] = v['X'][point] + v['O'][point]
	if val[point] in maxs:
		maxs[val[point]] += [point]
	else:
		maxs[val[point]] = [point]

pref = 0
goHere = (-1,-1)
for point in maxs[max(maxs)]:
	if v['X'][point] >= pref:
		pref = v['X'][point]
		goHere = point

print(v['X'])
print(v['O'])
print(val)
print(maxs[max(maxs)])
print(goHere)

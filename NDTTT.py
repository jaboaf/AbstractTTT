b = [ 	[	[0,0,0], [0,0,0], [0,0,0] ],
		[	[0,0,0], [0,0,0], [0,0,0] ],
		[	[0,0,0], [0,0,0], [0,0,0] ] ]

D = [3,3,3]
b = [ [ [0 for z in range(D[2])] for y in range(D[1])] for x in range(D[0]) ]


def openSpots(B):
	spots = []

	for p in b.keys() :
		if B[p] == 0:
			spots.append(p)

	return spots

def diags(B, point ):

	diagnols = []
	if point.count(0) + point.count( len(B)-1 ) == D : # Corner point
		
		for hold in range( D + 1 ):
			line = [ [-1 for j in range( D )] for k in range( N ) ]
			for c in range( D ):
				if c != hold:
					if point[c] = 0: 
						for i in range( N ):
							line[i][c] = point[c] + i
					else: # point[c] is max coordiate value aka = dimension -1
						for i in range( N ):
							line[i][c] = point[c] - i
				else:
					for i in range( N )
						line[i][c] = point[c]
			diagnols.append( line )

	elif point.count(0) + point.count( len(B)-1 ) == len(B) -1: # edge point not on corner
		i = 0 
		while hold == -1 :
			if point[i] != 0 and point[i] != len(B)-1:
				hold = i
			else:
				i += 1

		line = [ [-1 for j in range( D )] for k in range( N ) ]
		for c in range( D ):
			if c != hold:
				if point[c] = 0: 
					for i in range( N ):
						line[i][c] = point[c] + i
				else: # point[c] is max coordiate value aka = dimension -1
					for i in range( N ):
						line[i][c] = point[c] - i
			else:
				for i in range( N )
					line[i][c] = point[c]

		diagnols.append( line )


	elif point.count( ( len(B) -1 )/2 ) == len(B) -1: # center face
	else: # center

	for i in range( len(board) ):
		d.append( board[len(board)-1 - i][i] )
	return d

def downDiag(board):
	d = []
	for i in range( len(board) ):
		d.append( board[i][i] )
	return d
import copy

#Takes in a 3x3 board and returns a list of (row,col) coordinates of spots not filled with 'X' or 'O'
def openSpots(board):
	spots = []
	for row in range( len(board) ):
		for col in range( len(board[row]) ):
			if board[row][col] == 0:
				spots.append( (row,col) )
	return spots

#Takes in a 3x3 board and returns True if there is 3 in a row, and false otherwise
def isGameOver(board):
	#checking Rows
	if board[0][0] == board[0][1] == board[0][2] != 0:
		return True
	elif board[1][0] == board[1][1] == board[1][2] != 0:
		return True
	elif board[2][0] == board[2][1] == board[2][2] != 0:
		return True

	#Checking Cols
	elif board[0][0] == board[1][0] == board[2][0] != 0:
		return True
	elif board[0][1] == board[1][1] == board[2][1] != 0:
		return True
	elif board[0][2] == board[1][2] == board[2][2] != 0:
		return True

	#Checking Diagnols
	elif board[0][0] == board[1][1] == board[2][2] != 0:
		return True
	elif board[0][2] == board[1][1] == board[2][0] != 0:
		return True

	#No 3-in-a-row
	else:
		return False

#takes in a 3x3, rotates 90 degrees
def rot90(board):
	return [	[ board[2][0] , board[1][0] , board[0][0] ],
				[ board[2][1] , board[1][1] , board[0][1] ],
				[ board[2][2] , board[1][2] , board[0][2] ]		]

def rot180(board):
	return [	[ board[2][2] , board[2][1] , board[2][0] ],
				[ board[1][2] , board[1][1] , board[1][0] ],
				[ board[0][2] , board[0][1] , board[0][0] ]		]

def rot270(board):
	return [	[ board[0][2] , board[1][2] , board[2][2] ],
				[ board[0][1] , board[1][1] , board[2][1] ],
				[ board[0][0] , board[1][0] , board[2][0] ]		]

#takes in 3x3 board and reflects it over the line from 0,1 to 2,1
def flipOverVert(board):
	return [	[ board[0][2] , board[0][1] , board[0][0] ],
				[ board[1][2] , board[1][1] , board[1][0] ],
				[ board[2][2] , board[2][1] , board[2][0] ] ]

#takes in 3x3 board and reflects it over the line from 1,0 to 1,2
def flipOverHor(board):
	return [	board[2],
				board[1],
				board[0]	]

def flipOverUpRight(board):
	return [	[ board[2][2] , board[1][2] , board[0][2] ],
				[ board[2][1] , board[1][1] , board[0][1] ],
				[ board[2][0] , board[1][0] , board[0][0] ]		]

def flipOverDownLeft(board):
	return [	[ board[0][0] , board[1][0] , board[2][0] ],
				[ board[0][1] , board[1][1] , board[2][1] ],
				[ board[0][2] , board[1][2] , board[2][2] ]		]

def similar(check, memory):
	#check is the board that we want to "check" for similarity with boards in memory
	#memory is a list of boards that form a basis for a given number of moves
	for i in range(len(memory)):
		board = memory[i]
		if check[1][1] == board[1][1]:
			if board==flipOverVert(check) or board==flipOverHor(check) or board==flipOverUpRight(check) or board==flipOverDownLeft(check):
				return True, i
			elif board == rot180(check):
				return True, i
			elif board == rot90(check) or board == rot270(check):
				return True, i
			elif board == check:
				return True, i

	return False, len(memory)

#Xs are 1 and 0s are 2, empty spaces are 0
#uniq is a dictionary of unique boards
#	keys are number of moves
#	values are a list of unique boards formed the given number of moves
uniq = {}
uniq[0] =  [	[	[0, 0, 0],
					[0, 0, 0],
					[0, 0, 0]	]	]

#List of valid games to be played
gamesBefore = [ [0] ]
#List of valid games after being played
gamesAfter = []
gamesFinished = []

#Iterates over 'board statuses' ie. when there are x number of Xs or Os, where play = x 
for play in range(0,10):
	#Determining whose turn it is
	if play % 2 == 0:
		player = 'X'
	else:
		player = 'O'

	print('Play = ' + str(play) + ' , and player = ' + player)
	print(len(uniq[play]))

	basis = []
	#iterates over the unique boards
	#	Thought: should I only iterate over non-winning boards in the basis...
	for i in range(len(uniq[play])):

		U = uniq[play][i]
		possibleSpots = openSpots(U)

		for spot in possibleSpots:
			row = spot[0]
			col = spot[1]

			board = copy.deepcopy(U)
			board[row][col] = player

			sim = similar(board, basis)

			if sim[0] == False:
				basis.append(board)

	gamesBefore = copy.deepcopy(gamesAfter)
	uniq[play+1] = basis


for k in uniq:
	print('******** Basis for ' + str(k) + ' plays ****')
	if len(uniq[k]) < 13:
		for line in range(3):
			statment = ''
			for j in uniq[k]:
				statment += str(j[line][0]) + ',' + str(j[line][1]) + ',' + str(j[line][2])+  '  |  '
			print(statment)
	elif k != 9:
		for line in range(3):
			statment = ''
			for j in uniq[k][:13]:
				statment += str(j[line][0]) + ',' + str(j[line][1]) + ',' + str(j[line][2])+  '  |  '
			print(statment)
	else:
		for line in range(3):
			statment = ''
			for j in uniq[k][:13]:
				statment += str(j[line][0]) + ',' + str(j[line][1]) + ',' + str(j[line][2])+  '  |  '
			print(statment)
		print('-----------------------------------------------------------------------------------------------------')
		for line in range(3):
			statment = ''
			for j in uniq[k][13:]:
				statment += str(j[line][0]) + ',' + str(j[line][1]) + ',' + str(j[line][2])+  '  |  '
			print(statment)

for k in uniq:
	print(str(k) + '  ' + str(len(uniq[k])))

'''
for line in range(3):
	statment = ''
	for j in uniq[9][:15]:
		statment += str(j[line][0]) + ',' + str(j[line][1]) + ',' + str(j[line][2])+  '  |  '
	print(statment)
'''

print('-----------------------------------------------------------------------------------------------------')
'''
for line in range(3):
	statment = ''
	for j in uniq[9][15:]:
		statment += str(j[line][0]) + ',' + str(j[line][1]) + ',' + str(j[line][2])+  '  |  '
	print(statment)
'''












			
















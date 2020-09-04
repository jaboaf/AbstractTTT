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
terminalBasis = {}
nonTerminalBasis = {}

uniq[0] =  [	[	[0, 0, 0],
					[0, 0, 0],
					[0, 0, 0]	]	]

terminalBasis[0] = []
nonTerminalBasis[0] = [	[	[0, 0, 0],
							[0, 0, 0],
							[0, 0, 0]	]	]

#List of valid games to be played
relevantBefore = {}
relevantBefore[0] = [ [0] ]

#List of valid games after being played;
#	key = board # in nonTbasis
#	value= set of all games with that board played last 
relevantAfter = {}

duplicates = {}
duplicates['nonTerminal'] = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
duplicates['terminal'] = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}


gamesFinished = {0:[] , 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[] }
gamesContinued = {0:[] , 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[] }


#Iterates over 'board statuses' ie. when there are x number of Xs or Os, where play = x 
for play in range(0,10):
	#Determining whose turn it is
	if play % 2 == 0:
		player = 'X'
	else:
		player = 'O'

	print('Play = ' + str(play) + ' , and player = ' + player)
	print('Uniqs = ' + str(len(uniq[play])))
	print('nonTerminalBasis = ' + str(len(nonTerminalBasis[play])))
	print('terminalBasis = ' + str(len(terminalBasis[play])))

	nonTbasis = []
	Tbasis = []
	basis = []
	relevantAfter = {}
	#iterates over the unique boards
	#	Thought: should I only iterate over non-winning boards in the basis...
	for i in range(len(nonTerminalBasis[play])):

		U = nonTerminalBasis[play][i]
		possibleSpots = openSpots(U)

		for spot in possibleSpots:
			row = spot[0]
			col = spot[1]

			board = copy.deepcopy(U)
			board[row][col] = player

			basis = nonTbasis + Tbasis
			sim = similar(board, basis)

			#Board is Unique
			if sim[0] == False:
				if play < 4 or isGameOver(board) == False:
					#add board to the set of unique non-terminal boards
					nonTbasis.append(board)

				else:
					#add board to the set of unique terminal boards
					Tbasis.append(board)

			#Thought: when I append gamesAfter, should I append a 'relevantAfter' dict 
			#so we don't have to iterate at the begining
			if play < 4 or isGameOver(board) == False:
				for seq in relevantBefore[i]:
					if sim[1] in relevantAfter.keys():
						if seq + [sim[1]] in relevantAfter[ sim[1] ]:
							duplicates['nonTerminal'][play+1] += 1
						else:
							relevantAfter[ sim[1] ] += [ seq + [sim[1]] ]
					else:
						relevantAfter[ sim[1] ] = [ seq + [sim[1]] ]

			else:
				for seq in relevantBefore[i]:
					if seq + [sim[1]] in gamesFinished[play]:
						duplicates['terminal'][play+1] += 1
					else:
						gamesFinished[play+1] += [ seq + [sim[1]] ]

	print('Number of games relevantAfter')
	total = 0
	for i in relevantAfter:
		total += len( relevantAfter[i] )
	print(total)

	print('Number of gamesFinished')
	print(len(gamesFinished[play]))

	gamesContinued[play+1] = total
	relevantBefore = copy.deepcopy(relevantAfter)

	nonTerminalBasis[play+1] = nonTbasis
	terminalBasis[play+1] = Tbasis
	uniq[play+1] = nonTbasis + Tbasis


for k in uniq:
	print('******** Basis for ' + str(k) + ' plays ****')
	if len(uniq[k]) < 16:
		print('     *** nonTerminalBasis ***')
		for line in range(3):
			statment = ''
			for j in nonTerminalBasis[k]:
				statment += str(j[line][0]) + ',' + str(j[line][1]) + ',' + str(j[line][2])+  '  |  '
			print('     ' + statment)
		print('     *** terminalBasis ***')
		for line in range(3):
			statment = ''
			for j in terminalBasis[k]:
				statment += str(j[line][0]) + ',' + str(j[line][1]) + ',' + str(j[line][2])+  '  |  '
			print('     ' + statment)
	else:
		print('     *** nonTerminalBasis ***')
		for line in range(3):
			statment = ''
			for j in nonTerminalBasis[k][:12]:
				statment += str(j[line][0]) + ',' + str(j[line][1]) + ',' + str(j[line][2])+  '  |  '
			print('     ' + statment)
		print('     *** terminalBasis ***')
		for line in range(3):
			statment = ''
			for j in terminalBasis[k][:12]:
				statment += str(j[line][0]) + ',' + str(j[line][1]) + ',' + str(j[line][2])+  '  |  '
			print('     ' + statment)

		

for k in uniq:
	print(str(k) + '     ' + str(len(uniq[k])) + '     ' + str(len(nonTerminalBasis[k])) + '     ' +  str(len(terminalBasis[k])))

'''
for line in range(3):
	statment = ''
	for j in uniq[9][:15]:
		statment += str(j[line][0]) + ',' + str(j[line][1]) + ',' + str(j[line][2])+  '  |  '
	print(statment)
'''

print('-----------------------------------------------------------------------------------------------------')
for k in gamesFinished:
	print('gamesFinished   ' + str(len(gamesFinished[k]))  + '   terminal duplicates   ' + str(duplicates['terminal'][k]))

print('-----------------------------------------------------------------------------------------------------')
for k in gamesContinued:
	print('gamesContinued   ' + str(gamesContinued[k])  + '   non-terminal duplicates   ' + str(duplicates['nonTerminal'][k]))



'''
for line in range(3):
	statment = ''
	for j in uniq[9][15:]:
		statment += str(j[line][0]) + ',' + str(j[line][1]) + ',' + str(j[line][2])+  '  |  '
	print(statment)
'''












			
















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
		return True, board[0][0]
	elif board[1][0] == board[1][1] == board[1][2] != 0:
		return True, board[1][0]
	elif board[2][0] == board[2][1] == board[2][2] != 0:
		return True, board[2][0]

	#Checking Cols
	elif board[0][0] == board[1][0] == board[2][0] != 0:
		return True, board[0][0]
	elif board[0][1] == board[1][1] == board[2][1] != 0:
		return True, board[0][1]
	elif board[0][2] == board[1][2] == board[2][2] != 0:
		return True, board[0][2]

	#Checking Diagnols
	elif board[0][0] == board[1][1] == board[2][2] != 0:
		return True, board[0][0]
	elif board[0][2] == board[1][1] == board[2][0] != 0:
		return True, board[0][2]

	#No 3-in-a-row
	else:
		return False, 0

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

#dict of valid games after being played;
#	key1 = # of Xs and Os
#	value= dict of distinct games
#		key2 = last board played (from 0 to len(nonTerminalBasis[key1]) )
#		value = set of games with nonTerminalBasis[key1][key2] board played last
gamesContinued = { 0: { 0: [ [0] ] } , 1:{} , 2:{} , 3:{} , 4:{} , 5:{} , 6:{} , 7:{} , 8:{} , 9:{} , 10:{}  }
gamesFinished = { 0:{} , 1:{} , 2:{} , 3:{} , 4:{} , 5:{} , 6:{} , 7:{} , 8:{} , 9:{} , 10:{}  }

gameCount = {	'nonTerminal'	: { 'duplicates': {} ,
									'nonDuplicates' : {} },

				'terminal'		: { 'duplicates': {} ,
									'nonDuplicates' : { 'X' : {},
														'O' : {} }	}	}

gameCount['nonTerminal']['nonDuplicates'] = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
gameCount['nonTerminal']['duplicates'] = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}

gameCount['terminal']['nonDuplicates']['X'] = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
gameCount['terminal']['nonDuplicates']['O'] = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
gameCount['terminal']['duplicates'] = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}


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
	dealWithAfter = {}
	playedNextRound = 0
	endedThisRound = 0
	#iterates over the unique boards
	#	Thought: should I only iterate over non-winning boards in the basis...
	for i in range(len(gamesContinued[play])):
		dealWithAfter[i] = []

		U = nonTerminalBasis[play][i]
		possibleSpots = openSpots(U)

		for spot in possibleSpots:
			row = spot[0]
			col = spot[1]

			board = copy.deepcopy(U)
			board[row][col] = player

			#Thought: when I append gamesAfter, should I append a 'relevantAfter' dict 
			#so we don't have to iterate at the begining
			if play < 4 or isGameOver(board)[0] == False:
				sim = similar(board, nonTbasis)

				if sim[0] == False:
					nonTbasis.append(board)

				for seq in gamesContinued[play][i]:
					if sim[1] in gamesContinued[play+1].keys():
						newSeq = seq + [sim[1]]
						if newSeq in gamesContinued[play+1][ sim[1] ]:
							gameCount['nonTerminal']['duplicates'][play+1] += 1
						else:
							gameCount['nonTerminal']['nonDuplicates'][play+1] += 1
							gamesContinued[play+1][ sim[1] ] += [ seq + [sim[1]] ]
					else:
						gamesContinued[play+1][ sim[1] ] = [ seq + [sim[1]] ]
						gameCount['nonTerminal']['nonDuplicates'][play+1] += 1
			else:
				dealWithAfter[i] += [ board ]

	for i in dealWithAfter:
		for board in dealWithAfter[i]:
			sim = similar(board, Tbasis)

			if sim[0] == False:
				Tbasis.append(board)

			basisIndex = len(nonTbasis) + sim[1]

			winner = isGameOver(board)[1]

			for seq in gamesContinued[play][i]:
				if basisIndex in gamesFinished[play+1].keys():
					newSeq = seq + [basisIndex]

					if newSeq in gamesFinished[play+1][ basisIndex ]:
						gameCount['terminal']['duplicates'][play+1] += 1

					else:
						gameCount['terminal']['nonDuplicates'][winner][play+1] += 1
						gamesFinished[play+1][ basisIndex ] += [ seq + [basisIndex] ]

				else:
					gameCount['terminal']['nonDuplicates'][winner][play+1] += 1
					gamesFinished[play+1][ basisIndex ] = [ seq + [basisIndex] ]
					

	print('Number of games to be played next round')
	print(gameCount['nonTerminal']['nonDuplicates'][play+1])

	print('Number of games ended this round with X win')
	print(gameCount['terminal']['nonDuplicates']['X'][play+1])

	print('Number of games ended this round with O win')
	print(gameCount['terminal']['nonDuplicates']['O'][play+1])

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
for k in range(11):
	print('terminal nonDuplicates: X wins:' + str(gameCount['terminal']['nonDuplicates']['X'][k])  + ' O Wins: ' + str(gameCount['terminal']['nonDuplicates']['O'][k]))

print('-----------------------------------------------------------------------------------------------------')
for k in range(11):
	print('nonTerminal: nonDuplicates: ' + str(gameCount['nonTerminal']['nonDuplicates'][k])  + ' duplicates: ' + str(gameCount['nonTerminal']['duplicates'][k]))

print('-----------------------------------------------------------------------------------------------------')

'''
for line in range(3):
	statment = ''
	for j in uniq[9][15:]:

		statment += str(j[line][0]) + ',' + str(j[line][1]) + ',' + str(j[line][2])+  '  |  '
	print(statment)
'''












			
















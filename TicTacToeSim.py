import copy


class game:

	#seqOfB is the sequence of unique boards
	#	[	[ [ , , ] , [ , , ], [ , , ] ]	, ... , [ [ , , ] , [ , , ], [ , , ] ]	]
	#curB is the current Board
	#	[	[ , , ] , [ , , ], [ , , ]	]
	done = False
	winner = 0

	def __init__(self, priorBs , startB):
		self.seqOfB = priorBs
		self.curB = startB

	def get(self, arg):
		if arg == 'seqOfB':
			return self.seqOfB
		elif arg == 'curB':
			return self.curB
		elif arg == 'done':
			return self.done
		elif arg == 'winner':
			return self.winner
		else:
			return -1

	def openSpots(self):
		spots = []
		for row in range(3):
			for col in range(3):
				if self.curB[row][col] == 0:
					spots.append( (row,col) )
		return spots

	def checkGameOver(self):
		#Check 3 places in a row for the same value thats not 0:
		#	game is done
		#	winner is the value of those three places
		#Checking Rows
		if self.curB[0][0] == self.curB[0][1] == self.curB[0][2] !=0:
			done = True
			winner = curB[0][0]
		elif self.curB[1][0] == self.curB[1][1] == self.curB[1][2] !=0:
			done = True
			winner = curB[1][0]
		elif self.curB[2][0] == self.curB[2][1] == self.curB[2][2] !=0:
			done = True
			winner = curB[2][0]
		#Checking Cols
		elif self.curB[0][0] == self.curB[1][0] == self.curB[2][0] !=0:
			done = True
			winner = curB[0][0]
		elif self.curB[0][1] == self.curB[1][1] == self.curB[2][1] !=0:
			done = True
			winner = curB[0][1]
		elif self.curB[0][2] == self.curB[1][2] == self.curB[2][2] !=0:
			done = True
			winner = curB[0][2]
		#Checking Diagnols
		elif self.curB[0][0] == self.curB[1][1] == self.curB[2][2] !=0:
			done = True
			winner = curB[0][0]
		elif self.curB[0][2] == self.curB[1][1] == self.curB[2][0] !=0:
			done = True
			winner = curB[0][2]

	def play(self, player, row, col , uniqBnum):
		if player == 'X':
			if self.curB[row][col] == 0:
				self.seqOfB.append(uniqBnum)
				self.curB[row][col] = 1
				self.checkGameOver()
			else:
				return -1
		elif player =='O':
			if self.curB[row][col] == 0:
				self.seqOfB.append(uniqBnum)
				self.curB[row][col] = 2
				self.checkGameOver()
			else:
				return -1
		else:
			return -1


def rot90(board):
	new = [	[None, None, None],
			[None, None, None],
			[None, None, None]]
	new[0] = [ board[2][0] , board[1][0] , board[0][0] ]
	new[1] = [ board[2][1] , board[1][1] , board[0][1] ]
	new[2] = [ board[2][2] , board[1][2] , board[0][2] ]
	return new

def rot180(board):
	new = [	[None, None, None],
			[None, None, None],
			[None, None, None]]
	new[0] = [ board[2][2] , board[2][1] , board[2][0] ]
	new[1] = [ board[1][2] , board[1][1] , board[1][0] ]
	new[2] = [ board[0][2] , board[0][1] , board[0][0] ]
	return new

def rot270(board):
	new = [	[None, None, None],
			[None, None, None],
			[None, None, None]]
	new[0] = [ board[2][0] , board[1][0] , board[0][0] ]
	new[1] = [ board[2][1] , board[1][1] , board[0][1] ]
	new[2] = [ board[2][2] , board[1][2] , board[0][2] ]
	return new

def flipOverVert(board):
	new = [	[None, None, None],
			[None, None, None],
			[None, None, None]]
	new[0] = [ board[0][2] , board[0][1] , board[0][0] ]
	new[1] = [ board[1][2] , board[1][1] , board[1][0] ]
	new[2] = [ board[2][2] , board[2][1] , board[2][0] ]
	return new

def flipOverHor(board):
	new = [	[None, None, None],
			[None, None, None],
			[None, None, None]]
	new[0] = board[2]
	new[1] = board[1]
	new[2] = board[0]
	return new

def flipOverUpRight(board):
	new = [	[None, None, None],
			[None, None, None],
			[None, None, None]]
	new[0] = [ board[2][2] , board[1][2] , board[0][2] ]
	new[1] = [ board[2][1] , board[1][1] , board[0][1] ]
	new[2] = [ board[2][0] , board[1][0] , board[0][0] ]
	return new

def flipOverDownLeft(board):
	new = [	[None, None, None],
			[None, None, None],
			[None, None, None]]
	new[0] = [ board[0][0] , board[1][0] , board[2][0] ]
	new[1] = [ board[0][1] , board[1][1] , board[2][1] ]
	new[2] = [ board[0][2] , board[1][2] , board[2][2] ]
	return new


def similar(check, memory):
	for board in memory:
		if check[2][2] == board[2][2]:
			if board==flipOverVert(check) or board==flipOverHor(check) or board==flipOverUpRight(check) or board==flipOverDownLeft(check):
				uniqB = memory.index(board) #finding unique board number
				return True , uniqB
			elif board == rot180(check):
				uniqB = memory.index(board)
				return True , uniqB
			elif board == rot90(check) or board == rot270(check):
				uniqB = memory.index(board)
				return True , uniqB
	return False , len(memory)

#Xs are 1 and 0s are 2, empty spaces are 0
#uniq is a dictionary of unique boards
#	keys are number of moves
#	values are a list of unique boards formed the given number of moves
uniq = {}
blank = [	[0, 0, 0],
			[0, 0, 0],
			[0, 0, 0]	] 


openGames = [ game([], blank ) ]
endedGames = {}

for turn in range(0,2):
	turnUniqs = []
	nextMove = []
	noNextMove = []

	if turn % 2 == 1:
		player = 'O'
	else:
		player = 'X'

	for g in openGames:

		currentBoard = g.get('curB')

		print('*************')
		print(currentBoard[0])
		print(currentBoard[1])
		print(currentBoard[2])
		print(g.openSpots())

		for spot in g.openSpots():
			row = spot[0]
			col = spot[1]

			newG = game(g.get('seqOfB') , currentBoard)
			newG.play(player, row, col, 1)

			if newG.get('done') == True:
				noNextMove.append(newG)
			else:
				nextMove.append(newG)

	uniq[turn] = turnUniqs
	endedGames[turn] = noNextMove
	openGames = nextMove

for k in uniq:
	print(str(k) + '  ' + str(len(uniq[k])))

for k in uniq[0]:
	print(k[0])
	print(k[1])
	print(k[2])
	print('-----')







			
















#This is my version of TicTacToe
#I'm implementing this as a Breakable Toy, so it will likely be way overengineered, but that's the point
import copy

class Game:

	"""This class controls the game loop and annouces the result of the game. """

	def __init__(self):
		self.board = Board()
		self.player1 = None
		self.player2 = None
			
	def announceResult(self, result):
		if result == 0:
			print("Shockingly, it\'s a draw!!!")
		elif result == 1:
			print("Player 1 is the winner!")
		elif result == 2:
			print("Player 2 is the winner!")
		else:
			print("Invalid result!!!")
		

	def gameLoop(self):
		if self.player1.getSymbol() == 'X':
			currentPlayer = self.player1
		else:
			currentPlayer = self.player2
		while 1:
			self.board.displayBoard(self.board)
			if self.board.hasValidMove(self.board):
				print("Before we call requestMove(), openSpaces is equal to: ", self.board.getOpenSpaces())
				boardCopy = copy.deepcopy(self.board)
				move = currentPlayer.requestMove(boardCopy)
				print("After we call requestMove(), openSpaces is equal to: ", self.board.getOpenSpaces())
				self.board = self.board.makeMove(self.board, move, currentPlayer.getSymbol())
				if self.board.checkForWinner(self.board):
					break
				else:
					if currentPlayer == self.player1:
						currentPlayer = self.player2
					else:
						currentPlayer = self.player1
					continue

			else:
				break
		
	
	def gameSetup(self):
		print()
		numberOfPlayers = int(input("Please enter the number of players: "))
		while numberOfPlayers < 0 and numberOfPlayers > 2:
			numberOfPlayers = input("Please enter the number of players: ")
		whichPlayerIsX = int(input("Which player shall play as 'X', player 1 or player 2? "))
		while whichPlayerIsX < 1 and whichPlayerIsX > 2:
			whichPlayerIsX = input("Which player shall play as 'X', player 1 or player 2? ")
		
		if numberOfPlayers == 2:
			if whichPlayerIsX == 1:
				self.player1 = HumanPlayer('X')
				self.player2 = HumanPlayer('O')
			else:
				self.player2 = HumanPlayer('X')
				self.player1 = HumanPlayer('O')
		elif numberOfPlayers == 1:
			if whichPlayerIsX == 1:
				self.player1 = HumanPlayer('X')
				self.player2 = ComputerPlayer('O')
			else:
				self.player2 = ComputerPlayer('X')
				self.player1 = HumanPlayer('O')
		else:
			if whichPlayerIsX == 1:
				self.player1 = ComputerPlayer('X')
				self.player2 = ComputerPlayer('O')
			else:
				self.player2 = ComputerPlayer('X')
				self.player1 = ComputerPlayer('O')
	
	def getBoard(self):
		return self.board
		

class Board:
	"""Holds the board state and handles making the moves"""

	def __init__(self):
		self.board = []
		self.rows = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
		for i in range(9):
			self.board.append(Square(0, i))
		self.openSpaces = list(range(9))

	def hasValidMove(self, board):
		for i in range(len(board.board)):
			if board.board[i].getState() == 0:
				return True
		return False

	def makeMove(self, board, move, symbol):
		board.board[move].setState(symbol)
		board.openSpaces.remove(move)
		return board
		

	def displayBoard(self, board):
		print()
		print("{0}|{1}|{2}".format(board.board[0].getDisplay(), board.board[1].getDisplay(), board.board[2].getDisplay()))
		print("-----")
		print("{0}|{1}|{2}".format(board.board[3].getDisplay(), board.board[4].getDisplay(), board.board[5].getDisplay()))
		print("-----")
		print("{0}|{1}|{2}".format(board.board[6].getDisplay(), board.board[7].getDisplay(), board.board[8].getDisplay()))

	def checkForWinner(self, board):
		for row in board.rows:
			rowTotal = self.getRowTotal(row)
			if rowTotal == 3:
				return 1
			elif rowTotal == 30:
				return 2
			else:
				continue
		return 0
		
	def getRowTotal(self, row):
		rowTotal = 0
		for cell in row:
			if self.board[cell].getState() == game.player1.getSymbol():
				rowTotal += 1
			elif self.board[cell].getState() == game.player2.getSymbol():
				rowTotal += 10
		
		return rowTotal
		
	def getRows(self):
		return self.rows
	
	def isValidMove(self, board, move):
		return (move >= 0 and move <= 8 and board.openSpaces.count(move) != 0)
	
	def getOpenSpaces(self):
		return self.openSpaces
		
class Square:
	"""Holds the state for each square, as well as the display character."""

	def __init__(self, state, display):
		self.state = state
		self.display = display
	
	def getState(self):
		return self.state

	def setState(self, state):
		self.state = state
		self.display = state

	def getDisplay(self):
		return self.display

		
class Player:
	"""Holds the symbol that each player is using as well the requestMove() method to request (or calculate in the case of a computer opponent) the move"""

	def __init__(self, symbol):
		self.playerSymbol = symbol
		if symbol == 'X':
			self.opponentSymbol = 'O'
		else:
			self.opponentSymbol = 'X'

	def requestMove(self, board):
		"""we're just going to be overriding this.  there should never be a generic Player object that will receive a call to this..."""
		pass
	
	def getSymbol(self):
		return self.playerSymbol

class HumanPlayer(Player):
	"""subclass for Human Players.  We'll be moving the requestMove() methoed into the parent and overriding in here and in ComputerPlayer"""
	
	# def __init__(self, symbol):
		# self.playerSymbol = symbol
		
	def requestMove(self, board):
		move = int(input("Please input the number of the square for your move: "))
		while not board.isValidMove(board, move):
			print("That is not a valid move.")
			board.displayBoard(board)
			move = int(input("Please input the number of the square for your move: "))
	
		return move
		
class ComputerPlayer(Player):
	"""sub for computer players"""
	
	# def __init__(self, symbol):
		# self.playerSymbol = symbol
		
	def requestMove(self, board):
		#initially the algo here will be rather simple, basically looking at the rows with the closest for a win for either player
		#making a move in that same row.  Later on, I'll setup some kind of tree like Micah Martin suggested
		#for Jake Scruggs to do.
		#it was actually the minimax algo that was suggested, (though that traces the moves like a tree)
		move = self.minMax(board)
		print(move)
		return move
	
	def minMax(self, board)
		return myMax(board)
	
	def myMax(self, board):
		if not board.hasValidMove(board):
			return board.checkForWinner(board)
		
		best_move = None
		#max = -10000
		validMoves = board.getOpenSpaces()
		for move in validMoves:
			move = opponentMove(board.makeMove(move))
			if 
			boardCopy = copy.deepcopy(board)
			boardCopy.makeMove(boardCopy, move, self.playerSymbol)
			result = self.opponentMax(boardCopy)
			if result > max:
				max = result
				return move
		
		return max
	
	def opponentMax(self, board):
		validMoves = board.getOpenSpaces()
		
		if not board.hasValidMove(board):
			return board.checkForWinner(board)
		
		min = 10000
		for move in validMoves:
			boardCopy = copy.deepcopy(board)
			boardCopy.makeMove(boardCopy, move, self.opponentSymbol)
			result = self.minMax(boardCopy)
			if result < min:
				min = result
		
		return min

#start the show
game = Game()

print("Welcome to PyTacToe!")
game.gameSetup()
game.gameLoop()
result = game.board.checkForWinner(game.board)
game.board.displayBoard(game.board)
game.announceResult(result)


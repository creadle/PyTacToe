#This is my version of TicTacToe
#I'm implementing this as a Breakable Toy, so it will likely be way overengineered, but that's the point
import random

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
				move = currentPlayer.requestMove()
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

	def hasValidMove(self, board):
		for i in range(len(board.board)):
			if board.board[i].getState() == 0:
				return True
		return False

	def makeMove(self, board, move, symbol):
		board.board[move].setState(symbol)
		return board
		

	def displayBoard(self, board):
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
		return (move >= 0 and move <= 8 and board.board[move].getState() == 0)

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

	def requestMove(self):
		"""we're just going to be overriding this.  there should never be a generic Player object that will receive a call to this..."""
		pass
	
	def getSymbol(self):
		return self.playerSymbol

class HumanPlayer(Player):
	"""subclass for Human Players.  We'll be moving the requestMove() methoed into the parent and overriding in here and in ComputerPlayer"""
	
	# def __init__(self, symbol):
		# self.playerSymbol = symbol
		
	def requestMove(self):
		move = int(input("Please input the number of the square for your move: "))
		while not game.board.isValidMove(move):
			print("That is not a valid move.")
			game.board.displayBoard()
			move = int(input("Please input the number of the square for your move: "))
	
		return move
		
class ComputerPlayer(Player):
	"""sub for computer players"""
	
	# def __init__(self, symbol):
		# self.playerSymbol = symbol
		
	def requestMove(self):
		#initially the algo here will be rather simple, basically looking at the rows with the closest for a win for either player
		#making a move in that same row.  Later on, I'll setup some kind of tree like Micah Martin suggested
		#for Jake Scruggs to do.
		#it was actually the minimax algo that was suggested, (though that traces the moves like a tree)
		random.seed()
		
		if self.playerSymbol == game.player1.getSymbol():
			myTotal = 2
			opponentTotal = 20
		else:
			myTotal = 20
			opponentTotal = 2
		candidateMoves = []
		strongCandidates = []
		for row in game.board.getRows():
			validMoves = []
			total = game.board.getRowTotal(row)
			
			#if it's a winning move we want it at the top of the list, and blocking moves at the bottom
			#either way, we return the first move in the list
			if total == myTotal:
				validMoves.extend(self.determineValidMovesInRow(row))
				strongCandidates[0:] = validMoves
			elif total == opponentTotal:
				validMoves.extend(self.determineValidMovesInRow(row))
				strongCandidates.extend(validMoves)
			else:
				validMoves.extend(self.determineValidMovesInRow(row))
				candidateMoves.extend(validMoves)
		
		if len(strongCandidates) > 0:
			return strongCandidates[0]
		else:
			#since we don't have a winning or blocking move, pick a random choice from among the valid moves
			return candidateMoves[random.randint(0,len(candidateMoves) - 1)]
						
	def determineValidMovesInRow(self, row):
		moves = []
		for square in row:
			if game.board.isValidMove(game.board, square):
				moves.append(square)
		return moves
						
		

#start the show
game = Game()

print("Welcome to PyTacToe!")
game.gameSetup()
game.gameLoop()
result = game.board.checkForWinner(game.board)
game.board.displayBoard(game.board)
game.announceResult(result)


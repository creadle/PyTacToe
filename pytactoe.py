#This is my version of TicTacToe
#I'm implementing this as a Breakable Toy, so it will likely be way overengineered, but that's the point

class Game:

	"""This class controls the game loop and annouces the winner if there is one. """

	def __init__(self):
		self.board = Board()
			
	def announceResult(self, result):
		pass

	def hasWinner(self):
		pass

	def gameLoop(self):
		pass

	def gameSetup(self):
		pass

class Board:
	"""Holds the board state and handles making the moves"""

	def __init__(self):
		self.board = [9]
		self.rows = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

	def hasValidMove(self):
		pass

	def makeMove(self, move):
		pass

	def displayBoard(self):
		pass

class Player:
	"""Holds the symbol that each player is using"""

	def __init__(self, symbol):
		self.playerSymbol = symbol


#start the show
game = Game()

print "Welcome to PyTacToe!"
game.gameSetup(game)
game.gameLoop(game)
game.announceResult(game)


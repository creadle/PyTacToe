#This is my version of TicTacToe
#I'm implementing this as a Breakable Toy, so it will likely be way overengineered, but that's the point

class Game:

	"""This class controls the game loop and annouces the winner if there is one. """

	def __init__(self):
		self.board = Board()
			
	def announceResult(self, result):
		if result == 0:
			print "It's a draw!"
		elif result == 1:
			print "Player 1 is the winner!"
		elif result == 2:
			print "Player 2 is the winner!"
		else:
			print "Shockingly, it's a draw!!!"
		

	def gameLoop(self):
		symbol = player1.playerSymbol
		while 1:
			board.displayBoard(board)
			if board.hasValidMove(board):
				move = raw_input("Please input the number of the square for your move:")
				while move < 0 || move > 8 || board.filled[move]:
					print " That is not a valid move.\n"
					move = raw_input("Please input the number of the square for your move:")

				board.makeMove(board, move, symbol)
				winner = board.checkForWinner(board)
				if winner == 1:
					announceResult(self, winner)
				else if winner == 2:
					announceResult(self, winner)
				else:
					if symbol == player1.playerSymbol:
						symbol = player2.playerSymbol
					else:
						symbol = player1.playerSymbol
					continue

			else:
				break


	def gameSetup(self):
		print "\n"
		symbol = raw_input("Shall Player 1 be 'X' or 'O'?")
		while symbol != "X" || symbol != "O":
			symbol = raw_input("Shall Player 1 be 'X' or 'O'?")

		if symbol = "X":
			self.player1 = Player("X")
			self.player2 = Player("O")
		else:
			self.player1 = Player("O")
			self.player2 = Player("X")


class Board:
	"""Holds the board state and handles making the moves"""

	def __init__(self):
		self.board = []
		self.filled = [0,0,0,0,0,0,0,0,0]
		self.rows = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

	def hasValidMove(self):
		pass

	def makeMove(self, move, symbol):
		pass

	def displayBoard(self):
		pass

	def checkForWinner(self):
		pass

		
class Player:
	"""Holds the symbol that each player is using"""

	def __init__(self, symbol):
		self.playerSymbol = symbol


#start the show
game = Game()

print "Welcome to PyTacToe!\n"
game.gameSetup(game)
game.gameLoop(game)
result = game.board.checkForWinner(game.board)
game.announceResult(game, result)


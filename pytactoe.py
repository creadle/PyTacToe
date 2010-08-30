#This is my version of TicTacToe
#I'm implementing this as a Breakable Toy, so it will likely be way overengineered, but that's the point

class Game:

	"""This class controls the game loop and annouces the result of the game. """

	def __init__(self):
		self.board = Board()
			
	def announceResult(self, result):
		if result == 0:
			print("Shockingly, it\'s a draw!!!")
			pass
		elif result == 1:
			print("Player 1 is the winner!")
		elif result == 2:
			print("Player 2 is the winner!")
		else:
			print("Invalid result!!!")
		

	def gameLoop(self):
		symbol = player1.playerSymbol
		while 1:
			board.displayBoard(board)
			if board.hasValidMove(board):
				move = raw_input("Please input the number of the square for your move:")
				while move < 0 or move > 8 or board.board[move]:
					print("That is not a valid move.\n")
					move = raw_input("Please input the number of the square for your move:")

				board.makeMove(board, move, symbol)
				if board.checkForWinner(board):
					break
				else:
					continue

			else:
				break


	def gameSetup(self):
		print("\n")
		symbol = raw_input("Shall Player 1 be 'X' or 'O'?")
		while symbol != "X" or symbol != "O":
			symbol = raw_input("Shall Player 1 be 'X' or 'O'?")

		if symbol == "X":
			self.player1 = Player("X")
			self.player2 = Player("O")
		else:
			self.player1 = Player("O")
			self.player2 = Player("X")


class Board:
	"""Holds the board state and handles making the moves"""

	def __init__(self):
		self.board = [0,0,0,0,0,0,0,0,0]
		self.rows = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

	def hasValidMove(self):
		for square in self.board:
			if square == 0:
				return True
			return False

	def makeMove(self, move, symbol):
		self.board[move] = symbol

	def displayBoard(self):
		print "{1s}|{1s}|{1s}".format(self.board[0], self.board[1], self.board[2])
		print "-----"
		print "{1s}|{1s}|{1s}".format(self.board[3], self.board[4], self.board[5])
		print "-----"
		print "{1s}|{1s}|{1s}".format(self.board[6], self.board[7], self.board[8])

	def checkForWinner(self):
		for row in self.rows:
			rowTotal = 0
			for cell in row:
				if cell == game.player1.playerSymbol:
					rowTotal += 1
				elif cell == "O":
					rowTotal += 10
			if rowTotal = 3:
				return 1
			elif rowTotal = 30:
				return 2
			else:
				return 0

		
class Player:
	"""Holds the symbol that each player is using"""

	def __init__(self, symbol):
		self.playerSymbol = symbol


#start the show
game = Game()

print("Welcome to PyTacToe!\n")
game.gameSetup(game)
game.gameLoop(game)
result = game.board.checkForWinner(game.board)
game.announceResult(game, result)


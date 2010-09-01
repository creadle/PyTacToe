#This is my version of TicTacToe
#I'm implementing this as a Breakable Toy, so it will likely be way overengineered, but that's the point

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
		symbol = self.player1.playerSymbol
		while 1:
			self.board.displayBoard()
			if self.board.hasValidMove():
				move = self.requestMove()
				self.board.makeMove(move, symbol)
				if self.board.checkForWinner():
					break
				else:
					if symbol == self.player1.playerSymbol:
						symbol = self.player2.playerSymbol
					else:
						symbol = self.player1.playerSymbol
					continue

			else:
				break
	
	def requestMove(self):
		move = int(input("Please input the number of the square for your move: "))
		while not self.isValidMove(move):
			print("That is not a valid move.")
			self.board.displayBoard()
			move = int(input("Please input the number of the square for your move: "))
		
		return move

	def isValidMove(self, move):
		return (move >= 0 and move <= 8 and self.board.board[move].getState() == 0)
	
	
	def gameSetup(self):
		print()
		symbol = input("Shall Player 1 be 'X' or 'O'?")
		while symbol != "X" and symbol != "O":
			symbol = input("Shall Player 1 be 'X' or 'O'?")

		if symbol == "X":
			self.player1 = Player("X")
			self.player2 = Player("O")
		else:
			self.player1 = Player("O")
			self.player2 = Player("X")


class Board:
	"""Holds the board state and handles making the moves"""

	def __init__(self):
		self.board = []
		self.rows = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
		for i in range(9):
			self.board.append(Square(0, i))

	def hasValidMove(self):
		for i in range(len(self.board)):
			if self.board[i].getState() == 0:
				return True
		return False

	def makeMove(self, move, symbol):
		self.board[move].setState(symbol)

	def displayBoard(self):
		print("{0}|{1}|{2}".format(self.board[0].getDisplay(), self.board[1].getDisplay(), self.board[2].getDisplay()))
		print("-----")
		print("{0}|{1}|{2}".format(self.board[3].getDisplay(), self.board[4].getDisplay(), self.board[5].getDisplay()))
		print("-----")
		print("{0}|{1}|{2}".format(self.board[6].getDisplay(), self.board[7].getDisplay(), self.board[8].getDisplay()))

	def checkForWinner(self):
		for row in self.rows:
			rowTotal = 0
			for cell in row:
				if self.board[cell].getState() == game.player1.playerSymbol:
					rowTotal += 1
				elif self.board[cell].getState() == game.player2.playerSymbol:
					rowTotal += 10
			if rowTotal == 3:
				return 1
			elif rowTotal == 30:
				return 2
			else:
				continue
		return 0

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
	"""Holds the symbol that each player is using"""

	def __init__(self, symbol):
		self.playerSymbol = symbol


#start the show
game = Game()

print("Welcome to PyTacToe!")
game.gameSetup()
game.gameLoop()
result = game.board.checkForWinner()
game.board.displayBoard()
game.announceResult(result)


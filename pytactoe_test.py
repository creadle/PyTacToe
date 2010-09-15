import unittest
import pytactoe

class Board_Test(unittest.TestCase):
	def setUp(self):
		self.playerO = pytactoe.Player()
		self.playerX = pytactoe.Player('X', "Player X", self.playerO)
		self.playerO = pytactoe.Player('O', "Player O", self.playerX)
		self.nonWinningBoard = pytactoe.Board()
		self.winningBoardForX = pytactoe.Board()
		self.winningBoardForO = pytactoe.Board()
		for i in self.winningBoardForX.rows[0]:
			self.winningBoardForX.board[i].setState(self.playerX.playerSymbol)
		#self.winningBoardForX = ['X', 'X', 'X', 0, 0, 0, 0, 0, 0]
		for i in self.winningBoardForO.rows[0]:
			self.winningBoardForO.board[i].setState(self.playerO.playerSymbol)
		#self.winningBoardForO = ['O', 'O', 'O', 0, 0, 0, 0, 0, 0]
	
	def draw_Test(self):
		result = self.nonWinningBoard.checkForWinner(self.nonWinningBoard, self.playerX)
		assert result == 0
	
	def winForX_Test(self):
		result = self.winningBoardForX.checkForWinner(self.winningBoardForX, self.playerX)
		assert result == 1
		
	def winForO_Test(self):
		result = self.winningBoardForO.checkForWinner(self.winningBoardForO, self.playerX)
		assert result == -1
		
class ComputerPlayerBlockingMove_Test(unittest.TestCase):
	def setUp(self):
		self.computerPlayer = pytactoe.Player()
		self.humanPlayer = pytactoe.Player('X', "Player X", self.computerPlayer)
		self.computerPlayer = pytactoe.Player('O', "Player O", self.humanPlayer)
		self.board = pytactoe.Board()
		self.board.makeMove(self.board, 0, self.computerPlayer.getSymbol())
		self.board.makeMove(self.board, 4, self.computerPlayer.getSymbol())
		self.board.makeMove(self.board, 8, self.humanPlayer.getSymbol())
		self.board.makeMove(self.board, 5, self.humanPlayer.getSymbol())
		
	def computerPlayerBlockingMove_Test(self):
		#squareValues = [square.getDisplay() for square in self.board.board]
		#print(squareValues)
		#print(self.computerPlayer.requestMove(self.board))
		assert self.computerPlayer.requestMove(self.board) == 2
		
class ComputerPlayerWinningMove_Test(unittest.TestCase):
	def setUp(self):
		self.computerPlayer = pytactoe.Player()
		self.humanPlayer = pytactoe.Player('X', "Player X", self.computerPlayer)
		self.computerPlayer = pytactoe.Player('O', "Player O", self.humanPlayer)
		self.board = pytactoe.Board()
		self.board.makeMove(self.board, 0, self.humanPlayer.getSymbol())
		self.board.makeMove(self.board, 4, self.humanPlayer.getSymbol())
		self.board.makeMove(self.board, 8, self.computerPlayer.getSymbol())
		self.board.makeMove(self.board, 5, self.computerPlayer.getSymbol())
		
	def computerPlayerWinningMove_Test(self):
		#squareValues = [square.getDisplay() for square in self.board.board]
		#print(squareValues)
		#print(self.computerPlayer.requestMove(self.board))
		assert self.computerPlayer.requestMove(self.board) == 2	
			
def suite():
	suite = unittest.TestSuite()
	suite.addTest(Board_Test("draw_Test"))
	suite.addTest(BoardTestCase("winForX_Test"))
	suite.addTest(BoardTestCase("winForO_Test"))
	suite.addTest(ComputerPlayerBlockingMove_Test("computerPlayerBlockingMove_Test"))
	suite.addTest(ComputerPlayerWinningMoveTestCase("computerPlayerWinningMove_Test"))
	return suite

if __name__ == '__main__':
	runner = unittest.TextTestRunner()
	runner.run(suite())
import unittest
import pytactoe

class BoardTestCase(unittest.TestCase):
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
	
	def testDraw(self):
		result = self.nonWinningBoard.checkForWinner(self.nonWinningBoard, self.playerX)
		assert result == 0
	
	def testWinForX(self):
		result = self.winningBoardForX.checkForWinner(self.winningBoardForX, self.playerX)
		assert result == 1
		
	def testWinForO(self):
		result = self.winningBoardForO.checkForWinner(self.winningBoardForO, self.playerX)
		assert result == -1
		
class ComputerPlayerBlockingMoveTestCase(unittest.TestCase):
	def setUp(self):
		self.computerPlayer = pytactoe.Player()
		self.humanPlayer = pytactoe.Player('X', "Player X", self.computerPlayer)
		self.computerPlayer = pytactoe.Player('O', "Player O", self.humanPlayer)
		self.board = pytactoe.Board()
		self.board.makeMove(self.board, 0, self.computerPlayer.getSymbol())
		self.board.makeMove(self.board, 4, self.humanPlayer.getSymbol())
		self.board.makeMove(self.board, 1, self.computerPlayer.getSymbol())
		self.board.makeMove(self.board, 2, self.humanPlayer.getSymbol())
		
	def testComputerPlayerBlockingMove(self):
		assert self.computerPlayer.requestMove(self.board) == 6
		
class ComputerPlayerWinningMoveTestCase(unittest.TestCase):
	def setUp(self):
		self.computerPlayer = pytactoe.Player()
		self.humanPlayer = pytactoe.Player('X', "Player X", self.computerPlayer)
		self.computerPlayer = pytactoe.Player('O', "Player O", self.humanPlayer)
		self.board = pytactoe.Board()
		self.board.makeMove(self.board, 0, self.computerPlayer.getSymbol())
		self.board.makeMove(self.board, 4, self.humanPlayer.getSymbol())
		self.board.makeMove(self.board, 1, self.computerPlayer.getSymbol())
		self.board.makeMove(self.board, 3, self.humanPlayer.getSymbol())
		
	def testComputerPlayerWinningMove(self):
		assert self.computerPlayer.requestMove(self.board) == 2
			
def suite():
	suite = unittest.TestSuite()
	suite.addTest(BoardTestCase("testDraw"))
	suite.addTest(BoardTestCase("testWinForX"))
	suite.addTest(BoardTestCase("testWinForO"))
	suite.addTest(ComputerPlayerBlockingMoveTestCase("testComputerPlayerBlockingMove"))
	suite.addTest(ComputerPlayerWinningMoveTestCase("testComputerPlayerWinningMove"))
	return suite

runner = unittest.TextTestRunner()
runner.run(suite())
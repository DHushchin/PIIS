import chess

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QWidget, QApplication

from agents import *
from heuristic import Heuristic


class MainWindow(QWidget):
    """
    Create a surface for the chessboard.
    """
    def __init__(self):
        """
        Initialize the chessboard.
        """
        super().__init__()

        self.setWindowTitle("Chess GUI")
        self.setGeometry(600, 100, 700, 700)

        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(0, 0, 700, 700)

        self.boardSize = min(self.widgetSvg.width(),
                             self.widgetSvg.height())
        self.coordinates = True
        self.margin = 0.05 * self.boardSize if self.coordinates else 0
        self.squareSize = (self.boardSize - 2 * self.margin) / 8.0
        self.pieceToMove = [None, None]

        self.board = chess.Board()
        self.drawBoard()
        
        self.res_printed = False
        self.is_user_move = True
      
        
    def check_state(self):
        """
        Check the state of the game.
        """
        if self.res_printed:
            return
        
        if self.board.is_checkmate():
            print("Checkmate!")
        elif self.board.is_check():
            print("Check!")
        elif self.board.is_stalemate():
            print("Stalemate!")
        
        
    def is_game_over(self):
        """
        Check if the game is over.
        """    
        if self.res_printed:
            return
        
        if self.board.is_game_over():
            print("Game over")
            self.res_printed = True
            if self.board.result() == "1-0":
                print("White wins")
            else:
                print("Black wins")
          

    @pyqtSlot(QWidget)
    def mousePressEvent(self, event):
        """
        Handle left mouse clicks and enable moving chess pieces by
        clicking on a chess piece and then the target square.

        Moves must be made according to the rules of chess because
        illegal moves are suppressed.
        """
        if not self.is_user_move:
            return
        
        if event.x() <= self.boardSize and event.y() <= self.boardSize:
            if event.buttons() == Qt.LeftButton:
                if self.margin < event.x() < self.boardSize - self.margin and \
                   self.margin < event.y() < self.boardSize - self.margin:
                    file = int((event.x() - self.margin) / self.squareSize)
                    rank = 7 - int((event.y() - self.margin) / self.squareSize)
                    square = chess.square(file, rank)
                    piece = self.board.piece_at(square)
                    coordinates = "{}{}".format(chr(file + 97), str(rank + 1))
                    if self.pieceToMove[0] is not None:
                        try:
                            move = chess.Move.from_uci("{}{}".format(self.pieceToMove[1], coordinates))
                            if move in self.board.legal_moves:
                                self.board.push(move)
                                
                                self.drawBoard()
                                self.check_state()
                                self.is_game_over()
                                
                                
                                QApplication.processEvents()
                                self.makeAgentMove()

                                self.drawBoard()
                                self.check_state()
                                self.is_game_over()
                                
                            piece = None
                            coordinates = None
                        except:
                            pass
                                              
                    self.pieceToMove = [piece, coordinates]                 

    def drawBoard(self):
        """
        Draw a chessboard with the starting position and then redraw
        it for every new move.
        """
        self.boardSvg = self.board._repr_svg_().encode("UTF-8")
        self.drawBoardSvg = self.widgetSvg.load(self.boardSvg)

        return self.drawBoardSvg
    
    
    def makeAgentMove(self):
        self.is_user_move = False    
        heuristic = Heuristic(self.board, self.board.turn)
        # agent = NegamaxAgent(self.board, 3, heuristic)
        # agent = NegaScoutAgent(self.board, 3, heuristic)
        agent = PvsAgent(self.board, 3, heuristic)
        
        move = agent.get_move()
        print(move, '\n')
        self.board.push(move)
        self.drawBoard()
        self.is_user_move = True

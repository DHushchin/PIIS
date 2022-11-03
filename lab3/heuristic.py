import chess


class Heuristic:
    def __init__(self, board, color):
        self.board = board
        self.color = color

    def _get_balance(self):
        white = self.board.occupied_co[chess.WHITE]
        black = self.board.occupied_co[chess.BLACK]
        
        pawns = chess.popcount(white & self.board.pawns) \
                - chess.popcount(black & self.board.pawns)
                
        knights = chess.popcount(white & self.board.knights) \
                  - chess.popcount(black & self.board.knights)
                  
        bishops = chess.popcount(white & self.board.bishops) \
                  - chess.popcount(black & self.board.bishops)
                  
        rooks = chess.popcount(white & self.board.rooks) \
                - chess.popcount(black & self.board.rooks)
                
        queens = chess.popcount(white & self.board.queens) \
                 - chess.popcount(black & self.board.queens)
                 
        kings = chess.popcount(white & self.board.kings) \
                - chess.popcount(black & self.board.kings)

        return pawns * 1 + knights * 3 + bishops * 3 + rooks * 5 + queens * 9 + kings * 100
    
    def evaluate(self):
        white = self.board.occupied_co[chess.WHITE]
        black = self.board.occupied_co[chess.BLACK]
        score = self._get_balance() * (white - black)

        if (self.board.turn == self.color):
            return score

        return -score

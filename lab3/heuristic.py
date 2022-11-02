import chess

class Heuristic:
    def __init__(self, board, color):
        self.board = board
        self.color = color
        
    def evaluate(self):
        score = 0
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece is not None:
                if piece.color == self.color:
                    score += self.getPieceValue(piece)
                else:
                    score -= self.getPieceValue(piece)
        return score
    
    
    def getPieceValue(self, piece):
        if piece.piece_type == chess.PAWN:
            return 1
        elif piece.piece_type == chess.KNIGHT:
            return 3
        elif piece.piece_type == chess.BISHOP:
            return 3
        elif piece.piece_type == chess.ROOK:
            return 5
        elif piece.piece_type == chess.QUEEN:
            return 9
        elif piece.piece_type == chess.KING:
            return 100
        else:
            return 0
        
         
    def __str__(self):
        return "Heuristic"

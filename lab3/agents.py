class NegamaxAgent():
    def __init__(self, board, color, depth, heuristic):
        self.board = board
        self.color = color
        self.depth = depth
        self.heuristic = heuristic
        
    def get_move(self):
        return self.negamax(self.board, self.depth, -100000, 100000, self.color)
    
    def negamax(self, board, depth, alpha, beta, color):
        if depth == 0:
            return color * self.heuristic.evaluate()

        max_score = float('-inf')
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            score = -self.negamax(board, depth - 1, -beta, -alpha, -color)
            board.pop()

            if score > max_score:
                max_score = score
                best_move = move

            if score > alpha:
                alpha = score

            if alpha >= beta:
                break

        if depth == self.depth:
            return best_move

        return max_score
    
    
class NegaScoutAgent():
    def __init__(self, board, color, depth, heuristic):
        self.board = board
        self.color = color
        self.depth = depth
        self.heuristic = heuristic
        
    def get_move(self):
        return self.negascout(self.board, self.depth, -100000, 100000, self.color)
    
    def negascout(self, board, depth, alpha, beta, color):
        if depth == 0:
            return color * self.heuristic.evaluate()

        best_move = None
        for move in board.legal_moves:
            board.push(move)
            score = -self.negascout(board, depth - 1, -beta, -alpha, -color)
            board.pop()

            if score > alpha:
                if score >= beta:
                    return score
                alpha = score
                best_move = move

        if depth == self.depth:
            return best_move

        return alpha


class PvsAgent:
    def __init__(self, board, color, depth, heuristic):
        self.board = board
        self.color = color
        self.depth = depth
        self.heuristic = heuristic
        
    def get_move(self):
        return self.pvs(self.board, self.depth, -100000, 100000, self.color)
    
    def pvs(self, board, depth, alpha, beta, color):
        if depth == 0:
            return color * self.heuristic.evaluate()

        best_move = None
        for move in board.legal_moves:
            board.push(move)
            if best_move is None:
                score = -self.pvs(board, depth - 1, -beta, -alpha, -color)
            else:
                score = -self.pvs(board, depth - 1, -alpha - 1, -alpha, -color)
                if alpha < score < beta:
                    score = -self.pvs(board, depth - 1, -beta, -score, -color)
            board.pop()

            if score > alpha:
                alpha = score
                best_move = move

            if alpha >= beta:
                break

        if depth == self.depth:
            return best_move

        return alpha

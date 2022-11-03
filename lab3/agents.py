class NegamaxAgent():
    def __init__(self, board, depth, heuristic):
        self.board = board
        self.depth = depth
        self.heuristic = heuristic
        
    def get_move(self):
        print("Thinking...")
        return self.negamax(self.depth)[1]
    
    def negamax(self, depth):
        if (depth == 0):
            score = self.heuristic.evaluate()
            return score, None

        best_score = float('-inf')
        best_move = None
        for move in self.board.legal_moves:
            self.board.push(move)
            score = -1 * (self.negamax(depth - 1)[0])
            if score > best_score:
                best_score = score
                best_move = move
                
            self.board.pop()
            
        return best_score, best_move
    
    
class NegaScoutAgent():
    def __init__(self, board, depth, heuristic):
        self.board = board
        self.depth = depth
        self.heuristic = heuristic
        
    def get_move(self):
        print("Thinking...")
        return self.negascout(self.depth, -100000, 100000)[1]
    
    def negascout(self, depth, alpha, beta):
        best_score = float('-inf')
        best_move = None
        
        if (depth == 0):
            return self.heuristic.evaluate(), None

        for move in self.board.legal_moves:
            self.board.push(move)
            score = -1 * (self.max_score(depth - 1, alpha, beta))
            self.board.pop()

            if score > best_score:
                best_score = score
                best_move = move

        return best_score, best_move


    def max_score(self, depth, alpha, beta) -> int:
        if (depth == 0):
            return self.heuristic.evaluate()
        
        i = 1
        for move in self.board.legal_moves:
            self.board.push(move)
            score = -1 * (self.negascout(depth - 1, -beta, -alpha)[0])
            self.board.pop()
            
            if score > alpha and score < beta and i > 1 and depth < self.depth - 1:
                alpha = -1 * (self.negascout(depth - 1, -beta, -score)[0])
                
            alpha = max(alpha, score)
            
            if alpha >= beta:
                return alpha
            
            beta = alpha + 1
            i += 1
            
        return alpha


class PvsAgent:
    def __init__(self, board, depth, heuristic):
        self.board = board
        self.depth = depth
        self.heuristic = heuristic
        
    def get_move(self):
        print("Thinking...")
        return self.pvs(self.depth, -100000, 100000)[1]
    
    
    def pvs(self, depth, alpha, beta):
        best_score = float('-inf')
        best_move = None
        
        if (depth == 0):
            return self.heuristic.evaluate(), None

        for move in self.board.legal_moves:
            self.board.push(move)
            score = -1 * (self.get_score(depth - 1, alpha, beta))
            self.board.pop()

            if score > best_score:
                best_score = score
                best_move = move

        return best_score, best_move

    def get_score(self, depth, alpha, beta):
        if depth == 0:
            return self.heuristic.evaluate()
        
        search = True
        for move in self.board.legal_moves:
            self.board.push(move)
            
            if search:
                score = -1 * (self.pvs(depth - 1, -beta, -alpha)[0])
            else:
                score = -1 * (self.pvs(depth - 1, -alpha - 1, -alpha)[0])
                if score > alpha and score < beta:
                    score = -1 * (self.pvs(depth - 1, -beta, -alpha)[0])
                    
            self.board.pop()
            
            if score >= beta:
                return beta
            
            if score > alpha:
                alpha = score
                search = False
                
        return alpha

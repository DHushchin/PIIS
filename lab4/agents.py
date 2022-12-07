from math import log, sqrt, e, inf

import random
import chess


class Node:
    def __init__(self):
        self.state = chess.Board()
        self.children = set()
        self.parent = None
        self.child_visits = 0
        self.parent_visits = 0
        self.score = 0


class MCTSAgent:
    def __init__(self, board, color, depth):
        self.board = board
        self.color = color
        self.depth = depth
      
        
    def get_move(self):
        print("MCTS agent is thinking...")
        current = Node()
        current.state = self.board
        possible_moves = self.init_children(current)

        for _ in range(self.depth):
            best_child = self.select(current)
            expanded_child = self.expand(best_child)
            reward, state = self.simulate(expanded_child)
            current = self.backpropagation(state, reward)

        return self.select_move(current, possible_moves)
        
        
    def ucb(self, current):
        return current.score + \
               2 * (sqrt(log(current.parent_visits + e + (10**-8)) \
               / (current.child_visits + (10**-10))))


    def select(self, current):
        best_child = None
        max_ucb = -inf
        for node in current.children:
            node_ucb = self.ucb(node)
            if node_ucb > max_ucb:
                max_ucb = node_ucb
                best_child = node

        return best_child


    def expand(self, current):
        if len(current.children) == 0:
            return current

        return self.select(current)


    def simulate(self, current):
        if current.state.is_game_over():
            if current.state.result() == '1-0':
                return -1, current
            
            if current.state.result() == '0-1':
                return 1, current
            
            return 0.5, current

        possible_moves = [current.state.san(i) for i in list(current.state.legal_moves)]

        for move in possible_moves:
            temp_state = chess.Board(current.state.fen())
            temp_state.push_san(move)
            child = Node()
            child.state = temp_state
            child.parent = current
            current.children.add(child)
            
        rand_state = random.choice(list(current.children))

        return self.simulate(rand_state)


    def backpropagation(self, current, reward):
        current.child_visits += 1
        while current.parent is not None:
            current.parent_visits += 1
            current = current.parent
        current.score += reward
        return current


    def init_children(self, current):
        possible_moves = dict()
        
        for move in list(current.state.legal_moves):
            temp_state = chess.Board(current.state.fen())
            temp_state.push_san(current.state.san(move))

            res = Node()
            res.state = temp_state
            res.parent = current
            
            current.children.add(res)
            possible_moves[res] = move
            
        return possible_moves


    def select_move(self, current, states_moves):
        selected_move = None
        max_ucb = -inf
        
        for i in current.children:
            ucb_i = self.ucb(i)
            if ucb_i > max_ucb:
                max_ucb = ucb_i
                selected_move = states_moves[i]

        return selected_move

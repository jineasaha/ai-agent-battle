import random
from search import SearchCount, minimax, opposite

class ComputerPlayer:
    def __init__(self, label, lookahead, evaluator):
        self.label = label
        self.lookahead = lookahead
        self.evaluator = evaluator

    def move(self, board, mark):
        tally = SearchCount()
        top_score = float("-inf")
        finalists = []
        for square in board.legal_moves():
            board.cells[square] = mark
            value = minimax(board, opposite(mark), mark, self.lookahead - 1,
                            float("-inf"), float("inf"), self.evaluator, tally)
            board.cells[square] = ""
            if value > top_score:
                top_score, finalists = value, [square]
            elif value == top_score:
                finalists.append(square)
        return random.choice(finalists), tally

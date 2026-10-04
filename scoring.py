from board import Board

def line_value(board, mark, threat_weight, single_weight):
    rival = "O" if mark == "X" else "X"
    score = 0
    for triple in Board.winning_triples:
        values = [board.cells[i] for i in triple]
        own, enemy = values.count(mark), values.count(rival)
        if enemy == 0:
            score += threat_weight if own == 2 else single_weight if own == 1 else 0
        if own == 0:
            score -= threat_weight if enemy == 2 else single_weight if enemy == 1 else 0
    return score

def score_nexus(board, mark):
    won = board.winner()
    if won:
        return 100 if won == mark else -100
    return line_value(board, mark, 13, 2)

def score_titan(board, mark):
    won = board.winner()
    if won:
        return 100 if won == mark else -100
    score = line_value(board, mark, 10, 2)
    for square, value in ((4, 6), (0, 3), (2, 3), (6, 3), (8, 3)):
        if board.cells[square] == mark:
            score += value
        elif board.cells[square] and board.cells[square] != mark:
            score -= value
    return score

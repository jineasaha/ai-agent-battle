from dataclasses import dataclass

@dataclass
class SearchCount:
    visited: int = 0
    cutoffs: int = 0

def opposite(mark):
    return "O" if mark == "X" else "X"

def minimax(position, turn, root_mark, remaining, low, high, evaluator, count):
    count.visited += 1
    result = position.winner()
    if result:
        return (100 + remaining) if result == root_mark else (-100 - remaining)
    moves = position.legal_moves()
    if not moves:
        return 0
    if remaining == 0:
        return evaluator(position, root_mark)

    maximizing = turn == root_mark
    best = float("-inf") if maximizing else float("inf")
    for offset, square in enumerate(moves):
        position.cells[square] = turn
        value = minimax(position, opposite(turn), root_mark, remaining - 1, low, high, evaluator, count)
        position.cells[square] = ""
        if maximizing:
            best = max(best, value)
            low = max(low, best)
        else:
            best = min(best, value)
            high = min(high, best)
        if low >= high:
            count.cutoffs += len(moves) - offset - 1
            break
    return best

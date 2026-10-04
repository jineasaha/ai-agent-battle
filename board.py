class Board:
    winning_triples = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

    def __init__(self, cells=None):
        self.cells = list(cells) if cells is not None else [""] * 9

    def legal_moves(self):
        return [i for i, cell in enumerate(self.cells) if not cell]

    def place(self, index, mark):
        if index not in self.legal_moves():
            raise ValueError("That square is not available.")
        self.cells[index] = mark

    def winner(self):
        for a, b, c in self.winning_triples:
            if self.cells[a] and self.cells[a] == self.cells[b] == self.cells[c]:
                return self.cells[a]
        return None

    def finished(self):
        return self.winner() is not None or not self.legal_moves()

    def render(self):
        shown = [value if value else str(i + 1) for i, value in enumerate(self.cells)]
        for start in (0, 3, 6):
            print(" " + " | ".join(shown[start:start+3]))
            if start < 6:
                print("---+---+---")

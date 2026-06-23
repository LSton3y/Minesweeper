import src.constants

class Cell:

    def __init__(self, row: int, col: int):
        # Coordinates
        self.row = row
        self.col = col

        # Mine attributes
        self.mine = False
        self.adjacent_mines = 0

        # State attribute
        self.state = src.constants.CellState.HIDDEN
    

    def reveal(self):
        if self.mine:
            self.state = src.constants.CellState.MINE
        elif self.state != src.constants.CellState.FLAGGED:
            self.state = src.constants.CellState.REVEALED
        
    

    def flag(self):
        if self.state == src.constants.CellState.HIDDEN: 
            self.state = src.constants.CellState.FLAGGED
        elif self.state == src.constants.CellState.FLAGGED:
            self.state = src.constants.CellState.HIDDEN
import random
from itertools import product
from src.cell import Cell


class Grid:
    def __init__(self, rows, cols, mines):
        self.rows, self.cols = rows, cols
        self.mines = mines
        self.grid = self.generate_grid()


    def neighbours(self, row, col, neighbour_cells=[-1, 0, 1]):
        # Gets all the cells in a 3x3 grid around a cell
        for r_offset, c_offset in product(neighbour_cells, repeat=2):
            if r_offset == 0 and c_offset == 0:
                continue
            r, c = row + r_offset, col + c_offset
            if 0 <= r < self.rows and 0 <= c < self.cols:
                yield r, c


    def _count_adjacent_mines(self, grid, row, col) -> int:
         return sum(1 for r, c in self.neighbours(row, col) if grid[r][c].mine)


    def generate_grid(self):
        # Generate empty grid of cells
        grid = [[Cell(r, c) for c in range(self.cols)] for r in range(self.rows)]

        # Safely pick unique positions for mines using random.sample
        total_squares = self.rows * self.cols
        mine_count = min(self.mines, total_squares)  # Prevents infinite loop

        # Get 1D indices and convert them to 2D row/col coordinates
        mine_indices = random.sample(range(total_squares), mine_count)
        for index in mine_indices:
            r = index // self.cols
            c = index % self.cols
            grid[r][c].mine = self.mines

        # Change non mine squares numbers
        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c].mine:
                    continue

                grid[r][c].adjacent_mines = self._count_adjacent_mines(grid, r, c)
        
        return grid


    def get_cells(self):
        # Returns all the cells in the grid
        return [cell for row in self.grid for cell in row]


    def reveal_square(self, row, col, checked=None, reveal_mines=True):
        # Avoids recursion depth from exceeding by preventing same empty cells from being checked again
        if checked is None:
            checked = set()

        # Reveals cells
        if self.grid[row][col].mine:
            if reveal_mines:
                self.grid[row][col].reveal()
        else:
            self.grid[row][col].reveal()

        # If cell is empty, reveal all squares around it
        if not self.grid[row][col].mine and self.grid[row][col].adjacent_mines == 0:
            for r, c in self.neighbours(row, col):
                if (r, c) not in checked:
                    checked.add((r, c))
                    self.reveal_square(r, c, checked)
        
        return self.grid[row][col].mine
import pygame

import src.assets
import src.constants
import src.grid


class Game:

    def __init__(self, surface: pygame.Surface):
        # Game settings
        self.rows = 16
        self.columns = 16
        self.mines = 40

        self._start_click_size = 1

        # Class references
        self.surface = surface
        self.grid = src.grid.Grid(self.rows, self.columns, self.mines)

        # Images
        self._tile_size = min(src.constants.WIDTH, src.constants.HEIGHT) // self.rows
        self._images = src.assets.load_images((self._tile_size, self._tile_size))

        # Game conditions
        self._started = False
        self._playing = True


    def _get_cell_from_mouse(self, mouse_x, mouse_y) -> tuple:
        # Get coordinates of the mouse
        row = mouse_y // self._tile_size
        col = mouse_x // self._tile_size

        # Clamp values
        if row >= self.grid.rows: row = self.grid.rows - 1
        elif row < 0: row = 0

        if col >= self.grid.cols: col = self.grid.cols - 1
        elif col < 0: col = 0

        return row, col
    

    def _get_image_from_cell(self, cell):
        # Returns an image based on current cell state
        match cell.state:
            case src.constants.CellState.HIDDEN:
                return self._images["HIDDEN"]
            case src.constants.CellState.FLAGGED:
                return self._images["FLAGGED"]
            case src.constants.CellState.MINE:
                return self._images["EXPLODED"]
            case src.constants.CellState.REVEALED:
                return self._images["NUMBERS"][cell.adjacent_mines]
            case src.constants.CellState.REVEALED_MINE:
                return self._images["REVEALED_MINE"]
            case src.constants.CellState.CELL_NOT_MINE:
                return self._images["CELL_NOT_MINE"]

    

    def start_game(self):
        # Resets game
        self._started = False
        self.grid.grid = self.grid.generate_grid()
    

    def _win_game(self):
        pass


    def _lose_game(self):
        self._playing = False

        # Reveal cells
        self.grid.reveal_mines()
        self.grid.reveal_not_mines()

    
    def check_win(self):
        game_won = True

        for cell in self.grid.get_cells():
            # Checks if cell is not a mine and hidden, if so, game isn't won
            if not cell.mine and cell.state == src.constants.CellState.HIDDEN:
                game_won = False
                break
        
        if game_won:
            self._win_game()



    def draw_screen(self):
        # Draws each cell to screen
        for cell in self.grid.get_cells():
            self.surface.blit(
                self._get_image_from_cell(cell), ( 
                cell.col * self._tile_size,
                cell.row * self._tile_size
            ))


    def handle_click(self, mouse_button, mouse_x, mouse_y):
        if not self._playing: return

        row, col = self._get_cell_from_mouse(mouse_x, mouse_y)
        
        if mouse_button == 1:
            # If first click, clear squares based on _start_click_size
            if not self._started:
                self.grid.reveal_square(row, col, reveal_mines=False) # Reveals clicked square if not mine

                for r, c in self.grid.neighbours(row, col, [i for i in range(-self._start_click_size, self._start_click_size + 1)]):
                    self.grid.reveal_square(r, c, reveal_mines=False)
                
                self._started = True
            
            else:
                # Reveals clicked square regardless if it is a mine
                if self.grid.reveal_square(row, col):
                    self._lose_game() # Lose game if it is a mine

        elif mouse_button == 3:
            self.grid.grid[row][col].flag()
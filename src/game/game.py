import pygame

import src.utils.asset_manager
import src.constants
import src.game.grid


class Game:

    def __init__(self):
        # Game settings
        self.rows = 16
        self.columns = 16
        self.mines = 40

        self._start_click_size = 1

        # Class references
        self.grid = src.game.grid.Grid(self.rows, self.columns, self.mines)

        # Images
        self._min_size = min(src.constants.WIDTH, src.constants.HEIGHT)
        self._tile_size = self._min_size // self.rows
        self._cell_images = src.utils.asset_manager.load_cells((self._tile_size, self._tile_size))
        

        # Game state
        self.state = src.constants.GameState.PLAYING
        self._started = False


    def get_cell_from_mouse(self, mouse_x, mouse_y) -> tuple:
        # Get coordinates of the mouse
        row = (mouse_y - src.constants.TOP_BAR_HEIGHT) // self._tile_size
        col = mouse_x // self._tile_size

        # Return early if outside grid
        if row < 0 or row >= self.rows:
            return (None, None)
        if col < 0 or col >= self.columns:
            return (None, None)

        return row, col
    

    def _get_image_from_cell(self, cell):
        # Returns an image based on current cell state
        match cell.state:
            case src.constants.CellState.HIDDEN:
                return self._cell_images["HIDDEN"]
            case src.constants.CellState.FLAGGED:
                return self._cell_images["FLAGGED"]
            case src.constants.CellState.MINE:
                return self._cell_images["EXPLODED"]
            case src.constants.CellState.REVEALED:
                return self._cell_images["NUMBERS"][cell.adjacent_mines]
            case src.constants.CellState.REVEALED_MINE:
                return self._cell_images["REVEALED_MINE"]
            case src.constants.CellState.CELL_NOT_MINE:
                return self._cell_images["CELL_NOT_MINE"]

    

    def reset_game(self):
        # Resets game
        self.state = src.constants.GameState.PLAYING
        self._started = False
        self.grid.grid = self.grid.generate_grid()
    

    def _win_game(self):
        self.state = src.constants.GameState.WON


    def _lose_game(self):
        self.state = src.constants.GameState.LOST

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



    def draw_screen(self, surface: pygame.Surface):
        # Draws each cell to centered to the bottom - allows room for UI at top
        for cell in self.grid.get_cells():
            surface.blit(
                self._get_image_from_cell(cell), ( 
                cell.col * self._tile_size,
                cell.row * self._tile_size + src.constants.TOP_BAR_HEIGHT
            ))


    def handle_click(self, mouse_button, mouse_x, mouse_y):
        if not self.state == src.constants.GameState.PLAYING: return

        row, col = self.get_cell_from_mouse(mouse_x, mouse_y) # Get row and col of mouse

        # Return early if not in grid area
        if row is None or col is None:
            return
        
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
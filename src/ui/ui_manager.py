import pygame

from src.ui.reset_button import ResetButton
from src.ui.label import Label
from src.utils.asset_manager import load_faces
from src import constants
from src.game.game import Game


class UIManager:
    
    def __init__(self):
        # Class references
        self.reset_button = ResetButton()

        self.font = pygame.font.Font(constants.SEVEN_SEGMENT_FONT, 70)
    
        self.flags_left_text = self._create_counter_label((110, 10))
        self.timer_text = self._create_counter_label((430, 10))

        self.panel_rect = pygame.Rect(0, 0, constants.WIDTH, constants.TOP_BAR_HEIGHT)

        self.face_images = load_faces((
            self.reset_button.rect.width,
            self.reset_button.rect.height
        ))

        self._mouse_down = False # Used to control shocked face when clicking



    # Creates counter label with default font and color
    def _create_counter_label(self, position) -> Label:
        return Label(
            "0",
            position,
            self.font,
            constants.RED
        )    


    # Returns the reset button image based on current game state
    def _get_button_image_from_game_state(self, game_state: constants.GameState):
        if self._mouse_down:
            return self.face_images["SHOCKED"]

        match game_state:
            case constants.GameState.PLAYING:
                return self.face_images["SMILE"]
            case constants.GameState.WON:
                return self.face_images["SUNGLASSES"]
            case constants.GameState.LOST:
                return self.face_images["DEAD"]


    def draw_ui(self, surface: pygame.Surface, game: Game):
        # Draw panel
        pygame.draw.rect(surface, constants.GREY, self.panel_rect)
        # Draw the outline 
        pygame.draw.rect(surface, constants.LIGHTGREY, self.panel_rect, width=3)

        # Draws reset button
        surface.blit(self._get_button_image_from_game_state(game.state), self.reset_button.rect)

        # Draw the amount of flags left
        self.flags_left_text.text = str(game.grid.flags)
        self.flags_left_text.draw(surface)

        # Draw the timer
        self.timer_text.text = str(game.game_timer // constants.FPS)
        self.timer_text.draw(surface)

    

    def handle_click(self, game: Game, mouse_x: int, mouse_y: int):
        # Checks if reset button clicked, if so, reset game
        if self.reset_button.clicked((mouse_x, mouse_y)):
            game.reset_game()
        
        cell, cell = game.get_cell_from_mouse(mouse_x, mouse_y) # Keep "cell, cell" to unpack None tuple
        if cell is not None and game.state == constants.GameState.PLAYING:
            self._mouse_down = True
    

    def handle_click_release(self):
        self._mouse_down = False

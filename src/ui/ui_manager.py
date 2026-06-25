import pygame

import src.ui.reset_button
import src.ui.label

import src.constants
import src.utils.asset_manager


class UIManager:
    
    def __init__(self):
        # Class references
        self.reset_button = src.ui.reset_button.ResetButton()

        self.flags_left_text = src.ui.label.Label(
            "0", 
            (110, 10), 
            pygame.font.Font(src.constants.SEVEN_SEGMENT_FONT, 70),
            (255, 0, 0)
        )

        self.timer_text = src.ui.label.Label(
            "0", 
            (430, 10), 
            pygame.font.Font(src.constants.SEVEN_SEGMENT_FONT, 70),
            (255, 0, 0)
        )

        self.panel_rect = pygame.Rect(0, 0, src.constants.WIDTH, src.constants.TOP_BAR_HEIGHT)

        self.face_images = src.utils.asset_manager.load_faces((
            self.reset_button.rect.width,
            self.reset_button.rect.height
        ))

        self._mouse_down = False # Used to control shocked face when clicking
        


    # Returns the reset button image based on current game state
    def _get_button_image_from_game_state(self, game_state: src.constants.GameState):
        if self._mouse_down:
            return self.face_images["SHOCKED"]

        match game_state:
            case src.constants.GameState.PLAYING:
                return self.face_images["SMILE"]
            case src.constants.GameState.WON:
                return self.face_images["SUNGLASSES"]
            case src.constants.GameState.LOST:
                return self.face_images["DEAD"]


    def draw_ui(self, surface: pygame.Surface, game):
        # Draw panel
        pygame.draw.rect(surface, src.constants.GREY, self.panel_rect)
        # Draw the outline 
        pygame.draw.rect(surface, src.constants.LIGHTGREY, self.panel_rect, width=3)

        # Draws reset button
        surface.blit(self._get_button_image_from_game_state(game.state), self.reset_button.rect)

        # Draw the amount of flags left
        self.flags_left_text.text = str(game.grid.flags)
        self.flags_left_text.draw(surface)

        # Draw the timer
        self.timer_text.text = str(game.game_timer // src.constants.FPS)
        self.timer_text.draw(surface)

    

    def handle_click(self, game, mouse_x, mouse_y):
        # Checks if reset button clicked, if so, reset game
        if self.reset_button.clicked((mouse_x, mouse_y)):
            game.reset_game()
        
        if game.get_cell_from_mouse(mouse_x, mouse_y) != (None, None) \
        and game.state == src.constants.GameState.PLAYING:
            self._mouse_down = True
    

    def handle_click_release(self):
        self._mouse_down = False

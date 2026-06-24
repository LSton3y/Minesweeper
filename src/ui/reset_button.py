import pygame
import src.constants

class ResetButton:

    def __init__(self):
        # Creates rect
        self.rect = pygame.Rect(
            0,
            0,
            src.constants.TOP_BAR_HEIGHT // 2,
            src.constants.TOP_BAR_HEIGHT // 2
        )

        # Centers rect to top middle
        self.rect.centerx = src.constants.WIDTH // 2
        self.rect.top = src.constants.TOP_BAR_HEIGHT // 5
        

    def clicked(self, pos):
        return self.rect.collidepoint(pos)
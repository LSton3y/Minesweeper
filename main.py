import pygame

import src.game.game
import src.constants

class Main:

    def __init__(self):
        # Pygame initialisation
        pygame.init()
        self.clock = pygame.time.Clock()

        # Window initialisation
        self.surface = pygame.display.set_mode((src.constants.WIDTH, src.constants.HEIGHT))
        pygame.display.set_caption("Minesweeper")

        # Class initialisation
        self.game = src.game.game.Game(self.surface)

    # Handles input
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.game.handle_click(event.button, *event.pos)
    

    # Handles draw functions
    def _draw(self):
        self.surface.fill((255, 255, 255))
        self.game.draw_screen()
        pygame.display.flip()


    def main(self):
        # Main loop
        self.running = True
        while self.running:
            self.game.check_win()
            self._handle_events()
            self._draw()
            self.clock.tick(src.constants.FPS)
        
        pygame.quit()

                
if __name__ == "__main__":
    main = Main()
    main.main()

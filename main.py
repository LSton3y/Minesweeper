import pygame

import src.game.game
import src.constants
import src.ui.ui_manager

class Main:

    def __init__(self):
        # Pygame initialisation
        pygame.init()
        self.clock = pygame.time.Clock()

        # Window initialisation
        self.surface = pygame.display.set_mode((src.constants.WIDTH, src.constants.HEIGHT))
        pygame.display.set_caption("Minesweeper")

        # Class initialisation
        self.game = src.game.game.Game()
        self.ui = src.ui.ui_manager.UIManager()

    # Handles input
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.ui.handle_click(self.game, *event.pos)
            
            if event.type == pygame.MOUSEBUTTONUP:
                self.game.handle_click(event.button, *event.pos)

                if event.button == 1:
                    self.ui.handle_click_release()
                
    

    # Handles draw functions
    def _draw(self):
        self.surface.fill(src.constants.GREY)

        self.game.draw_screen(self.surface)
        self.ui.draw_ui(self.surface, self.game)

        pygame.display.flip()


    def main(self):
        # Main loop
        self.running = True
        while self.running:
            self.game.check_win()
            self._handle_events()
            self._draw()

            self.game.increment_timer()
            self.clock.tick(src.constants.FPS)
        
        pygame.quit()

                
if __name__ == "__main__":
    main = Main()
    main.main()

class Label:

    def __init__(self, text: str, pos: tuple, font, color=(255, 255, 255)):
        self.text = text
        self.pos = pos
        self.font = font
        self.color = color
    

    def draw(self, surface):
        text_surface = self.font.render(
            self.text,
            True,
            self.color
        )

        surface.blit(text_surface, self.pos)
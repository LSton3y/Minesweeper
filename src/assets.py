import pygame
import os
import src.constants

def load_images(tile_size: tuple) -> dict:
    def load(name):
        path = os.path.join(src.constants.IMAGES_PATH, name)
        return pygame.transform.scale(pygame.image.load(path).convert_alpha(), tile_size)

    return {
        "HIDDEN":   load("masked_tile.png"),
        "FLAGGED":     load("masked_tile_flag_blue.png"),
        "EXPLODED": load("tile_exploded.png"),
        "NUMBERS":  [load(f"revealed_tile_{i}.png") if i > 0 else load("revealed_tile.png") for i in range(9)],
    }
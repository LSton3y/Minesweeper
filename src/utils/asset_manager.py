import pygame
import os
import src.constants


def load_cells(cell_size: tuple) -> dict:
    def load(name):
        path = os.path.join(src.constants.CELL_IMAGES_PATH, name)
        return pygame.transform.scale(pygame.image.load(path).convert_alpha(), cell_size)

    return {
        "HIDDEN": load("masked_tile.png"),
        "FLAGGED": load("masked_tile_flag_blue.png"),
        "EXPLODED": load("tile_exploded.png"),
        "NUMBERS": [load(f"revealed_tile_{i}.png") if i > 0 else load("revealed_tile.png") for i in range(9)],
        "REVEALED_MINE": load("revealed_tile_bomb.png"),
        "CELL_NOT_MINE": load("tile_not_mine.png")
    }


def load_faces(face_size: tuple) -> dict:
    def load(name):
        path = os.path.join(src.constants.FACE_IMAGES_PATH, name)
        return pygame.transform.scale(pygame.image.load(path).convert_alpha(), face_size)
    
    return {
        "SMILE": load("smile.png"),
        "DEAD": load("dead.png"),
        "SUNGLASSES": load("sunglasses.png"),
        "SHOCKED": load("shocked.png")
    }
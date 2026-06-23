import os
from enum import Enum, auto

# Constants
WIDTH, HEIGHT = 800, 800
FPS = 60


# Images
IMAGES_PATH = "assets/images"

MASKED_TILE = os.path.join(IMAGES_PATH, "masked_tile.png")
MASKED_TILE_FLAG = os.path.join(IMAGES_PATH, "masked_tile_flag_blue.png")
REVEALED_TILE = os.path.join(IMAGES_PATH, "revealed_tile.png")
REVEALED_TILE_1 = os.path.join(IMAGES_PATH, "revealed_tile_1.png")
REVEALED_TILE_2 = os.path.join(IMAGES_PATH, "revealed_tile_2.png")
REVEALED_TILE_3 = os.path.join(IMAGES_PATH, "revealed_tile_3.png")
REVEALED_TILE_4 = os.path.join(IMAGES_PATH, "revealed_tile_4.png")
REVEALED_TILE_5 = os.path.join(IMAGES_PATH, "revealed_tile_5.png")
REVEALED_TILE_6 = os.path.join(IMAGES_PATH, "revealed_tile_6.png")
REVEALED_TILE_7 = os.path.join(IMAGES_PATH, "revealed_tile_7.png")
REVEALED_TILE_8 = os.path.join(IMAGES_PATH, "revealed_tile_8.png")
TILE_EXPLODED = os.path.join(IMAGES_PATH, "tile_exploded.png")


# Cell states
class CellState(Enum):
    HIDDEN = auto()
    FLAGGED = auto()
    REVEALED = auto()
    MINE = auto()
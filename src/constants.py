import os
from enum import Enum, auto

# Constants
WIDTH, HEIGHT = 800, 800
FPS = 60


# Cell states
class CellState(Enum):
    HIDDEN = auto()
    FLAGGED = auto()
    REVEALED = auto()
    MINE = auto()
    REVEALED_MINE = auto()
    CELL_NOT_MINE = auto()


# Images path
IMAGES_PATH = "assets/images"
import os
from enum import Enum, auto

# Constants
WIDTH, HEIGHT = 608, 700
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
CELL_IMAGES_PATH = "assets/images/cells"
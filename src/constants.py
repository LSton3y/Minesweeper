import os
from enum import Enum, auto

# Constants
WIDTH, HEIGHT = 608, 700
TOP_BAR_HEIGHT = 92
FPS = 60


# Cell states
class CellState(Enum):
    HIDDEN = auto()
    FLAGGED = auto()
    REVEALED = auto()
    MINE = auto()
    REVEALED_MINE = auto()
    CELL_NOT_MINE = auto()


# Game states
class GameState(Enum):
    PLAYING = auto()
    WON = auto()
    LOST = auto()


# Images path
CELL_IMAGES_PATH = "assets/images/cells"
FACE_IMAGES_PATH = "assets/images/faces"


# Colors
GREY = (144, 164, 174)
LIGHTGREY = (213, 224, 230)
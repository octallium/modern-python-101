from enum import Enum, auto


class GameState(Enum):
    """Describes the state of game"""

    INITIALIZING = auto()
    IN_PROGRESS = auto()
    WIN = auto()
    LOST = auto()

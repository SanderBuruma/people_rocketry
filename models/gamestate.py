from enum import Enum
from models.vehicles.rocket import Rocket

class GameStateEnum(Enum):
  PLAY = 0
  PAUSE = 1
  GAMEOVER = 2

class GameState:
  def __init__(self, runmode: GameStateEnum = GameStateEnum.PLAY):
    self.runmode = runmode
    self.elapsed_time = 0
    self.rockets: list[Rocket] = []
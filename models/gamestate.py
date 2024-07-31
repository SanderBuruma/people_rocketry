

from models.vehicles.rocket import Rocket

class GameStateEnum:
  play = 0
  pause = 1
  gameover = 2

class GameState:
  def __init__(self, runmode: GameStateEnum = GameStateEnum.play):
    self.runmode = runmode
    self.elapsed_time = 0
    self.rockets: list[Rocket] = []
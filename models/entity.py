import copy

class Entity:
  def __init__(self, x, y, dx, dy):
    self.x = x
    self.y = y
    self.dx = dx
    self.dy = dy

  @property
  def copy(self): return copy.deepcopy(self)
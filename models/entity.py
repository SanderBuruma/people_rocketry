import copy

class Entity:
  def __init__(self, x, y, dx, dy):
    self.x = x
    self.y = y
    self.dx = dx
    self.dy = dy
  
  def update(self, dt):
    self.x += self.dx * dt
    self.y += self.dy * dt

  @property
  def copy(self): return copy.deepcopy(self)

class FuelType:
  def __init__(self, name: str, density: float):
    self.name = name
    self.density = density

  def __str__(self):
    return self.name
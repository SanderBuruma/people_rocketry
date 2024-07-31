import copy


class Engine:
  def __init__(self, name: str, thrust: float, mass: float, fuel_flow_rate: float):
    """
    :param thrust: The amount of thrust the engine produces, in kN
    :param mass: The mass of the engine, in tons
    :param fuel_flow_rate: The rate at which the engine consumes fuel, in tons per second
    """
    self.name = name
    self.thrust = thrust
    self.mass = mass
    self.fuel_flow_rate = fuel_flow_rate
  
  def __str__(self):
    return self.name
  
  @property
  def exhaust_velocity(self) -> float:
    """The amount of thrust per unit of fuel"""
    return self.thrust / self.fuel_flow_rate

  @property
  def copy(self): return copy.deepcopy(self)
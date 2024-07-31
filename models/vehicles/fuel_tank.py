import copy
from models.vehicles.fuel_type import FuelType


class FuelTank:
  def __init__(self, name: str, capacity: float, fuel_amount: float, dry_mass: float, fuel_type: FuelType):
    """
    :param capacity: The amount of fuel the tank can hold, in tons
    :param fuel: The type of fuel the tank holds
    :param dry_mass: The mass of the tank when empty, in tons
    """
    if fuel_amount > capacity: raise ValueError('Fuel amount cannot exceed capacity')
    self.capacity = capacity
    self.fuel_amount = fuel_amount
    self.fuel_type = fuel_type
    self.dry_mass = dry_mass
    self.name = name

  def __str__(self):
    return self.name

  @property
  def volume(self): return self.capacity * 1.05 / self.fuel_type.density

  @property
  def mass(self): return self.dry_mass + self.capacity

  @property
  def copy(self): return copy.deepcopy(self)
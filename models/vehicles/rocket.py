import math

from models.entity import Entity
from models.vehicles.engine import Engine
from models.vehicles.fuel_tank import FuelTank


class Rocket(Entity):
  def __init__(self, name: str, x: int, y: int, dx: int, dy: int, engines, fuel_tanks, dry_weight, payload):
    super().__init__(x, y, dx, dy)
    self.name = name
    self.payload: 'Rocket' = payload
    self.engines: list[Engine] = engines
    self.fuel_tanks: list[FuelTank] = fuel_tanks
    self.dry_mass: float = dry_weight

  def __str__(self):
    return self.name
  
  @property
  def dv(self):
    math.e ** self.thrust / self.fuel_consumption_rate + self.payload.dv if self.payload else 0
    
  @property
  def fuel_consumption_rate(self): return sum([engine.fuel_flow_rate for engine in self.engines])

  @property
  def burn_time(self): 
    """How long the engines will run given the current fuel amount and flowrate"""
    return self.fuel_amount / self.fuel_consumption_rate
  
  @property
  def thrust(self): return sum([engine.thrust for engine in self.engines])
  
  @property
  def fuel_amount(self): return sum([tank.fuel_amount for tank in self.fuel_tanks])

  @property
  def exhaust_velocity(self): return self.thrust / self.fuel_consumption_rate

  @property
  def mass(self): return self.dry_weight + sum([tank.mass for tank in self.fuel_tanks]) + sum([engine.mass for engine in self.engines]) + self.payload.mass if self.payload else 0
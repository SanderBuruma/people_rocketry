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
    self.structural_mass: float = dry_weight

  def __str__(self):
    return self.name
  
  def update(self, dt, thrusting: bool):
    super().update(dt) 

    if not thrusting:
      return
    
    active_fuel_tanks = [tank for tank in self.fuel_tanks if tank.fuel_amount > 0]
    total_capacity = sum(tank.capacity for tank in active_fuel_tanks)
    for fuel_tank in (active_fuel_tanks):
      fuel_tank.fuel_amount -= self.fuel_consumption_rate * dt * (fuel_tank.capacity/total_capacity)
  
  @property
  def dv(self): 
    return math.e ** (self.mass / self.dry_mass) * self.exhaust_velocity
    
  @property
  def fuel_consumption_rate(self): return sum(engine.fuel_flow_rate for engine in self.engines)

  @property
  def burn_time(self): 
    """How long the engines will run given the current fuel amount and flowrate"""
    return self.fuel_amount / self.fuel_consumption_rate
  
  @property
  def thrust(self): return sum(engine.thrust for engine in self.engines)
  
  @property
  def fuel_amount(self): return sum(tank.fuel_amount for tank in self.fuel_tanks)

  @property
  def exhaust_velocity(self): return self.thrust / self.fuel_consumption_rate

  @property
  def mass(self): 
    """The mass of the rocket, including fuel"""
    return self.structural_mass + sum(tank.mass for tank in self.fuel_tanks) + sum(engine.mass for engine in self.engines) + (self.payload.mass if self.payload else 0)
  @property
  def dry_mass(self): 
    """The mass of the rocket without fuel"""
    return self.structural_mass + sum(tank.dry_mass for tank in self.fuel_tanks) + sum(engine.mass for engine in self.engines) + (self.payload.mass if self.payload else 0)
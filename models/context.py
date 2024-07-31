
from models.vehicles.engine import Engine
from models.vehicles.fuel_tank import FuelTank
from models.vehicles.fuel_type import FuelType
from models.vehicles.rocket import Rocket


class Context:
  fuel_types: dict[str, FuelType] = {}
  fuel_tanks: dict[str, FuelTank] = {}
  engines_types: dict[str, Engine] = {}
  rockets: dict[str, Rocket] = {}
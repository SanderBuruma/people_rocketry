from models.vehicles.engine import Engine
from models.vehicles.fuel_type import FuelType
from models.vehicles.rocket import Rocket

class Context:
  rocket: Rocket
  fuel_types: dict[str, FuelType]
  engines: dict[str, Engine]


from features.context import Context
from models.vehicles.rocket import Rocket


def before_scenario(context: Context, scenario):
  context.fuel_types = {}
  context.engines = {}
from features.context import Context
from models.vehicles.rocket import Rocket
from models.vehicles.engine import Engine
from models.vehicles.fuel_tank import FuelTank
from models.vehicles.fuel_type import FuelType

from behave import given, when, then

@given('we have a Rocket with a structural mass of {structural_mass:f} tons')
def step(context: Context, structural_mass:float):
  context.rocket = Rocket('Test Rocket', 0, 0, 0, 0, [], [], structural_mass, None)

@given('there is a fuel type of {name} with density {density:f}t/m3')
def step(context: Context, name:str, density: float):
  if not context.fuel_types:
    context.fuel_types = {}
  
  context.fuel_types[name] = FuelType(name, density)

@given('{nr:d} {fuel_type} fuel tanks are added containing {amount:g} tons of {fuel_type} massing {dry_mass:f} tons dry')
@given('{nr:d} {fuel_type} fuel tank is added containing {amount:g} tons of {fuel_type} massing {dry_mass:f} tons dry')
def step(context: Context, nr: int, fuel_type: str, amount, dry_mass):
  if not context.fuel_types or not context.fuel_types.get(fuel_type, None):
    raise ValueError(f'Fuel type {fuel_type} not found')
  fuel_type = context.fuel_types[fuel_type]
  for _ in range(nr):
    context.rocket.fuel_tanks.append(FuelTank('{} Tank'.format(fuel_type), amount, amount, dry_mass, fuel_type))
  
  pass

@given('there is an engine called {name} massing {mass:f} tons, thrust {thrust:d}kN, fuel {fuel_type}, flow rate {flow_rate:f}t/s')
def step(context: Context, name: str, mass: float, thrust: int, fuel_type: str, flow_rate: float):
  if not context.fuel_types or not context.fuel_types.get(fuel_type, None):
    raise ValueError(f'Fuel type {fuel_type} not found')

  ft = context.fuel_types[fuel_type]
  context.engines[name] = Engine(name, thrust, mass, flow_rate, ft)

@given('{nr:d} {engine} engines are added to the rocket')
def step(context: Context, engine, nr:int):
  if not context.engines or not context.engines.get(engine, None):
    raise ValueError(f'Engine {engine} not found')

  for _ in range(nr):
    context.rocket.engines.append(context.engines[engine])

@then('the rocket masses {mass:f} tons')
@then('the rocket masses {mass:f} tons in total')
def step(context: Context, mass: float):

  assert abs(context.rocket.mass - mass) < .01

@then('the rocket has a thrust of {thrust:d}kN')
def step(context: Context, thrust: int):
  assert abs(context.rocket.thrust - thrust) < .01

@then('the rocket has dV of {dv:d}m/s^2')
def step(context: Context, dv: int):
  assert abs(context.rocket.dv - dv) < 10

@then('the rocket has a TWR of {twr:f}')
def step(context: Context, twr: float):
  assert abs(context.rocket.twr - twr) < .01
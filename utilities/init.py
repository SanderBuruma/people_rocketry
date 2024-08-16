
from models.vehicles.engine import Engine
from models.vehicles.fuel_tank import FuelTank
from models.vehicles.fuel_type import FuelType
from models.vehicles.rocket import Rocket

def rockets():
  fts = fuel_tanks()
  es = engines()
  rs = { }
  
  rs['Payload-1'] = Rocket(
    'Payload-1',
    0,0,0,0,
    [es['Terrier-20'], es['Terrier-20']],
    [fts['Hydrolox-1']],
    .1,
    None
  )
  rs['Launcher-1'] = Rocket(
    'Launcher-1',
    0,0,0,0,
    [es['Kicker-80'], es['Kicker-80']],
    [fts['Kerolox-8'].copy],
    .5,
    rs['Payload-1'].copy
  )

  return rs

def fuel_types():
  fuel_types = {}
  fuel_types['Kerolox'] = FuelType('Kerosene', 0.61)
  fuel_types['Hydrolox'] = FuelType('Hydrolox', .6)
  return fuel_types

def fuel_tanks():
  fts = fuel_types()
  fuel_tanks = {}

  fuel_tanks['Kerolox-1'] = FuelTank('Kerolox-1'  , 1, 1,.108, fts['Kerolox'])
  fuel_tanks['Kerolox-4'] = FuelTank('Kerolox-4'  , 4, 4,.4  , fts['Kerolox'])
  fuel_tanks['Kerolox-8'] = FuelTank('Kerolox-8'  , 8, 8,.78 , fts['Kerolox'])
  fuel_tanks['Hydrolox-D2']=FuelTank('Hydrolox-D2',.2,.2,.045, fts['Hydrolox'])
  fuel_tanks['Hydrolox-1'] =FuelTank('Hydrolox-1' , 1, 1,.2  , fts['Hydrolox'])
  fuel_tanks['Hydrolox-2'] =FuelTank('Hydrolox-2' , 2, 2,.38 , fts['Hydrolox'])

  return fuel_tanks

def engines():
  fts = fuel_types()
  engines = {}
  engines['Kicker-80'] = Engine('Kicker-80',80,.5,.02,fts['Kerolox'])
  engines['Terrier-20'] = Engine('Terrier-20',20,.1,.004,fts['Hydrolox'])
  return engines
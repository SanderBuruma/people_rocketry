
from behave import given,when,then
from features.context import Context
from utilities.init import rockets

@given('we start with rocket {rocket_name}')
def step(context: Context, rocket_name):
  context.rocket = rockets()[rocket_name]

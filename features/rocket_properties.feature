Feature: Rockets have db, mass, fuel thrust, exhaust velocity, etc
  Background:
    Given we have a Rocket with dry mass .8 tons
    And there is a fuel type kerosene with density .7t/m3
    And 1 kerosene fuel tank is added containing 2 tons of kerosene weighing 0.2 tons dry.
    And there is an engine called Kicker-1 weighing .8 tons, thrust 80kN, fuel kerosene
    And 2 Kicker-1 engines are added to this rocket
    Then the rocket has a mass over 4 tons
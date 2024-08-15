Feature: Rockets have db, mass, fuel thrust, exhaust velocity, etc
  Background:
    Given we have a Rocket with a structural mass of .8 tons
    And there is a fuel type of Kerosene with density .7t/m3
    And 1 Kerosene fuel tank is added containing 2.0 tons of kerosene massing 0.2 tons dry
    And there is an engine called Kicker-1 massing .1 tons, thrust 80kN, fuel Kerosene, flow rate 0.1t/s
    And 2 Kicker-1 engines are added to the rocket
  
  Scenario: x
    Then the rocket masses 3.2 tons in total
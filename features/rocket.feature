Feature: Rockets have db, mass, fuel thrust, exhaust velocity, etc
  Background:
    Given we have a Rocket with a structural mass of .8 tons
    And there is a fuel type of Kerosene with density .7t/m3
    And 1 Kerosene fuel tank is added containing 2.0 tons of kerosene massing 0.2 tons dry
    And there is an engine called Kicker-1 massing .5 tons, thrust 80kN, fuel Kerosene, flow rate 0.02t/s
    And 2 Kicker-1 engines are added to the rocket
  
  Scenario: rocket properties
    Then the rocket masses 4.0 tons in total
    Then the rocket has a thrust of 160kN
    Then the rocket has a TWR of 40.0
    Then the rocket has dV of over 2750m/s^2
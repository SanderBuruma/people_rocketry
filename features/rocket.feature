Feature: Rockets have db, mass, fuel thrust, exhaust velocity, etc
  Background:
    Given we have a Rocket with a structural mass of 1.8 tons
    And there is a fuel type of Kerosene with density .7t/m3
    And 1 Kerosene fuel tank is added containing 4.9 tons of kerosene massing 0.3 tons dry
    And there is an engine called Kicker-80 massing .5 tons, thrust 80kN, fuel Kerosene, flow rate 0.02t/s
    And 2 Kicker-80 engines are added to the rocket
  
  Scenario: rocket properties
    Then the rocket masses 8.0 tons in total
    Then the rocket has a thrust of 160kN
    Then the rocket has a TWR of 20.0
    Then the rocket has dV of 3750m/s^2
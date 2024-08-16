Feature: Rockets have db, mass, fuel thrust, exhaust velocity, etc
  Background:
    Given we start with rocket Launcher-1
  
  Scenario: rocket properties
    Then the rocket masses 11.78 tons in total
    And the rocket has a thrust of 160kN
    And the rocket has a TWR of 13.5823
    And the rocket has dV of 4540m/s^2
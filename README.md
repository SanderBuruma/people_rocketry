# People Rocketry
A quixotical rocketry game. Design rockets, set their mission profile and see them fly.

## Gameplay Loop
You build up infrastructure on your home planet (at first) and 


### Mission Setup
Every mission you get a set of materials for building and fuel and initial conditions. Steel for construction, kerosene and other fuels for propellant.

The mission goal can be landing on the surface, landing on a specific spot, launching to orbit or rendezvous with another object in orbit, for example.

### GameState.play
With every update every rocket except the active one is considered be active, whether launching, coasting or injection or maneuver burning. Every tick its position, velocity and fuel amount are updated according to the dt (delta time, how much change in time is being calculated) parameter. Properties like (total) mass are updated dynamically through @property attributes.

Every rocket has an update method which is called every update tick and passed any objects which it needs for its calculations. Rockets are linked to a sphere of influence of a nearby celestial object, and can change SOI once they get far enough away from them.

### Rocket
- The mass of the rocket is the sum of the mass of its own structural mass, fuel tanks, engines and payload.
- The thrust of the rocket is the sum of the thrusts of its engines (not including the payload)
- The fuel flow rate is the sum of the fuel flow rate of its fuel tanks
- Fuel tanks have a fuel type associated with them
- Orientation: where the rocket is pointing

### Fuel Type
- Has a density

### Fuel Tank
Has:
- A fuel type
- Dry mass

### Engine
Has
- Mass
- Fuel Type
- Fuel flow rate
- Thrust

### Celestial Bodies
These are places rockets can interact with. They have:
- Surface gravity
- Radius
- Rotation speed
- An atmosphere defined by surface density and scaling attitude
- Color, surface features
- Orbit around parent celestial body
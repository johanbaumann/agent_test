# N-Body Simulation

This repository contains a small interactive n-body physics simulation built with Python and Pygame.

## Requirements

- Python 3.11+
- `pygame` library

Install dependencies with:

```bash
pip install pygame
```

## Running the Simulation

Execute the script using Python:

```bash
python nbody.py
```

A window will open where you can interact with the simulation:

- **Left click** to add a body at the mouse position.
- **Right click** to remove the nearest body.
- Press **`c`** to clear all bodies.

Bodies attract each other using a simple gravitational model. Objects bounce off the window edges so they remain visible. The simulation updates at 60 frames per second.

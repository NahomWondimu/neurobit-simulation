# Maze Demo Usage Instructions

This project includes two interactive maze visualization demos. Both require Pygame to be installed.

## Prerequisites

Make sure you have the required dependencies installed:

```bash
pip3 install pygame
```

## Demo 1: displayIt.py - Neural Pulse Maze

### How to Run
```bash
python3 displayIt.py
```

### Description
A small interactive maze (10x6 grid) that demonstrates neural pulse propagation through a generated maze structure.

### Mouse-Click Behavior
- **Left Click**: Click anywhere on a maze cell to spawn a neural pulse at that location
- Each click creates a new "neurobit" with random properties (ID, pattern, mask)
- Multiple pulses can exist simultaneously and interact with each other

### Visual Feedback
- **Red Background**: Walls/barriers that block movement
- **Grey Cells**: Regular maze paths
- **Blue Cells**: Exit points (maze boundaries that lead outside)
- **White Fading Effect**: Shows where pulses have recently traveled
- **Gold Highlighting**: The brightest/most active pulse appears in gold
- **Pulse Propagation**: Watch as neural pulses move through the maze based on their neurobit patterns
- **Collision Avoidance**: Pulses avoid positions occupied by other active pulses

### Expected Behavior
- Pulses automatically navigate through the maze using their neural patterns
- Each pulse has a time-to-live (TTL) of 7 steps before disappearing
- Pulses can split and create new pulses during navigation
- The maze is randomly generated each time you run the program
- Fade effects show the trail left by moving pulses

### How to Quit
- Click the **X** button on the window title bar
- Or press **Alt+F4** (Windows/Linux) or **Cmd+Q** (Mac)

---

## Demo 2: testMaze.py - Large Maze Visualizer

### How to Run
```bash
python3 testMaze.py
```

### Description  
A larger interactive maze (60x30 grid) focused on maze visualization and simple click interactions.

### Mouse-Click Behavior
- **Left Click**: Click on any maze cell to create a bright white highlight at that position
- Each click creates an independent fading effect
- You can click multiple cells to create multiple simultaneous fade effects

### Visual Feedback
- **Red Background**: Walls/barriers between maze cells
- **Grey Cells**: Regular maze paths
- **Blue Cells**: Exit points (special cells at maze edges)
- **Yellow Circles**: Visual markers at exit locations
- **White Fading Boxes**: Bright white boxes that gradually fade to grey and then disappear
- **Smooth Fade Animation**: Clicked cells fade over approximately 6 seconds

### Expected Behavior
- The maze is randomly generated using depth-first search algorithm
- 5 random exit points are placed along the maze edges
- Clicking creates visual feedback without affecting maze structure
- Fade effects run independently and don't interact with each other
- The maze layout remains static once generated

### How to Quit
- Click the **X** button on the window title bar  
- Or press **Alt+F4** (Windows/Linux) or **Cmd+Q** (Mac)

---

## Key Differences Summary

| Feature | displayIt.py | testMaze.py |
|---------|-------------|-------------|
| **Grid Size** | 10x6 (small) | 60x30 (large) |
| **Main Focus** | Neural pulse simulation | Maze visualization |
| **Click Effect** | Spawns moving neural pulses | Creates fading highlights |
| **Interactivity** | Dynamic pulse behavior | Static visual effects |
| **Complexity** | Advanced AI simulation | Simple click-to-highlight |
| **Performance** | Includes sleep delay (0.1s) | Smooth 60 FPS |

## Troubleshooting

If you encounter any issues:

1. **Import Errors**: Make sure `neurobit_walker.py` is in the same directory as `displayIt.py`
2. **Performance**: If displayIt.py runs slowly, this is expected due to the neural simulation complexity
3. **Window Size**: If the maze appears too small/large, you can modify the `BOX_WIDTH` constant in either file
4. **Dependencies**: Ensure Pygame is properly installed with `pip3 install pygame`

Both demos will continue running until you close the window. Enjoy exploring the different maze interactions!

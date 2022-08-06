# CubeSolverAPI
This is an API for Rubik's Cube Solver Robots to solve the cube in the most optimal number of steps

The API could be accessed using the format:

https://cubersolverapi.herokuapp.com/{cubestring}

For {cubestring}, please put a string that represents the pattern of the cube follow the instructions giving here: https://github.com/hkociemba/RubiksCube-TwophaseSolver/blob/master/enums.py

**Examples:**

https://cubersolverapi.herokuapp.com/UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB
https://cubersolverapi.herokuapp.com/DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL

**Explanations for values:**
  - 1. If a pattern is valid, the algorithm will return the solution move sequence to solve the cube, followed by the number of steps in brackets. For example: (20f) means 20 steps

  - 2. If the pattern is invalid, a 404 error would be raised and the error would be returned in the format:
  detail: "Error: ..."
  
**Recognition:**
This project is created based on the Kociemba's algorithm, more information about the algorithm could be found here: https://github.com/hkociemba/RubiksCube-TwophaseSolver

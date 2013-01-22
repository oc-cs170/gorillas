gorillas
========

A basic gorillas game using PyGame.

The program should consist of at least four modules:

* gorillas.py    - Contains the game loop and runs the game
* gorilla.py     - A class to create, update, and draw a sprite-based gorilla
* banana.py      - A class to create, update, and draw a sprite-based banana
* building.py    - A class to create, and draw buildings for the city skyline

To-do
-----

1. Create a gorilla class that uses the given artwork, to draw a gorilla in three states (standing, throwing left, and throwing right)
2. Create a banana class that draws a banana the spins while moving, use the given banana_snippet to help with drawing
3. Create a building class that draws a building at the bottom of the screen, using location and size
4. Implement a game level that draws a random skyline, and places two gorillas accordingly
5. Implement user input to get angle and power of throw, then animate the throw, including wind and gravity
6. Implement banana collisions, subtracting a section of building or destroying a gorilla, as necessary
7. Implement a rudimentary "learning" computer algorithm that adjusts based on the distance between the landing and the target, and optionally landing height (distance to target, target location, and target elevation are not to be used!)
8. Use pygame.font for all on-screen text creation
9. Implement a game system, with multiple rounds (player turns) and multiple levels (hits to a pretermined score), and scoring
10. Add a sun

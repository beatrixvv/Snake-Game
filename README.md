# Snake-Game
It's the classic snake game where you play against the computer.

## Overview
At the beginning of the game, the program will display a screen that consists of the game's status, a brief introduction of the game, the snake, and the monster. The status includes the number of contacts between the snake’s body and the monster, the time elapsed after the game starts in seconds, and the snake's motion. The snake, the blue-colored square, is located at the center of the motion area. The monster, which is the red-colored square, is located at a random position located at least 200 turtle step units from the origin.

The game will start when the player clicks on the screen. The food, shown as the numbers ranging from 1 to 9, will be shown subsequently. The monster will move at a random motion and speed towards the head of the snake. The player can use the keyboard's up, down, left, right, and spacebar keys to move or pause the snake’s motion. At the beginning, the snake will have a body of length five, a yellow square with a black border. The length of the body will increase by the number that the snake consumes. The snake’s movement will slow down when the tail is extended after food consumption.

The game will end when the snake has consumed all the food and the tail has fully extended (player wins) or when the monster has reached the snake’s head (player loses). 

## Program structure
1.	Set the screen before the game starts (before the player clicks on the screen).
    -	Draw the border for the status area and the motion area.
    -	Display a brief introduction and the initial status of the game.
    -	Set the snake’s body and head in the center of the motion area (the head will cover the snake’s body).
    -	Set the monster in a random position at a reasonable distance from the snake.
2.	Wait for the player to click on the screen.
3.	When the player clicks on the screen,
     - Clear the introduction shown at the beginning of the game.
     - Display the food subsequently.
     - While the game is not over,
         * Update the status.
         * Snake moves according to the input given by the player.
         * Monster moves at random motion and speed towards the snake’s head.
         * The food passed by the snake will be removed.
4. If no more food is on the screen and the tail has fully extended, the player wins. If the monster collides with the snake’s head, the player loses.

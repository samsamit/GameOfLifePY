# GameOfLifePY
Game of life made with python and pygame

To try the game just download and run the .exe file from /Exec folder

## Rules of the game 
You bring cells to live by clicking the dead cell (grey rectangle)
Then you can make a single evolve with the button that says "Evolve" or start evolving the cells automatically by pressing the "Play" button.
When evolve action is called every cell will follow thease set of rules:
  1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
  2. Any live cell with two or three live neighbours lives on to the next generation.
  3. Any live cell with more than three live neighbours dies, as if by overpopulation.
  4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
You can make more cells with the Cells + and - buttons but beware the game cant handle too many rects.


You can try it out by making this type of figure and pressing play!
![image](https://user-images.githubusercontent.com/48052278/131803385-00723d18-8ec5-473f-badd-ecbc0e717fbf.png)

## Dev notes
This was purely a fun learning project that i can actually finish fast and have something nice and ready to show people. Conway's Game of Life was perfect for this type of project. I have always liked the simplicity of the game. I didnt use any time for the UI but i wwanted to make the game responsive because thats the least i can do for the user. 

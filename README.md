Python Maze Generator
[hr]
Just a fun little experiment to see if I can generate mazes.

Function: generateMaze
Arguments:	width
				The width of the maze
			height
				The height of the maze
			startingpoint
				Where the maze will begin generating from.
Returns:	Maze Table
Description:
			Generate a simple maze and return it as a table.

			
Function: generateMazeAnimated
Arguments: width
				The width of the maze
			height
				The height of the maze
			startingpoint
				Where the maze will begin generating from.
Returns: Maze Table
Description:
			Essentially the same as generateMaze, only it will
			capture what the maze looks as a PNG like every time
			the "cursor" moves. Once the maze has finished generating,
			it will stitch all the PNGs together and create a GIF.
			Lastly, it will clean up all the PNGs.
Function: pngMaze
Arguments:	mazeTable
				The maze generated using generateMaze or generateMazeAnimated.
			name
				The filepath of the generated maze.

				
Example:
	m = generateMaze(100,100,[10,5])
	pngMaze(m, "mazes/experiment.png")
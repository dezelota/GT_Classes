import random, argparse, pdb
import matplotlib.pyplot as plt # We have not covered this module yet but we use this for plotting

"""
Group Members: []

Week 6 Exercise (10 Points)

Due Date: This assignment is due on Monday September 28, 2026 @ 12:30pm

Directions: Please edit this template in order to model bacterial killing. You must use, edit, and submit this python script directly for this assignment.

Collaboration: 
You must work in small groups (2-4 students) on this assignment!
Failure to do so will result in an automatic 15% penalty to your submission. 
Please indicate who worked on the assignment together at the top of this script and if you want any parts graded differently between group members in your submission, else all members will get the same grade.

Submission Details: 
Please submit 1 script per group. For members of the group who do not submit the script, there will be a text box available on the submission page. 
Please tell me who you worked with in the text box and I will assign the same grade to you and all other members of that group. 

Sources:
At the end of the script, in a comment block like this one, please include a list of any links to any webpages (stackoverflow, github, geeksforgeeks etc.) used for help completing the assignment.

"""

"""
Bacterial Warfare  Example

General instructions: Please use this code skeleton for your implementation, making no changes to the function names,
function parameter names, or function return-value names. We recommend that you complete this assignment in the
following order:
	1. implement the argument parser, as described in the "if __name__ == '__main__'" block at the bottom of this script (3 points)
	2. implement seed_grid (3 points)
	3. implement update_grid (3 points)
	4. run your code and confirm that the plots you see resemble those from the paper (1 point)
"""

def seedGrid(n):
	# This function should create a grid of n x n squares
	# Each square should contain the value -1 (for the red species), 1 (for the blue species), or 0 (if it is empty)
	# Implement this as a list of lists: [[],[],[]]
	# Use two for loops to loop through each dimension of the grid
	# Use the random module to generate an integer of -1 or 1 to randomly seed the grid with one or the other species

	assert type(n) == int
	grid = []
	for x in range(n):
		grid.append([])
		for y in range(n):
			grid[-1].append(random.choice([-1, 1]))
	return grid

def updateGrid(grid, killing_rate = 0.05, reproducing_rate = 0.05):
	assert type(grid) == list
	assert type(killing_rate) == float
	assert type(reproducing_rate) == float

	# This function takes in a grid and updates it by killing and reproducing a random number of elements

	n = len(grid)  # defined once, up top, so it's always available below

	# Determine how many cells are activated for T6SS (killing_rate * number of grid squares)
	# n * n = total number of squares; len(grid) alone is only the number of rows
	num_activated = round(killing_rate * n * n)
	assert type(num_activated) == int

	# This variable is useful to keep track of the total number of killed cells
	num_killed = 0

	# Loop through number of cells that are activated
	for i in range(num_activated):
		# Randomly select an x and y position, representing a cell that is activated.
		x = random.randint(0, n-1)
		y = random.randint(0, n-1)

		# Determine if the cell contains a bacteria, if not continue!
		if grid[x][y] == 0:
			continue

		# Loop through each of the nearby neighbors of this activated cell
		for j in [-1, 0, 1]:
			for k in [-1, 0, 1]:
				if j == 0 and k == 0:
					continue  # skip cell itself -- it's not a neighbor of itself

				neighbor_x = x + j
				neighbor_y = y + k

				# Determine if the neighbor is still within the grid. If it's not, continue to the next neighbor
				if neighbor_x < 0 or neighbor_x > n-1 or neighbor_y < 0 or neighbor_y > n-1:
					continue

				# Determine if the neighbor contains a bacteria, if not continue!
				if grid[neighbor_x][neighbor_y] == 0:
					continue

				# If the neighbor is a different species, than kill it! Make sure to increment the num_killed variable
				if grid[neighbor_x][neighbor_y] != grid[x][y]:
					grid[neighbor_x][neighbor_y] = 0
					num_killed += 1

	# Determine how many cells are reproducing
	num_reproducing = round(reproducing_rate * n * n)
	assert type(num_reproducing) == int

	# This variable is useful to keep track of the total number of new cells
	num_new = 0

	# Loop through number of cells that are reproducing
	for i in range(num_reproducing):
		# Randomly select an x and y position, representing a cell that is reproducing.
		x = random.randint(0, n-1)
		y = random.randint(0, n-1)

		# Determine if the cell contains a bacteria, if not continue!
		if grid[x][y] == 0:
			continue

		# Loop through each of the nearby neighbors of this reproducing cell
		for j in [-1, 0, 1]:
			for k in [-1, 0, 1]:
				if j == 0 and k == 0:
					continue

				neighbor_x = x + j
				neighbor_y = y + k

				# Determine if the neighbor is still within the grid. If it's not, continue to the next neighbor
				if neighbor_x < 0 or neighbor_x > n-1 or neighbor_y < 0 or neighbor_y > n-1:
					continue

				# If the neighbor is empty, than reproduce! Increment the num_new variable
				if grid[neighbor_x][neighbor_y] != 0:
					continue

				grid[neighbor_x][neighbor_y] = grid[x][y]
				num_new += 1

	print(str(num_killed) + ' bacteria were killed')
	print(str(num_new) + ' new cells were produced')

	return num_killed, num_new # Don't need to return grid. Why? Grid is a shallow copy and will be modified without returning it

def updatePlot(img_obj, grid, i):
	"""
	Leave the code in this section as it is. You do not need to add any code.
	This function is used to update the plot of the current bacterial distribution across the playing field. The
	parameter img_obj should be a matplotlib.image.AxesImage object, which is the type of object returned by
	matplotlib.pyplot.matshow().

	:param img_obj: plotting object to be updated
	:type img_obj: matplotlib.image.AxesImage
	:param grid: array containing the current playing field
	:type grid: list of lists
	:param i: current simulation step
	:type i: int
	"""

	# use the matplotlib.image.AxesImage.set_data() method to update array associated with img_obj
	img_obj.set_data(grid)
	# update the title to be "Step i", where i is the current step
	plt.title('Step ' + str(i))
	# use the matplotlib.pyplot.draw() command to redraw the figure
	plt.draw()
	# use the matplotlib.pyplot.pause() command to delay the drawing of the next frame by 0.1 seconds
	plt.pause(.1)

	# this return statement is not necessary, but is included to help with grading
	return img_obj

if __name__ == '__main__':
	# Use argparse to take in the grid size, the number steps you want to simulate, the killing_rate, and the
	# reproduction_rate. Set the default values of these arguments to what was used in the paper. Use flagged arguments
	# for all four arguments. Use the flag names
	# "--gridsize", default value = 500
	# "--n_steps", default value = 250
	# "--killing_rate", default value = 0.05 
	# "--reproduction_rate", default value = 0.05
	# include a descriptive help string for each, and specify the expected type. Please place all of your argument
	# parsing code here, within the __name__ == '__main__' block.

	# add your argument parsing code here
	parser = argparse.ArgumentParser(description='Simulate T6SS-mediated killing between two bacterial species on a 2D grid.')
	parser.add_argument('--gridsize', type=int, default=500,
						help='Length of one side of the square grid (grid is gridsize x gridsize). Default: 500')
	parser.add_argument('--n_steps', type=int, default=250,
						help='Number of simulation steps to run. Default: 250')
	parser.add_argument('--killing_rate', type=float, default=0.05,
						help='Fraction of grid squares activated for T6SS killing each step. Default: 0.05')
	parser.add_argument('--reproduction_rate', type=float, default=0.05,
						help='Fraction of grid squares selected to reproduce each step. Default: 0.05')
	args = parser.parse_args()

	# do not modify the below code
	grid = seedGrid(args.gridsize)
	img_obj = plt.matshow(grid, cmap='seismic')
	for i in range(args.n_steps):
		print('Loop: ' + str(i))
		num_killed, num_reproducing = updateGrid(grid, args.killing_rate, args.reproduction_rate)
		updatePlot(img_obj, grid, i)
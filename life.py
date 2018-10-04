
#
from random import randint

#grid = None
def generateGrid(height, width):
	global grid
	grid = [0]*height
	for i in grid:
		row = [0]*width
		for j in range(len(row)):
			newVal = randint(0,1)
			if newVal == 0:
				row[j] = " "
			elif newVal == 1:
				row[j] = "*"
		global grid
		grid[i] = row

	print grid

#def printGrid():
	#global grid
	#for i in grid:
	#	rowString = ""
	#	print i
	#	for j in i:
	#		rowString+=j
		#print rowString
	
generateGrid(25,25)
printGrid()

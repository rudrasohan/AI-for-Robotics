# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
	path = []
	count = 0
	temp = [[0,init[0],init[1]]]
	t = init
	grid1 = grid
	grid1[init[0]][init[1]] = 1
	FINAL = []
	print delta
	while True:
		k = [-9,-9]
		m = temp[0][0]
		p = 0
		for i in range(0,len(temp)):
			if(temp[i][0]<m):
				p = i
	
		t = [temp[p][1],temp[p][2]]
		count = temp[p][0] + cost
		del temp[p]
		#print temp[p][0]
		if (count == 5):
			print t
		for i in range(4):
			k[0] = t[0] + delta[i][0]
			k[1] = t[1] + delta[i][1]
			#print k
			if (count == 5):
				print k,delta[i],temp
			if((k[0]>=0 and k[1]>=0) and (k[0]<5 and k[1]<6) and (grid[k[0]][k[1]] == 0) and (k[0]<=goal[0] and k[1]<=goal[1]) ):
				temp.append([count,k[0],k[1]])
				grid1[k[0]][k[1]] = 1
		
		print temp
		print grid1[0]
		print grid1[1]
		print grid1[2]
		print grid1[3]
		print grid1[4]
		if(len(temp) == 1):
			FINAL = temp[0]
		if(len(temp) == 0):
			break
	if (FINAL[1] == goal[0] and FINAL[2] == goal[1]):
		print "PASS"			
		print FINAL
	else :
		print "FAIL"
			

search(grid,init,goal,cost)

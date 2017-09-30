# -----------
# User Instructions:
# 
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid 
# you return has the value 0.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [1, 0]
#goal = [3,1]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    c = 0
    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            c +=1
                            closed[x2][y2] = 1
                            expand[x2][y2] = c
    expand[0][0] = 0  
    path = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]   
    dx = 0
    dy = 0
    l = 0
    r = 0
    u = 0
    d = 0
    i = 0
    j = 0
    while True:
    	if((j-1) >= 0):
    		l = expand[i][j-1]
    	if((i-1) >= 0):
    	 	u = expand[i-1][j]
    	if((j+1) < 6):
    	 	r = expand[i][j+1]
    	if((i+1) < 5):
    	 	d = expand[i+1][j]
    	lis = [l,r,u,d]
    	m = max(lis)
    	pos = [a for a, b in enumerate(lis) if b == m]
    	#print pos
    	if (pos[0] == 0):
    		path[i][j] = delta_name[1]
    		j = j - 1
    	if (pos[0] == 1):
    		#print "right"
    		path[i][j] = delta_name[3]
    		j = j + 1
    	if (pos[0] == 2):
    		path[i][j] = delta_name[0]
    		i = i - 1
    	if (pos[0] == 3):
    		path[i][j] = delta_name[2]
    		i = i + 1
    	if(i == goal[0] and j == goal[1]): 
    		break
     	 
    #path[0][0] = delta_name[2]    
    path[goal[0]][goal[1]] = '*'           
    return path

a = search(grid,init,goal,cost)
print a[0]
print a[1]
print a[2]
print a[3]
print a[4]

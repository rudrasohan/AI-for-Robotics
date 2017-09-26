colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]
measurements = ['G','G','G','G','G']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

r,c =4,5
p = [[0.05 for x in range(c)] for y in range(r)]

sensor_right = 0.7
p_move = 0.8

def sense(p,Z):
	r,c =4,5
	q = [[0 for x in range(c)] for y in range(r)]
	s = 0.0
	for i in range(r):
		for j in range(c):
			hit = (float)(colors[i][j] == Z)
			q[i][j] = p[i][j]*(hit*sensor_right + (1-hit)*(1-sensor_right)) 
			s = s + q[i][j]
	for i in range(r):
		for j in range(c):
			q[i][j] = q[i][j]/s
	return q

def move(p,U):
	r,c =4,5
	q = [[0 for x in range(c)] for y in range(r)]
	for i in range(r):
		for j in range(c):
			q[i][j] = p_move*p[(i-U[0])%4][(j-U[1])%5] + p[i][j]*(1-p_move)
	return q

for i in range(len(motions)):   
    p = move(p,motions[i])
    p = sense(p,measurements[i])
    
print p[0]
print p[1]
print p[2]
print p[3]

colors=[['green','green','green'],
		['green','red','red'],
		['green','green','green']]

r,c =3,3
p = [[0.1111111 for x in range(c)] for y in range(r)]
	
measurements=['red','red']

motions=[[0,0],[0,1]]

sensor_right = 0.8
p_move = 1.0

def sense(p,Z):
	r,c =3,3
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
	r,c =3,3
	q = [[0 for x in range(c)] for y in range(r)]
	for i in range(r):
		for j in range(c):
			q[i][j] = p[(i-U[0])%3][(j-U[1])%3]
	return q

p = move(p,motions[0])
p = sense(p,measurements[0])
p = move(p,motions[1])
p = sense(p,measurements[1])
print p[0]
print p[1]
print p[2]

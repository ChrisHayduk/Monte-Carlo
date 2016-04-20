import numpy as np
import math
import matplotlib.pyplot as plt

#Randomly add edges to a graph until it is connected

def randomly_add_edges(k):	#k is the number of vertices on the graph
	numAttempts = 0
	listOfEdges = []
	matrix = []
	
	for i in range(k):	#Initialize matrix of graph to 0
		tempRow = []
		for j in range(k):
			tempRow.append(0)	
		matrix.append(tempRow)

	for i in range(k):	#Create a list of tuples that represents all possible edges
		for j in range(k):
			if j != i:
				listOfEdges.append((i, j))

	y = []
	
	for i in range(len(listOfEdges)):
		y.append(i)	
	
	while(check_connectedness(matrix, k) != True):	#Checks if the graph is connected
		m = np.random.choice(y, replace=False)
		y.remove(m)
	
		x = listOfEdges[m]	#Selects a random element from listOfEdges
	
		n = x[0]
		q = x[1]
	
		matrix[n][q] = 1	#Sets spot in matrix equal to 1
		
		numAttempts += 1	#Increments number of attempts

	return numAttempts	#Returns number of attempts

def check_connectedness(A, k):	#A is the matrix representing the graph and k is the number of vertices
	B = A
	tOrF = False

	for j in range(2,k+1):
		B = B + np.linalg.matrix_power(A,j)
	
	if np.prod(B) != 0:
		tOrF = True

	return tOrF

def average_number_of_edges(n, k):	#n is the number of times to loop. K is the number of vertices
	s = 0.0
	
	if k > 1:
		for i in range(n):
			s += randomly_add_edges(k)

	return s/n


#Let e(k) be the expected number of directed edges needed to be added to k vertices to make the graph connected.
#Plot e(k) vs. k for k up to 50

points = 10 

xlist = []
ylist = []

for i in range(points+1):
	xlist.append(i)
	ylist.append(average_number_of_edges(100, i))

ymax = max(ylist)

plt.plot(xlist, ylist, 'bo--')
plt.axis([-.1, points, 0, ymax+1])
plt.show()


#Also, find probability that k vertices is connected with k edges using Monte Carlo. Then in general, obtain a function,
#called p(k). Plot it. Then come up with a forumula for p(k) by hand and write a function that computes it with that formula

def probability_k_vertices_connected_with_k_edges(n, k):
	s = 0.0
	
	for i in range(n):
		if randomly_add_edges(k) == k:
			s += 1.0
	
	return s/n

print probability_k_vertices_connected_with_k_edges(1000, 4)

#Start at 1 on number line. Flip a coin to determine whether to go left or right.
#Find probability that you will end up at 0 in certain number of flips

def average_probability_of_reaching_zero(n, k): #k is the number of flips, n is the number of trials
	s = 0.0

	for i in range(k):
		if did_reach_zero(k):
			s += 1.0
	
	return s/n

def did_reach_zero(k): #k is the number of flips
	position = 1
	tOrF = False

	for i in range(k):	
		m = np.random.choice(1)
		print m	
		if m:
			position += 1
		else:
			position -= 1
	
	if position == 0:
		tOrF = True

	return tOrF

#print average_probability_of_reaching_zero(100, 5)	

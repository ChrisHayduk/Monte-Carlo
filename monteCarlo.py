import numpy as np
import math
import matplotlib.pyplot as plt
import graphviz

#March 29 Lecture Exercise

def get_graphviz_from_adj_mat2(graph_adj_mat):
	if np.array_equal(np.array(graph_adj_mat), np.transpose(np.array(graph_adj_mat))):
		graphviz_graph = graphviz.Graph(comment='This is a graph')

		#Initialize graph's vertices.
		for r in range(len(graph_adj_mat)):
			graphviz_graph.node(str(r))
	
		#Add edges
		for r in range(len(graph_adj_mat)):
			for c in range(len(graph_adj_mat[r])):
				if r <= c and graph_adj_mat[r][c] > 0:
					for i in range(graph_adj_mat[r][c]):
						graphviz_graph.edge(str(r), str(c))
		
	else:
		graphviz_graph = graphviz.Digraph(comment='This is a digraph')
		
		#Initialize graph's vertices
		for r in range(len(graph_adj_mat)):
			for c in range(len(graph_adj_mat[r])):
				if graph_adj_mat[r][c] > 0:
					for i in range(graph_adj_mat[r][c]):
						graphviz_graph.edge(str(r),str(c))
	
	return graphviz_graph

my_graph_adj_mat = [[0,2,1,3], [1,0,0,4], [1,0,0,3], [3,1,2,0]]	

g = get_graphviz_from_adj_mat2(my_graph_adj_mat)

g.format='png'
g.render('g_graph.gv', view=True)


#April 4 Lecture Exercise

def createListOfEdges(k):
	listOfEdges = []
	
	for i in range(k):
		for j in range(k):
			if j != i:
				listOfEdges.append((i, j))
	
	return listOfEdges

def check_connectedness(A, k):  #A is the matrix representing the graph and k is the number of vertices
        B = A
        tOrF = True

        for j in range(2,k+1):
                B = B + np.linalg.matrix_power(A,j)

	for x in range(k):
		for y in range(k):
			if B[x][y] == 0:
				tOrF = False

        return tOrF

def randomly_add_edges(k):	#k is the number of vertices on the graph
	numAttempts = 0
	matrix = np.zeros(shape=(k, k))	#Creates a matrix of zeros of size k,k
	listOfEdges = createListOfEdges(k)	#Creates a list of all possible edgs

	y = range(len(listOfEdges))	#Gets all of the possible indices for the list of edges

	while(check_connectedness(matrix, k) == False):	#Checks if the graph is connected
		m = np.random.choice(y, replace=False)	#Selects a random index from list of edges
		y.remove(m)	#Removes index from list of indices
	
		x = listOfEdges[m]	#Gets tuple at position m

		n = int(m/10)
		q = m%10
			
		n = x[0]	#Split tuple into two variables
		q = x[1]
	
		matrix[n][q] = 1	#Sets spot in matrix equal to 1
		
		numAttempts += 1	#Increments number of attempts

	return numAttempts	#Returns number of attempts

def average_number_of_edges(n, k):	#n is the number of times to loop. K is the number of vertices
	s = 0.0
	
	if k > 1:
		for i in range(n):
			s += randomly_add_edges(k)

	elif k == 1:
		return k
		
	return s/n

print average_number_of_edges(100, 5)	


#April 5 Lecture Exercise

#Let e(k) be the expected number of directed edges needed to be added to k vertices to make the graph connected.
#Plot e(k) vs. k for k up to 50

points = 30 

xlist = []
ylist = []

for i in range(points+1):
	xlist.append(i)
	ylist.append(average_number_of_edges(100, i))

ymax = max(ylist)

plt.plot(xlist, ylist, 'bo--')
plt.axis([-.1, points, 0, ymax+1])
plt.show()



#Not exercises

#Also, find probability that k vertices is connected with k edges using Monte Carlo. Then in general, obtain a function,
#called p(k). Plot it. Then come up with a forumula for p(k) by hand and write a function that computes it with that formula

def probability_k_vertices_connected_with_k_edges(n, k):
	s = 0.0
	
	for i in range(n):
		if randomly_add_edges(k) == k:
			s += 1.0
	
	return s/n

#print probability_k_vertices_connected_with_k_edges(1000, 4)

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

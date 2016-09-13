# Idea taken from http://mathematica.stackexchange.com/questions/608/how-to-generate-random-directed-acyclic-graphs
import random, sys

def GenerateDAG(n, k):
	# Adjacency Matrix
	Graph = [ [0]*n for i in xrange(n)]
	for i in range(n):
		temp = random.sample(range(i),min(i,random.randint(0,k)))
		for j in temp:
			Graph[i][j] = 1
	return Graph

def PrintArray(i, A):
	st = str(i+1)+' ['
	for i in range(len(A)):
		if A[i] == 1:
			st += str(i+1)+','
	if st[-1] == '[': 
		return (st+']')
	else:
		return (st[:-1]+']')

def DAGPrinter(DAG):
	for i in range(len(DAG)):
		print PrintArray(i,DAG[i])

print (sys.argv[1])
DAGPrinter(GenerateDAG(int(sys.argv[1]),int(sys.argv[2])))
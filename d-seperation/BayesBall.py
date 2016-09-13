import sys
import copy
execfile('BayesianNetworkIO.py')

la = 0


def descendents(BayesianNetwork, Z):
	Des = [copy.deepcopy(Z)]
	i =  0
	while (i < len(Des)):
		Des += BayesianNetwork[Des[i]]
		i = i+1
	return [Z]

def BayesBall(BayesianNetwork, Reverse, X, Y, Z, isRight, Xi, Trail):
	RightNodes = BayesianNetwork[Xi]
	LeftNodes = Reverse[Xi]

	if Y == Xi:
		return Trail

	if len(Trail) == len(BayesianNetwork):
		return
	else:
		if isRight: # Visit is from child
			for la in descendents(BayesianNetwork, Xi):
				if la in Z:
					for i in LeftNodes:
						if i not in Trail:
							toReturn = BayesBall(BayesianNetwork, Reverse, X, Y, Z, False, i, Trail+[i])
							if toReturn: return toReturn
					for i in RightNodes:
						if i not in Trail:
							toReturn = BayesBall(BayesianNetwork, Reverse, X, Y, Z, True, i, Trail+[i])
							if toReturn: return toReturn
		else:
			for la in descendents(BayesianNetwork ,Xi):
				if la in Z:
					for i in LeftNodes:
						if i not in Trail:
							toReturn = BayesBall(BayesianNetwork, Reverse, X, Y, Z, False, i, Trail+[i])
							if toReturn: return toReturn
				else:
					for i in RightNodes:
						if i not in Trail:
							toReturn = BayesBall(BayesianNetwork, Reverse, X, Y, Z, True, i, Trail+[i])
							if toReturn: return toReturn
	return

def MainBayesBall(BayesianNetwork, X, Y, Z):
	reverse = Reverse(BayesianNetwork)
	LeftNodes = BayesianNetwork[X]
	RightNodes = reverse[X]
	# TODO: Change Z to Z + descendents(Z)
	for i in LeftNodes:
		toReturn = BayesBall(BayesianNetwork, reverse, X, Y, Z, False, i, [X, i])
		if toReturn: return toReturn
	for i in RightNodes:
		toReturn = BayesBall(BayesianNetwork, reverse, X, Y, Z, True, i, [X, i])
		if toReturn: return toReturn
	return

debugging = False
if debugging: print MainBayesBall(Read(), 0, 3, [1,2])

def BayesBallOutput(out):
	if out == None:
		print "yes"
		return
	st = ""
	for i in out:
		if st == "":
			st = str(i+1)
		else:
			st = st + ","+ str(i+1)
	st = "["+st+"]"
	print 'no '+st

BN = Read(str(sys.argv[1]))
f = open(str(sys.argv[2]),'r')
for i in f.readlines():
	print i.strip()
	data = i.strip().split()
	BayesBallOutput(MainBayesBall(BN, int(data[0])-1, int(data[1])-1, [l-1 for l in eval(data[2])]))
f.close()

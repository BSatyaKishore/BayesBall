execfile('BayesianNetworkIO.py')

la = 0

def BayesBall(BayesianNetwork, Reverse, X, Y, Z, isRight, Xi, Trail):
	RightNodes = BayesianNetwork[Xi]
	LeftNodes = Reverse[Xi]

	if Y == Xi:
		return Trail

	if len(Trail) == len(BayesianNetwork):
		return
	else:
		if isRight: # Visit is from child
			if Xi in Z:
				for i in LeftNodes:
					if i not in Trail:
						toReturn = BayesBall(BayesianNetwork, Reverse, X, Y, Z, False, i, Trail+[i])
						if toReturn: return toReturn
				for i in RightNodes:
					if i not in Trail:
						toReturn = BayesBall(BayesianNetwork, Reverse, X, Y, Z, True, i, Trail+[i])
						if toReturn: return toReturn
		else:
			if Xi in Z:
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
	for i in LeftNodes:
		toReturn = BayesBall(BayesianNetwork, reverse, X, Y, Z, False, i, [X, i])
		if toReturn: return toReturn
	for i in RightNodes:
		toReturn = BayesBall(BayesianNetwork, reverse, X, Y, Z, True, i, [X, i])
		if toReturn: return toReturn
	return

debugging = False
if debugging: print MainBayesBall(Read(), 0, 3, [1,2])

print MainBayesBall(Read(), 0, 4, [2])

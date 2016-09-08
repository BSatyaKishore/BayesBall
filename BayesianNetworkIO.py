def Parse(text):
	toReturn = []
	for i in eval(text.split()[1]):
		toReturn.append(i-1)
	return toReturn

def Read():
	BayesianNetwork = []
	for i in range(input()):
		BayesianNetwork.append(Parse(raw_input()))
	return BayesianNetwork

def Write(BayesianNetwork):
	print len(BayesianNetwork)
	for i in range(len(BayesianNetwork)):
		toPrint = "["
		for j in BayesianNetwork[i]:
			toPrint += str(j+1)+','
		if toPrint[-1] == ',':
			toPrint = toPrint[:-1]
		toPrint += ']'
		print i+1, toPrint

def Reverse(BayesianNetwork):
	toReturn = []
	for i in BayesianNetwork:
		toReturn.append([])
	for i in range(len(BayesianNetwork)):
		for j in BayesianNetwork[i]:
			toReturn[j].append(i)
	return toReturn

debugging = False
if debugging:
	Write(Read())

#print Reverse(Read())
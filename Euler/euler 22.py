def nameScores(file):
	f = open(file, "r")
	ic = f.readlines()
	f.close()
	nameList = sorted(ic[0].replace('"','').split(","))
	nameDict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
	scoreList = []
	position = 1
	
	for n in nameList:
		score = 0
		for c in n:
			score += nameDict[c]*position
		scoreList.append(score)
		score = 0
		position += 1
	sum = 0
	for i in scoreList:
		sum += i
	return sum
def main():
	file = "p022_names.txt"
	print(nameScores(file))
	
main()
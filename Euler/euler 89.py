def numLength(file):
	f = open(file,"r")
	numList = []
	input_contents = f.readlines()
	f.close()
	for i in input_contents:
		i = i.strip("\n")
		count = str(i)
		numList.append(count)
	return numList
def RomanToList(file):
	f = open(file,"r")
	input_contents = f.readlines()
	f.close()
	RomanToInt = []
	RomanDict = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
	for i in input_contents:
		i = i.strip("\n")
		numeralList = list(i)
		count = 0
		for r in numeralList:
			count += RomanDict[r]
		RomanToInt.append(count)
	return RomanToInt
	
def IntToRoman(test):
	modList = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
	checker = [2,3,6,7,10,11]
	romList = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
	count = 0
	final = ""
	
	index = []
	for i in range(len(modList)):
		if test < modList[i]:
			index.append(0)
			continue
		while True:
			if ((test % modList[i]) == test):
				final = final + count*romList[i]
				count = 0
				break
			elif (i in checker):
				if (final.find(romList[i]) == -1):
					test = test - modList[i]
					final = final + romList[i]
					count = 0
					break
				else:
					count = 0
					break
			else:
				count += 1
				test = test - modList[i]	
	return final
def main():
	file = "p089_roman.txt"	
	RomanList = RomanToList(file)
	compare = numLength(file)
	saved = 0
	for i in range(len(RomanList)):
		ok = len(compare[i]) - len(IntToRoman(RomanList[i]))
		saved += ok
		print(IntToRoman(RomanList[i]),len(IntToRoman(RomanList[i])), compare[i],len(compare[i]) )
	print(saved)
	
main()
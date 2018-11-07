def Perm():
	listNum = []
	for i in range(100000,1000000):
		listNum.append(i)
	return listNum
	
def SortPerm(arr):
	for i in arr:
		m = sorted([int(digits) for digits in str(i)])
		a = sorted([int(digits) for digits in str(2*int(i))])
		b = sorted([int(digits) for digits in str(3*int(i))])
		c = sorted([int(digits) for digits in str(4*int(i))])
		d = sorted([int(digits) for digits in str(5*int(i))])
		e = sorted([int(digits) for digits in str(6*int(i))])
		if m == a and m == b and m == c and m == d and m == e:
			return i,m,a
def main():
	arr = Perm()
	print(SortPerm(arr))
	
main()
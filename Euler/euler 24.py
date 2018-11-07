from itertools import permutations
def perm():
	string = '0123456789'
	permList = [''.join(p) for p in permutations(string)]
	print(permList[999999])
perm()
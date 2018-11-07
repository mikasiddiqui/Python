def trianglePath(file):
	f = open(file,"r")
	ic = f.readlines()
	f.close()
	triangle = []
	path = []
	index = 0
	for i in ic:
		i = i.strip("\n").split()
		num = [int(n) for n in i]
		triangle.append(num)
		
	for i in triangle:
		if len(i) > 1:
			app = max(i[index], i[index + 1])
			path.append(app)
			index = i.index(app)
		else:
			path.append(i[0])
	sum = 0	
	for n in path:
		sum += n
	return path,sum
def main():
	file = "p018_sum.txt"
	print(trianglePath(file))
	
main()
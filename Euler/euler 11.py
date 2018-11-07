def grid(file):
	f = open(file,'r')
	ic = f.readlines()
	gridM = []
	count = 19
	f.close()
	for i in ic:
		i = i.strip().split()
		gridM.append(i)
	for i in range(len(gridM)):
		for x in range(len(gridM[i])):
		
			if(x + 4 <= 20):
				print(gridM[i][x:x+4])
		print()
	return gridM
def main():
	file = "grid.txt"
	print(grid(file))
	
main()
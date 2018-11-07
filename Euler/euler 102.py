import math
def Formula(x1,x2,x3,y1,y2,y3):
	return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))/2)

#From a given list, count the number of triangles where the origin point sits inside
def TriangleOrigin(file):
	f = open(file,"r") #input
	input_contents = f.readlines()
	f.close()
	count = 0
	for i in input_contents:
		i = i.strip("\n")
		c = i.split(",")
		coord = [int(x) for x in c] #int coordinate list
		
		x1,x2,x3 = coord[0],coord[2],coord[4]
		y1,y2,y3 = coord[1],coord[3],coord[5]
		ox,oy = 0,0 #origin point
		
		a = Formula(x1,x2,x3,y1,y2,y3) #area
		a1 = Formula(ox,x2,x3,oy,y2,y3)
		a2 = Formula(x1,ox,x3,y1,oy,y3)
		a3 = Formula(x1,x2,ox,y1,y2,oy)	
		
		if (a == (a1 + a2 + a3)):
			count += 1
	return count
	
def main():
	file = "p102_triangles.txt"
	print(TriangleOrigin(file))
	
main()
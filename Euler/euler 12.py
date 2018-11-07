import math

def g(x):
	return x**2 + 1
	
def rhoAlgorithm(arr):
	x,y,d = 2,2,1
	while d == 1:
		x = g(x)
		y = g(g(y))
		d = math.gcd(abs(x - y), arr[10])
		
		if d == arr[10]:
			return False
		else:
			return d

def triangleDivisor():
	triangleNums = [1]
	
	for i in range(2,5000):
		nextNum = triangleNums[-1] + i
		triangleNums.append(nextNum)
	return triangleNums
	
def main():
	arr = triangleDivisor()
	print(rhoAlgorithm(arr))
	
main
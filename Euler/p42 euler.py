import math

def TriangleNumbers(file):
	letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	triangle_list = []
	f = open(file,'r')
	input_contents = f.readlines()
	word_list = []
	f.close()
	num_of_triangle_words = 0
	
	for n in range(len(letters)):
		tn = 0.5*n*(n+1)
		triangle_list.append(tn)
		
	for i in input_contents:
		words = i.replace('"','')
		word_list = words.split(',')
		
	for i in word_list:
		i = i.lower()
		characters = list(i)
		total = 0
		for c in characters:
			total += (letters.index(c) + 1)
		if(total in triangle_list):
			num_of_triangle_words += 1
	return num_of_triangle_words
	
filename = 'p042_words.txt' #Change this variable
print(TriangleNumbers(filename))
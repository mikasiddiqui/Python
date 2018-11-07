def rightAngle():
	count = 0
	number = 0
	for p in range(900,1001):
		numbers = []
		for partition in partitionSum(p,3):
			pythagoras = []
			for r in partition:
				pythagoras.append(r)
			if pythagoras[2]**2 + pythagoras[1]**2 == pythagoras[0]**2:
				numbers.append(pythagoras)
				
		if (len(numbers) > count):
			count = len(numbers)
			number = p
	print(number)
	print(count)

def partitionSum(n, size, limit=None):
    if size == 1:
        yield [n]
        return
    if limit is None:
        limit = n
    start = (n + size - 1) // size
    stop = min(limit, n - size + 1) + 1
    for i in range(start, stop):
        for tail in partitionSum(n - i, size - 1, i):
            yield [i] + tail

rightAngle()
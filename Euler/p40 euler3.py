import math
import time
def BenChapero(digit):
	if digit == 10:
			return 1
	realm = len(str(digit)) - 1
	sum = 0
	for i in range(realm - 1):
		sum += (i + 1)*9*10**i
	if realm == 0:
		return digit
	elif realm == 1:
		result = (digit - 9)/ 2
		modResult = math.floor(result)
		test = result % modResult
		if test != 0:
			final = str(10 + modResult)[0]
		else:
			final = str(10 + modResult - 1)[1]
		return int(final)
	result = (digit - sum) / realm
	modResult = math.floor(result)
	remainder = result % modResult
	if remainder != 0:
		whichDigit = round(remainder*realm) - 1
		final = str(modResult + 10**(realm - 1))[whichDigit]
	else:
		whichDigit = realm - 1
		final = str((modResult - 1) + 10**(realm - 1))[whichDigit]
	return int(final)
def main():
	start_time = time.time()
	#print(BenChapero(1)*BenChapero(10)*BenChapero(100)*BenChapero(1000)*BenChapero(10000)*BenChapero(100000)*BenChapero(1000000))
	print(BenChapero(10000))
	print("Executed In:",(time.time() - start_time), 'seconds.') #STO 1557571
main()

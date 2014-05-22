def numberOnes(num):
	counter = 0
	while num:
		if num & 1:
			counter+=1
		num = num>>1
	return counter

if __name__ == '__main__':
	print numberOnes(11)
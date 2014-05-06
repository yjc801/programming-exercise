def SingleNumber(A):
	one = two = 0
	for i in A:
		one ^= i
		two |= (~one & i)
		three = one & two
		one &= ~three
		two &= ~three
	return one, two

if __name__ == '__main__':
	print SingleNumber([2,2,2,1,3,3,3,1])
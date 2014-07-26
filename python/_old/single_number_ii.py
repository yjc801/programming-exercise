def SingleNumber(A):
	one = two = 0
	for i in A:
		one ^= i
		two |= (~one & i)
		print one,two
		three = one & two
		one &= ~three
		two &= ~three
	# return one, two

if __name__ == '__main__':
	print SingleNumber([1,1,2,2,1,4,4,3])
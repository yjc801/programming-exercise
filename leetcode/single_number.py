def single_number(A):
	res = 0
	for i in xrange(len(A)):
		res = res ^ A[i]
	return res

if __name__ == '__main__':
	A = [1,3,6,1,2,2,3,5,6]
	print single_number(A)
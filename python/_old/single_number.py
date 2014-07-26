def single_number(A):
	res = 0
	for i in A:
		res = res ^ i
	return res

if __name__ == '__main__':
	A = [1,3,6,1,2,2,3,5,6]
	print single_number(A)
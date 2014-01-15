def maxSubArray(A):
	maxm = 0
	for i in xrange(len(A)):
		tot = 0
		for j in A[i+1:]:
			tot += j
			if maxm < tot:
				maxm = tot
	return maxm


if __name__ == '__main__':
	A = [-2,1,-3,4,-1,2,1,-5,4]
	print maxSubArray(A)
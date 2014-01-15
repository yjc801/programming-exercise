import sys

def maxSubArray(A):
	maxm = 0
	for i in xrange(len(A)):
		tot = 0
		for j in A[i+1:]:
			tot += j
			maxm = max(maxm,tot)
	return maxm

def maxSubArray2(A):
	tot = 0
	maxm = -sys.maxint-1
	for i in A:
		tot+=i
		maxm = max(maxm,tot)
		if tot < 0:
			tot = 0
	return maxm

if __name__ == '__main__':
	A = [-2,1,-3,4,-1,2,1,-5,4]
	print maxSubArray2(A)
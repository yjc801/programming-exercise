import sys

# def maxSubArray(A):
# 	maxm = 0
# 	for i in xrange(len(A)):
# 		tot = 0
# 		for j in A[i+1:]:
# 			tot += j
# 			maxm = max(maxm,tot)
# 	return maxm

def maxSubArray(A):
	tot = 0
	maxm = -sys.maxint-1
	for i in A:
		tot+=i
		maxm = max(maxm,tot)
		tot = 0 if tot < 0 else tot
	return maxm

# Divide-Conquer
def maxSubArray2(A):
	return findSubArray(A,0,len(A)-1)
def findSubArray(A,left,right):
	if left > right:
		return -sys.maxint-1
	if left == right:
		return A[left]
	mid = (left+right)>>1
	leftMax = -sys.maxint-1
	rightMax = -sys.maxint-1
	tot = 0
	for i in reversed(A[left:mid]):
		tot += i
		leftMax = max(leftMax,tot)
	for i in A[mid+1:right]:
		tot += i
		rightMax = max(rightMax,tot)
	midMax = A[mid]+leftMax+rightMax
	midMax = max(A[mid],midMax)
	return max(findSubArray(A,left,mid-1),midMax,findSubArray(A,mid+1,right))

if __name__ == '__main__':
	A = [-2,1,-3,4,-1,2,1,-5,4]
	# A = [-1,-2,-3,4]
	print maxSubArray2(A)

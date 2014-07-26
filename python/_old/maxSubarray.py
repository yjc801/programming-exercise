import sys

def maxSub(A):
	n = len(A)
	S = [0]*n
	T = [0]*n
	S[0] = A[0]
	max_elem = A[0]
	for i in xrange(1,n):
		if S[i-1] > 0:
			S[i] = A[i]+S[i-1]
			T[i] = T[i-1]
		else:
			S[i] = A[i]
			T[i] = i
		if S[i] > max_elem:
			max_elem = S[i]

	k = -sys.maxint
	for i in xrange(n-2):
		if S[i] > S[i+1] and S[i+2] > S[i+1] and S[i]+S[i+2]> k:
			index = i
			k = S[i]+S[i+2]

	start1 = T[index]
	start2 = T[index+2]

	max_value = -sys.maxint
	for key, value in enumerate(A):
		if T[key] == T[index]:
			end1 = key
		if T[key] == T[index+2]:
			end2 = key
		if (T[key] != T[index] and T[key] != T[index+2]) and value > max_value:
			max_value = value
	print T
	print S
	print index
	
	if max_value> A[start1] and  max_value > A[end2]:
		return S[end1-1]+S[end2]+max_value
	else:
		return S[end1-1]+S[end2]

if __name__ == '__main__':
	# A = [3,2,-6,3,1]
	# A = [-2,1,-3,4,-1,2,1,-5,4,1]
	# A = [3, 2, -6, 3, 1,1,1,1,1]
	A = [-2, -2, 6, -1, -9, -3, 1, 6]
	print maxSub(A)
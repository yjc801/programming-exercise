def firstMissingPositive(A):
    if not A:
        return 1
    helper(A)
    for i, value in enumerate(A):
        if value != i+1:
            return i+1
    return len(A)+1

def helper(A):
    n = len(A)
    for i in xrange(0,n):
        while A[i] != i+1:
            if A[i] <= 0 or A[i] > n or A[i] == A[A[i]-1]:
                break
            A[A[i]-1], A[i] = A[i], A[A[i]-1]

if __name__ == '__main__':
	A = [5,-1,2,3]
	firstMissingPositive(A)
	print A


	# Catch
	# A = [4,1,2,3]
	# A[0],A[A[0]-1] = A[A[0]-1],A[0]
	# print A
	# A = [4,1,2,3]
	# A[A[0]-1],A[0] = A[0],A[A[0]-1]
	# print A
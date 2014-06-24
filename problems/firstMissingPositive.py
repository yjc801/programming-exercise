def firstMissingPositive(A):
    if not A:
        return 1
    helper(A)
    for i, value in enumerate(A):
        if value != i:
            return i
    return len(A)+1

def helper(A):
    n = len(A)
    for i in xrange(0,n):
        while A[i] != i:
            print A
            if A[i] <= 0 or A[i] > n or A[i]==A[A[i]]:
                break
            A[A[i]], A[i] = A[i], A[A[i]]

if __name__ == '__main__':
	# A = [5,-1,2,3]
    A = [1,1]
    print firstMissingPositive(A)
	# print A


	# Catch
	# A = [4,1,2,3]
	# A[0],A[A[0]-1] = A[A[0]-1],A[0]
	# print A
	# A = [4,1,2,3]
	# A[A[0]-1],A[0] = A[0],A[A[0]-1]
	# print A
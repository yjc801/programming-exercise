def quicksort(A,p,r):
	if (r-p)>0:
		q = partition(A,p,r)
		quicksort(A,p,q-1)
		quicksort(A,q+1,r)

def partition(A,p,r):
	firsthigh = p
	for i in xrange(p,r):
		if A[i] < A[r]:
			A[i],A[firsthigh] = A[firsthigh],A[i]
			firsthigh = firsthigh + 1
	A[r],A[firsthigh] = A[firsthigh],A[r]
	return firsthigh

if __name__ == '__main__':
	A = [4,2,6,1,3,0,5]
	quicksort(A,0,6)
	print A

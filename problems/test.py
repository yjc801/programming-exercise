A = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]

n = len(A)
m = len(A[0])

print A
print m,n



x = -5
counter = 0
x = abs(x)
while x:
    x = x>>1
    counter+=1

print counter

A = [1,2]
n = len(A)
# A[A[0]],A[0] = A[0],A[A[0]]
for i in xrange(n):
    while A[i] != i:
        if A[i] >= n:
            break
        A[A[i]],A[i] = A[i],A[A[i]]
print A
for i in xrange(1,n):
	if A[i]!=i:
		print i
print n
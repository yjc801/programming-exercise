def minMaxPath(a):
	m = len(a)
	n = len(a[0])
	res = a
	for i in xrange(1,m):
		res[i][0] = min(res[i-1][0],a[i][0])
	for j in xrange(1,n):
		res[0][j] = min(res[0][j-1],a[0][j])
	for i in xrange(1,m):
		for j in xrange(1,n):
			res[i][j] = min(max(res[i-1][j],res[i][j-1]),res[i][j])
	
	return res[m-1][n-1]

if __name__ == '__main__':
	a = [[5,2],
		 [3,4],
		 [5,6]]

	print minMaxPath(a)

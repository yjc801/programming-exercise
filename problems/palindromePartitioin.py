def palindrome_partition(s):
	n = len(s)
	max_len = 0
	p = [[False for _ in xrange(n+1)] for _ in xrange(n+1)]
	f = [-1 for _ in xrange(n+1)]
	for i in xrange(n-1,-1,-1):
		f[i] = n-i
		for j in xrange(i,n):
			p[i][j] = s[i] == s[j] and ((j-i<2) or p[i+1][j-1])
			if p[i][j]:
				f[i] = min(f[i],f[j+1]+1)
			# if p[i][j] and (j-i+1)>max_len:
			# 	max_len = j-i+1
			# 	start = i
	print f

	res = [[] for _ in xrange(n)]

	for i in xrange(n-1,-1,-1):
		for j in xrange(i,n):
			if p[i][j]:
				print res
				if j < n-1:
					for k in res[j+1]:
						temp = []
						temp.extend(k)
						temp.insert(0,s[i:j+1])
						res[i].append(temp)
				else:
					res[i].append([s[i:j+1]])
	res[0].reverse()
	return res[0]

if __name__ == '__main__':
	A = "aaba"
	print palindrome_partition(A)
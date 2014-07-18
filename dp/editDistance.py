import timeit

def editDistance(word1,word2):
	n = len(word1)
	m = len(word2)
	f = [[0]*(m+1) for _ in xrange(n+1)]

	for i in xrange(n+1):
		f[i][0] = i
	for j in xrange(m+1):
		f[0][j] = j

	for i in xrange(1,n+1):
		for j in xrange(1,m+1):
			if word1[i-1] == word2[j-1]:
				f[i][j] = f[i-1][j-1]
			else:
				f[i][j] = min(f[i-1][j],f[i][j-1],f[i-1][j-1])+1
	return f[n][m]

def editDistance_rec(word1,word2):
	n, m = len(word1), len(word2)
	prev = range(n+1)
	return helper(0,n,m,word1,word2,prev)

def helper(i, n, m, word1, word2, prev):

	if i == n:
		return prev[-1]

	curr = [prev[0]+1]

	for j in xrange(m+1):
		if word1[i] == word2[j-1]:
			k = prev[j-1]
		else:
			k = min(prev[j-1], curr[j-1], prev[j])+1
		curr += [k]

	return helper(i+1, n, m, word1, word2, curr)
	


if __name__ == '__main__':
	print editDistance('hello','the')
	print editDistance_rec('hello','the')
	print timeit.timeit("editDistance('hello','the')",setup = "from __main__ import editDistance",number = 10000)
	print timeit.timeit("editDistance_rec('hello','the')",setup = "from __main__ import editDistance_rec",number = 10000)
class Solution:
    # @return an integer
	def uniquePaths(self, m, n):
		if (m == 1 and n == 1): return 1
		if (m < 1 or n < 1): return 0
		return self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)
	
	def uniquePaths2(self,m,n):
		res = list()
		for i in xrange(n):
			res.append(1)
		for i in xrange(1,m):
			res[0] = 1
			for j in xrange(1,n):
				res[j] = res[j-1] + res[j]
		return res[n-1]

if __name__ == '__main__':
	s = Solution()
	print s.uniquePaths(3,7)
	print s.uniquePaths2(3,7)
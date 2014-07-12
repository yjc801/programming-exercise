def z_algorithm(s):
	n = len(s)
	r = l = 0
	z = [0]*n
	for i in xrange(1,n):
		if i > r:
			l = r = i
			while r < n and s[r-l] == s[r]:
				r+=1
			z[i] = r-l
			r-=1
		else:
			k = i-l
			if z[k] < r-i+1:
				z[i] = z[k]
			else:
				l = i
				while r < n and s[r-l] == s[r]:
					r+=1
				z[i] = r-l
				r-=1
	return z

def kmp_prep(p):
	i, j, m = 0, -1, len(p)
	b = [-1]
	while i < m:
		while j > -1 and p[i]!=p[j]:
			j = b[j]
		j+=1
		i+=1
		b.append(j)
	return b

def kmp(t,p):
	i, j, n, m = 0, 0, len(t), len(p)
	if m == 0:
		return ""
	b = kmp_prep(p)
	while i < n:
		while j > -1 and t[i]!=p[j]:
			j = b[j]
		i+=1
		j+=1
		if j == m:
			return t[i-j:]
	return None



if __name__ == '__main__':
	T = "mississippi"
	P = "issip"
	# S = P+"&"+T
	s = 'bbaaccaadd'*2
	# s = 'ccaaddbbaa'+'&'+s
	z = z_algorithm(s)
	print z
	print kmp("","")
	# for key, value in enumerate(z):
	# 	if value == len(P):
	# 		print S[key:]

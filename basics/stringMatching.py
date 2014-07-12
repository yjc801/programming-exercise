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


if __name__ == '__main__':
	# T = "mississippi"
	# P = "issip"
	# S = P+"&"+T
	s = 'bbaaccaadd'*2
	# s = 'ccaaddbbaa'+'&'+s
	z = z_algorithm(s)
	print z
	# for key, value in enumerate(z):
	# 	if value == len(P):
	# 		print S[key:]

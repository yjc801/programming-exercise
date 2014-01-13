def sqrt(x):
	if x ==0:
		return 0
	elif x == 1:
		return 1
	l = 1
	r = x
	while r-l>1:
		mid = (l+r)/2
		if mid*mid <= x:
			l = mid
		else:
			r = mid
	return l

if __name__ == '__main__':
	print sqrt(8194)
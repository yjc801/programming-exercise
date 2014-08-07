def multiply(x, y):
	negative = (x < 0) ^ (y < 0)
	a, b, res, i = abs(x), abs(y), 0, 0
	while b:
		res += a << i if abs(y) & (1 << i) else 0
		b >>= 1
		i+=1
	return -res if negative else res

if __name__ == '__main__':
	print multiply(10,-1)
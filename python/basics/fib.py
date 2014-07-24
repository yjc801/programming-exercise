def fib(n):
	x, y = 0,1
	for i in xrange(n):
		x, y = y, x + y
	return x

if __name__ == '__main__':
	print fib(5)
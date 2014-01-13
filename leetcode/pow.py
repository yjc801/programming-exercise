def pow1(x,n):
	if x == 0:
		return 0.0
	if n == 0:
		return 1.0
	elif n > 0:
		x = x*pow(x,n-1)
	else:
		x = 1.0/x*pow(x,n+1)
	return x

def pow2(x,n):
	if n == 0:
		return 1.0
	half = pow(x,n/2)
	if n%2 == 0:
		return half*half
	elif n%2 == 1:
		return half*half*x
	else:
		return half*half/x

if __name__ == '__main__':
	print pow1(1.00001,123456)
	print pow2(1.001,-10)
	print pow2(0,0)
	print pow2(1.00001,123456)
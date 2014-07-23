def windowSize(array,size):
	res = []
	for i in xrange(len(array)-size+1):
		value = 0
		for j in xrange(size):
			value+=array[i+j]		
		res.append(value)
	return res

if __name__ == '__main__':
	a = [1,2,3,4,5]
	print windowSize(a,2)
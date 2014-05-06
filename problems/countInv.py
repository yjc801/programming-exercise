from collections import deque as queue


def CountInversions(A,low,high):
	counter = 0
	if low < high:
		mid = (low+high)/2
		counter += CountInversions(A,low,mid)
		counter += CountInversions(A,mid+1,high)
		counter += merge(A,low,mid,high)
	return counter


def merge(A,low,mid,high):
	counter = 0
	buffer_a = queue()
	buffer_b = queue()

	for key,value in enumerate(A):
		if low<=key<=mid:
			buffer_a.append(A[key])
		if mid<key<=high:
			buffer_b.append(A[key])
	
	i = low
	
	while buffer_a and buffer_b:
		if buffer_a[0] < buffer_b[0]:
			A[i] = buffer_a.popleft();
		else:
			A[i] = buffer_b.popleft();
			counter+=len(buffer_a)
		i+=1
	
	while buffer_a:
		A[i] = buffer_a.popleft()
		i+=1
	
	while buffer_b:
		A[i] = buffer_b.popleft()
		i+=1
	
	return counter


if __name__ == '__main__':
	A = [1,4,3,2,6,5,8,7]
	print CountInversions(A,0,len(A))
	print A
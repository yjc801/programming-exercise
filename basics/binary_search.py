def binary_search(A,key,low,high):
	if low > high: 
		return -1
	middle = (low+high)/2
	# if A[middle] == key:
		# return middle
	if A[middle] > key:
		return binary_search(A,key,low,middle-1)
	else:
		return binary_search(A,key,middle+1,high)

if __name__ == '__main__':
	A = [1,2,3,3,3,3,3,4,6]
	print binary_search(A,3,0,len(A)-1)
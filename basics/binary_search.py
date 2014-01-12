def binary_search(A,key,low,high):
	if low > high: 
		return -1
	middle = (low+high)/2
	if A[middle] == key:
		return middle
	if A[middle] > key:
		return binary_search(A,key,low,middle-1)
	else:
		return binary_search(A,key,middle+1,high)

def find_occurence(A,key):
	length = len(A)
	left = left_boundary(A,key,0,length-1)
	right = right_boundary(A,key,0,length-1)
	return right - left

def left_boundary(A,key,low,high):
	if low > high:
		return low
	middle = (low+high)/2
	if A[middle] < key:
		return left_boundary(A,key,middle+1,high)
	else:
		return left_boundary(A,key,low,middle-1)

def right_boundary(A,key,low,high):
	if low > high:
		return low
	middle = (low+high)/2
	if A[middle] > key:
		return right_boundary(A,key,low,middle-1)
	else:
		return right_boundary(A,key,middle+1,high)

if __name__ == '__main__':
	A = [1,2,3,3,3,3,3,4,6]
	print binary_search(A,4,0,len(A)-1)
	print find_occurence(A,3)
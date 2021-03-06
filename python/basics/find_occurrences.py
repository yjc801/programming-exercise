def find_occurence(A,key):
	length = len(A)
	left = left_boundary(A,key,0,length-1)
	right = right_boundary(A,key,0,length-1)
	return right - left

def left_boundary(A,key,low,high):
	if low > high:
		return low
	middle = (low+high)/2
	if A[middle] >= key:
		return left_boundary(A,key,low,middle-1)
	else:
		return left_boundary(A,key,middle+1,high)

def right_boundary(A,key,low,high):
	if low > high:
		return low
	middle = (low+high)/2
	if A[middle] > key:
		return right_boundary(A,key,low,middle-1)
	else:
		return right_boundary(A,key,middle+1,high)

if __name__ == '__main__':
	# A = [1,2,3,3,3,3,3,4,6]
	A = [2]
	print left_boundary(A,3,0,len(A)-1)
	print right_boundary(A,3,0,len(A)-1)
	# print find_occurence(A,3)

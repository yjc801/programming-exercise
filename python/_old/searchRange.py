def searchRange(A, target):
    n = len(A)
    low, high = 0, n-1
    lower = left_boundary(A,target,low,high)
    upper = right_boundary(A,target,low,high)-1
    
    if lower== n or A[lower]!=target:
        return [-1,-1]
    else:
        return [lower,upper]
        

def left_boundary(A,key,low,high):
	if low > high:
		return low
	middle = (low+high)/2
	if A[middle] >= key:
		return left_boundary(A,key,low,middle-1)
	else:
		return left_boundary(A,key,middle+1,high)

def right_boundary(self,A,key,low,high):
	if low > high:
		return low
	middle = (low+high)/2
	if A[middle] > key:
		return right_boundary(A,key,low,middle-1)
	else:
		return right_boundary(A,key,middle+1,high)

def searchInsert(A, target):
    if not A:
        return 0
    n= len(A)
    low, high = 0,n-1
    while low <= high:
        mid = (low+high)/2
        if A[mid] >= target:
            high = mid - 1
        else:
            low = mid + 1
    return low

if __name__ == '__main__':
	A = [2,3]
	print left_boundary(A,2,0,0)
	print searchInsert(A,2)
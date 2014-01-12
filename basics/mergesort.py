from collections import deque

def mergesort(A,low,high):
	if low < high:
		middle = (high+low)/2
		mergesort(A,low,middle)
		mergesort(A,middle+1,high)
		merge(A,low,middle,high)

def merge(A,low,middle,high):
	buffer1 = deque()
	buffer2 = deque()
	for i,value in enumerate(A):
		if low <= i <= middle:
			buffer1.append(value)
		if middle < i <= high:
			buffer2.append(value)
	i = low
	while buffer1 and buffer2:
		if buffer1[0] < buffer2[0]:
			A[i]=buffer1.popleft()
		else:
			A[i]=buffer2.popleft()
		i=i+1
	while buffer1:
		A[i]=buffer1.popleft()
		i=i+1
	while buffer2:
		A[i]=buffer2.popleft()
		i=i+1

if __name__ == "__main__":
	A = [4,2,1,3,5,6,0]
	mergesort(A,0,len(A)-1)
	print A

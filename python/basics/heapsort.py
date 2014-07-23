def heapsort(A):
	if not A:
		print "A is empty."
	heap = heap_construct(A)
	for i in xrange(0,len(A)):
		A[i] = extract_min(heap)

def extract_min(heap):
	min = heap[0]
	if len(heap)>1:
		heap[0] = heap.pop()
		buble_down(heap,0)
	return min

def buble_down(heap,p):
	min_index = p
	start = heap_child(p)
	for i in xrange(0,2):
		if (start+i) < len(heap):
			if heap[min_index]>heap[start+i]:
				min_index = start+i
	if min_index != p:
		heap[p],heap[min_index] = heap[min_index],heap[p]
		buble_down(heap,min_index)

def heap_construct(A):
	heap = []
	for i,value in enumerate(A):
		heap.append(value)
		buble_up(heap,i)
	return heap

def buble_up(heap,i):
	parent = heap_parent(i)
	if parent == -1:
		return
	if heap[parent] > heap[i]:
		heap[i],heap[parent] = heap[parent],heap[i]
		buble_up(heap,parent)

def heap_parent(i):
	if i == 0:
		return -1
	return i/2

def heap_child(i):
	if i < 0:
		return -1
	return i*2+1

if __name__ == "__main__":
	A = [4,2,1,0,5,6]
	heapsort(A)
	print A

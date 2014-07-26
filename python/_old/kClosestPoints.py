class Point:
	def __init__(self,x = 0,y = 0):
		self.x = x
		self.y = y

class Heap:
 	def __init__(self,A):
 		self.heap = []
 		
 	def buildHeap(self):
 		for i, value in enumerate(A):
 			self.heap.append(value)
 			self.bubleUp(self.heap,i)
 		return self.heap

 	def bubleUp(self,A,i):
 		parent = self.nodeParent(i)
 		if parent == -1: return
 		if A[parent] > A[i]:
 			A[parent],A[i] = A[i],A[parent]
 			self.bubleUp(A,parent)

 	def nodeParent(self,i):
 		if i == 0: return -1
 		return i/2

 	def extractNode(self):
 		node = self.heap[0]
 		if len(self.heap) > 1:
 			self.heap[0] = self.heap.pop()
 			self.bubleDown(self.heap,0)
 		return node

 	def bubleDown(self,heap,i):
 		min_index = i
 		start = self.nodeChild(i)
 		for counter in xrange(0,2):
 			if (start+counter) < len(heap):
	 			if heap[start+counter] < heap[min_index]: 
	 				min_index = start+counter
 		if min_index != i:
			heap[i],heap[min_index] = heap[min_index], heap[i]
	 		self.bubleDown(heap,min_index)

 	def nodeChild(self,i):
 		if i < 0: return -1
 		return 2*i+1



if __name__ == '__main__':
	A = [5,3,4,7,1]
	h = Heap(A)
	h.buildHeap()
	print h.heap
	print h.extractNode()
	print h.heap
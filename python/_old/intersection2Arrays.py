class Solution():
	def __init__(self,arrayA,arrayB):
		self.arrayA = arrayA
		self.arrayB = arrayB
	
	def intersectSorted(self):
		intersections = []
		for value in self.arrayA:
			if self.binarySearch(self.arrayB,value,0,len(self.arrayB)-1):
				intersections.append(value)
		return intersections

	def binarySearch(self,array,key,low,high):
		if low > high: return False
		mid = (low+high)/2
		if array[mid] == key: return True
		if array[mid] > key:
			return self.binarySearch(array,key,low,mid-1)
		else:
			return self.binarySearch(array,key,mid+1,high)

	def intersectUnsorted(self):
		intersections = []
		HashTable = set()
		for value in self.arrayA:
			HashTable.add(value)
		for value in self.arrayB:
			if value in HashTable:
				intersections.append(value)
		return intersections

if __name__ == '__main__':
	arrayA = [4,7,6,1,2,3,8,0,9]
	arrayB = [0,9,2,1,3,5]
	s = Solution(arrayA,arrayB)
	print s.intersectUnsorted()
	s.arrayA = sorted(arrayA)
	s.arrayB = sorted(arrayB)
	print s.intersectSorted()
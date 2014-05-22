import sys
import unittest


def bs(A,low,high,target):
	if low > high:
		return low
	mid = (low + high)/2
	# if target == A[mid]:
		# return mid
	if target <= A[mid]:
		return bs(A,low,mid-1,target)
	else:
		return bs(A,mid+1,high,target)


class Test(unittest.TestCase):
	def test(self):
		seq = [0,0,0,1,1,1,1,2,2,2,2]
		self.assertEqual(bs(seq,0,len(seq)-1,1),3)

if __name__ == '__main__':
	# A = [1.2,2.4,3.6,5.8,9.2]
	# A = [1,2,3,4,5]
	# A = [0,0,0,1,1,1,1,2,2,2,2]
	# print bs(A,0,len(A)-1,1)
	unittest.main()

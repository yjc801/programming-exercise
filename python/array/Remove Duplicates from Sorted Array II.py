class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        index, n = 2, len(A)
        if n < 3:
            return n
        for i in xrange(2, n):
            if A[index-2] != A[i]:
                A[index] = A[i]
                index+=1
        return index

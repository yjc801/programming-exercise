class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        index, n = 0, len(A)
        for i in xrange(1, n):
            if A[i] != A[index]:
                index+=1
                A[index] = A[i]
        return index+1
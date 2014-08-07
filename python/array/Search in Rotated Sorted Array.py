class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        low, high = 0, len(A) - 1
        while low <= high:
            mid = (low + high)/2
            if A[mid] == target:
                return mid
            if A[low] > A[mid]:
                if A[mid] < target <= A[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if A[low] <= target < A[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1
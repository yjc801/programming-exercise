class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        low, high = 0, len(A) - 1
        while low <= high:
            mid = (low+high)/2
            if A[mid] == target:
                return True
            if A[mid] > A[low]:
                if A[low] <= target < A[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif A[mid] < A[low]:
                if A[mid] < target <= A[high]:
                    low = mid + 1
                else:
                    high = mid -1
            else:
                low += 1
        return False
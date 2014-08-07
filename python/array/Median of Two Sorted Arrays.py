class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        
        if  (m + n) & 1:
            return self.helper(A, B, 0, m - 1, 0, n - 1, (m + n) / 2)
        else:
            return 0.5 * (self.helper(A, B, 0, m - 1, 0, n - 1, (m + n) / 2)
                    + self.helper(A, B, 0, m - 1, 0, n - 1, (m + n) / 2 - 1))
    
    def helper(self,A,B,a_start,a_end,b_start,b_end,k):
        a_len = a_end - a_start + 1
        b_len = b_end - b_start + 1
        
        if a_len == 0:
            return B[b_start+k]
        
        if b_len == 0:
            return A[a_start+k]
        
        if k == 0:
            return min(A[a_start],B[b_start])
        
        a_mid = a_len * k / (a_len + b_len) # when m != n
        b_mid = k - a_mid - 1
        
        a_mid += a_start
        b_mid += b_start
        
        if A[a_mid] > B[b_mid]:
            k -= b_mid - b_start + 1
            a_end = a_mid
            b_start = b_mid + 1
        else:
            k -= a_mid - a_start + 1
            b_end = b_mid
            a_start = a_mid + 1
        
        return self.helper(A,B,a_start,a_end,b_start,b_end,k)
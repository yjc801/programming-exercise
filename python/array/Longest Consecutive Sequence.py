class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self,num):
        s = set([])
        for i in num:
            s.add(i)
        res = 0
        for i in num:
            length = 1
            j = i
            while 1:
                j += 1
                if j not in s:
                    break
                s.remove(j)
                length += 1
            j = i
            while 1:
                j -= 1
                if j not in s:
                    break
                s.remove(j)
                length += 1
            res = max(res, length)
        return res
                
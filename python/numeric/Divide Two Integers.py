class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        negative = (dividend < 0) ^ (divisor < 0)
        a, b, res = abs(dividend), abs(divisor), 0
        while a >= b:
            c, i = b, 0
            while a>=c:
                a-=c
                c<<=1
                res+=1<<i
                i+=1
        return -res if negative else res


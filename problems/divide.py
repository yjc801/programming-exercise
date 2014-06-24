def divide(dividend, divisor):
    
    negative = (dividend < 0) ^ (divisor < 0)
    a = abs(dividend)
    b = abs(divisor)
    
    res = 0
    while a >= b:
        c = b
        i = 0
        while a>=c:
            a-=c
            res+=1<<i
            c<<=1
            i+=1
    
    return -res if negative else res

if __name__ == '__main__':
    print divide(5,2)
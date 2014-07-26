def getPermutation(n,k):
    sequence = [x for x in xrange(1,n+1)]
    fac = factorial(n)
    temp = []
    k-=1
    while n:
        fac /= n
        res = k / fac
        k %= fac
        temp.append(str(sequence[res]))
        del sequence[res]
        n-=1
    return ''.join(temp)
        
def factorial(n):
    res = 1
    while n > 0:
        res *= n
        n -= 1
    return res


if __name__ == '__main__':
    # print getPosition(123)
    print getPermutation(2,2)
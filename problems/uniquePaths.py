def uniquePaths(m, n):
    cache = {}
    helper(m,n,cache)
    return cache[(m,n)]

def helper(m,n, cache):
    if (m,n) not in cache:
        if m < 1 or n < 1: 
            cache[(m,n)] = 0
        elif m == 1 and n == 1:
            cache[(m,n)] = 1
        else:
            cache[(m,n)] = helper(m,n-1,cache) + helper(m-1,n,cache)
    return cache[(m,n)]

if __name__ == '__main__':
    print uniquePaths(2,3)
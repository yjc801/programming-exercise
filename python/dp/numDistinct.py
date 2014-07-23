def numDistinct(S, T):
    n = len(S)
    m = len(T)
    f = [[0]*(m+1) for _ in xrange(n+1)]
    
    for i in xrange(n+1):
        f[i][0] = 1
    
    for i in xrange(1,n+1):
        for j in xrange(1,m+1):
            f[i][j] = f[i-1][j]
            if S[i-1] == T[j-1]:
                f[i][j] += f[i-1][j-1]
    print f
    return f[n][m]


if __name__ == '__main__':
    print numDistinct('ABCDE','ACE')
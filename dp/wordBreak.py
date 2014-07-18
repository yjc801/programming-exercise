def wordBreak(s, dict):
    n = len(s)
    f = [False]*n
    for i in xrange(n):
            if s[:i+1] in dict:
                f[i] = True
            else:
                for j in xrange(i):
                    if f[j] and s[j+1:i+1] in dict:
                        f[i] = True
                        break
    return f[n-1]

if __name__ == '__main__':
    print wordBreak('ab',['a','b'])
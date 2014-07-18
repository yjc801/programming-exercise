def numDecodings(s):
    if not s:
        return 0

    pprev, prev, n = 0, 1, len(s)

    for i in xrange(n):
        curr = 0
        if s[i] != '0':
            curr = prev
        if i > 0 and 0 < int(s[i-1:i+1]) <= 26:
            print s[i-1],s[i]
            curr += pprev
        pprev, prev = prev, curr
    return prev


if __name__ == '__main__':
    print numDecodings('01')

def longestPalindrome(s):
    if not s:
        return s
    n = len(s)
    f = [[False]*n]*n
    max_len = 1
    start = 0
    for i in xrange(n):
        f[i][i] = True
        for j in xrange(i):
            f[j][i] = (s[j] == s[i]) and (i-j < 2 or f[j+1][i-1])
            if f[j][i] and max_len < i-j+1:
                max_len = i-j+1
                start = j
    return s[start:start+max_len]

def longestPalindrome2(s):
    if not s:
        return s
    t = transform(s)
    n = len(t)
    p = [1]*n
    center = 0
    right = 0

    for i in xrange(1,n):
        j = 2*center-i
        p[i] = min(p[j],right-i) if right > i else 0
        
        while i+p[i] < n and t[i+p[i]] == t[i-p[i]]:
            p[i]+=1

        if i + p[i] > right:
            center = i
            right = i + p[i]

    max_len = 0
    for key, value in enumerate(p):
        if value > max_len:
            max_len = value
            max_index = key
    start =  (max_index - max_len + 1)/2
    length = max_len-1
    return s[start:start+length]

def transform(s):
    res = ['#']
    for i in s:
        res.append(i)
        res.append('#')
    return ''.join(res)

if __name__ == '__main__':
    print longestPalindrome2('abb')
    print longestPalindrome2('ccd')
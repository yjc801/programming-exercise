def romanToInt(s):
    table = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    res = table[s[-1]]
    for i in xrange(len(s)-2,-1,-1):
        if table[s[i]] < table[s[i+1]]:
            res-=table[s[i]]
        else:
            res+=table[s[i]]
    return res

if __name__ == '__main__':
    s = 'MMMDLXXXVI'
    print romanToInt(s)
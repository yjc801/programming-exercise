def wordBreak(s, dict):
    
    if len(s) < 1:
        return False

    maxLen = 0
    minLen = len(s)
    
    for word in dict:
        minLen = min(len(word), minLen)

    for i in xrange(1,len(s)):
        # for j in xrange(minLen,len(s)+1):
            print s[0:i], s[i:]
            # if s[0:i] in dict and s[i+1:] in dict:
                # return True
    return False

if __name__ == '__main__':
    s = "abcdefg"
    dict = set(["aaaa","aa"])
    print wordBreak(s,dict)
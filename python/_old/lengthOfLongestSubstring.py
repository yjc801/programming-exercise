import string

def lengthOfLongestSubstring(s):
    visted = {i:-1 for i in string.printable}
    start = 0
    max_len = 0
    for i in xrange(len(s)):
        if visted[s[i]] >= start:
            max_len = max(max_len,i-start)
            start = visted[s[i]]+1
        visted[s[i]] = i
    return max(len(s)-start,max_len)


if __name__ == '__main__':
    print lengthOfLongestSubstring("abcabcabc")
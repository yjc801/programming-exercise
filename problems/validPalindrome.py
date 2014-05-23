import re
def isPalindrome(s):
    if s == "":
        return True
    s = ''.join(re.findall("[0-9a-zA-Z]+",s))
    low = 0
    high = len(s) - 1
    
    while low < high:
        if s[low].lower() != s[high].lower():
            return False
        low+=1
        high-=1
    return True

if __name__ == '__main__':
    print isPalindrome("1a2")
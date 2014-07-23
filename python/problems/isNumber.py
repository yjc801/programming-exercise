def isNumber(s):
    s = s.strip()
    if 'e' in s:
        l = s.split('e')
        if len(l) == 2:
            return helper(l[0],True) and helper(l[1],False)
        else:
            return False
    else:
        return helper(s,True)
    
def helper(s,decimal):
    if not s:
        return False
    
    i,n = 0,len(s)
    apeared,sign = False,False

    if s[0] in ('+','-'):
        if n == 1:
            return False
        sign = True
        i+=1

    while i < n:
        if s[i] == '.':
            if n == 1 or (n == 2 and i == 1 and sign) or not decimal or apeared:
                return False
            apeared = True
        else:
            if not s[i].isdigit():
                return False
        i+=1

    return True



if __name__ == '__main__':
    print isNumber('+')
    print isNumber('.')
    print isNumber('..')
    print isNumber('-.')
    print isNumber('3.')
    print isNumber('-1.')
    print isNumber('+.8')
    print isNumber('2e0')
    print isNumber('96 e5')
    print isNumber('7e69e')
    print isNumber('1e.66')
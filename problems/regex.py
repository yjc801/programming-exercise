'''
Regular Expression Matching

'''

def isMatch(s, p):
    s = s+'#'
    p = p+'#'
    return helper(s,p,0,0)


def helper(s,p,m,n):
    if p[n] == '#':
        return s[m] == '#'

    if p[n+1] != '*':
        if p[n] == s[m] or (s[m]!= '#' and p[n] == '.'):
            return helper(s,p,m+1,n+1)
        else:
            return False
    else:
        while p[n] == s[m] or (s[m]!= '#' and p[n] == '.'):
            if helper(s,p,m,n+2):
                return True
            m+=1
        return helper(s,p,m,n+2)

if __name__ == '__main__':
    s = 'a'
    p = 'a.'
    print isMatch(s,p)
    s = 'aaaaaaaaaaaaab'
    p = 'a*a*a*a*a*a*a*a*a*a*c'
    print isMatch(s,p)

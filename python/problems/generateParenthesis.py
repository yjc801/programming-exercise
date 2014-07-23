def generateParenthesis(n):
    l = 0
    r = 0
    s = ""
    res = []
    helper(n,l,r,s,res)
    return res

def helper(n,l,r,s,res):
    if l == n:
        s+=(n-r)*")"
        res.append(s)
        return
    
    helper(n,l+1,r,s+"(",res)
    
    if l > r:
        helper(n,l,r+1,s+")",res)

if __name__ == '__main__':
    print generateParenthesis(3)
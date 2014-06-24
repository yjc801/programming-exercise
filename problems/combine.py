import copy
def combine(n, k):
    digits= range(1,n+1)
    curr = 0
    res = []
    path = []
    # dfs(n,k,1,curr,path,res)
    dfs(digits,k,curr,path,res)
    return res
    
def dfs(digits,k,curr,path,res):
# def dfs(n,k,start,curr,path,res):
    # print path
    if curr == k:
        # print res
        res.append(path)
        return
    for i in digits[curr:]:
    # for i in xrange(start,n+1):
        temp = copy.copy(path)
        temp.append(i)
        # print i
        # dfs(n,k,i+1,curr+1,path,res)
        dfs(digits,k,curr+1,temp,res)

def dfs2(n,k):
    stack= []
    res = []
    stack.append(1)
    curr = 0
    while stack:
        if curr == k:
            # res.append(path)
            curr = 0
        start = stack.pop()
        for i in xrange(start,n):
            stack.append(i)
        curr+=1

if __name__ == '__main__':
    print combine(4,2)
    dfs2(4,2)
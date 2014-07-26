def subsetsWithDup(S):
    S.sort()
    res = []
    helper(S,0,[],res)
    return res
    
    
def helper(S,start,path,res):
    if path not in res:
        res+=[path[:]]

    for i in xrange(start,len(S)):
        path.append(S[i])
        helper(S,i+1,path,res)
        path.pop()

if __name__ == '__main__':
    print subsetsWithDup([1,2,2,0])
def combinationSum2(candidates, target):
    candidates.sort()
    path = []
    res = set()
    helper(candidates,target,0,path,res)
    res = [list(i) for i in res]
    return res

def helper(candidates,target,start,path,res):
    if target == 0:
        res.add(tuple(path))
        return

    for i in xrange(start,len(candidates)):
        value = candidates[i]
        if target - value >= 0:
            temp = path[:]
            temp.append(value)
            helper(candidates,target-value,i+1,temp,res)

if __name__ == '__main__':
    print combinationSum2([1],1)
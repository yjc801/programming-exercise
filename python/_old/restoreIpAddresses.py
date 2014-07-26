import copy

def restoreIpAddresses(s):
    start = 0
    path = []
    res = []
    step = 0
    helper(s,start,step,path,res)
    return res

def helper(s,start,step,path,res):
    if start == len(s) and step == 4:
        res.append('.'.join(path))
        return

    if len(s) - start > 3*(4-step) or len(s) - start< 4 -step:
        return

    for i in xrange(1,4):
        if isValid(s,start,i):
            temp = copy.copy(path)
            temp.append(s[start:start+i])
            helper(s,start+i,step+1,temp,res)

def isValid(s,start,i):
    if start + i > len(s):
        return False
    if (s[start] == '0' and i > 1) or int(s[start:start+i]) > 255:
        return False
    return True


if __name__ == '__main__':
    print restoreIpAddresses('25525511135')
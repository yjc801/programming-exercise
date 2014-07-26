def totalNQueens(n):
    counter = [0]   # function can only change mutable type args passed to the func. list is mutable; integer is immutable
    start = 0
    path = [-1]*n
    helper(n,start,path,counter)
    return counter[0]

def helper(n,start,path,counter):
    if start == n:
        counter[0]+=1
        return
    for col in xrange(n):
        if isValid(n,start,col,path):
            path[start] = col
            helper(n,start+1,path,counter)
            path[start] = -1
            
def isValid(n,start,col,path):
    for i in xrange(start):
        offset = start - i
        if path[i] == col or path[i]+offset == col or path[i]-offset == col:
            return False
    return True

if __name__ == '__main__':
    print totalNQueens(4)
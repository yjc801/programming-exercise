def solveNQueens(n):
    res = []
    path = [-1]*n
    start = 0
    helper(n,start,path,res)
    return res

def helper(n,start,path,res):
    if start == n:
        temp = []
        for i in path:
            string = '.'*i
            string+='Q'
            string+='.'*(n-i-1)
            temp.append(string)
        res.append(temp)
        return
    
    for col in xrange(n):
        if isValid(n,start,col,path):
            path[start] = col
            helper(n,start+1,path,res)
            path[start] = -1

def isValid(n,start,col,path):
    for row in xrange(start):
        offset = start-row
        if path[row] == col or path[row]+offset == col or path[row]-offset == col:
            return False
    return True

if __name__ == '__main__':
    print solveNQueens(1)
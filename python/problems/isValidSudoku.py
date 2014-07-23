def isValidSudoku(board):
    m = len(board)
    n = len(board[0])
    
    for i in xrange(m):
        
        used = {str(i):False for i in xrange(1,10)}

        for j in xrange(n):
            if board[i][j] == '.':
                continue
            elif used[board[i][j]]:
                return False
            used[board[i][j]] = True
            
        used = {str(i):False for i in xrange(1,10)}
        
        for j in xrange(n):
            if board[j][i] == '.':
                continue
            elif used[board[j][i]]:
                return False
            used[board[j][i]] = True

    for k in xrange(3):
        for l in xrange(3):
            used = {str(i):False for i in xrange(1,10)}
            for i in xrange(l*3,(l+1)*3):
                for j in xrange(k*3,(k+1)*3):
                    if board[i][j] == '.':
                        continue
                    elif used[board[i][j]]:
                        return False
                    used[board[i][j]] = True
    return True

if __name__ == '__main__':
    print isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
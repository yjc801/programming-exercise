def solveSudoku(board):
    helper(board)
    # print board
    for i in xrange(len(board)):
        board[i] = ''.join(board[i])

def helper(board):   
    for i in xrange(9):
        board[i] = list(board[i])
        for j in xrange(9):
            if board[i][j] == '.':
                for k in xrange(9):
                    board[i][j] = str(k+1)
                    if isValid(board,i,j) and helper(board):
                        return True
                    board[i][j] = '.'
                return False
    return True

def isValid(board,row,col):
    for i in xrange(9):
        if i!= col and board[row][i] == board[row][col]:
            return False
    for j in xrange(9):
        if j != row and board[j][col] == board[row][col]:
            return False
    
    for i in xrange(row/3*3,row/3*3+3):
        for j in xrange(col/3*3,col/3*3+3):
            if i != row and j != col and board[i][j] == board[row][col]:
                return False
    return True


if __name__ == '__main__':

    A = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    # A = [[5,3,'.','.',7,'.','.','.','.'],
    # [6,'.','.',1,9,5,'.','.','.'],
    # ['.',9,8,'.','.','.','.',6,'.'],
    # [8,'.','.','.',6,'.','.','.',3],
    # [4,'.','.',8,'.',3,'.','.',1],
    # [7,'.','.','.',2,'.','.','.',6],
    # ['.',6,'.','.','.','.',2,8,'.'],
    # ['.','.','.',4,1,9,'.','.',5],
    # ['.','.','.','.',8,'.','.',7,9]]

    solveSudoku(A)
    print A
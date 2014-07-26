def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    cache = {}
    helper(obstacleGrid,m,n,cache)
    return cache[(m,n)]
    
def helper(obstacleGrid,m,n,cache):
    print m,n
    if (m,n) not in cache:
        if m < 1 or n < 1 or obstacleGrid[m-1][n-1]:
            cache[(m,n)] = 0
        elif m == 1 and n == 1:
            cache[(m,n)] = 1
        else:
            cache[(m,n)] = helper(obstacleGrid,m,n-1,cache)+helper(obstacleGrid,m-1,n,cache)
    return cache[(m,n)]

if __name__ == '__main__':
    obstacleGrid = [[0,0]]
    print uniquePathsWithObstacles(obstacleGrid)
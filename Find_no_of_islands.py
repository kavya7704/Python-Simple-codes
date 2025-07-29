def Islands(grid):
    n = len(grid)
    m = len(grid[0])
    count = 0 
    visited = [[0] * m for i in range(n)]

    def dfs(i,j,grid,visited,n,m):
        visited[i][j] = 1
        for row,col in [[-1,0],[1,0],[0,-1],[0,1]]:
            delRow = i + row
            delCol = j + col
            if delRow >= 0 and delRow < n and delCol >= 0 and delCol < m and visited[delRow][delCol] == 0 and grid[delRow][delCol] == "1":
                dfs(delRow,delCol,grid,visited,n,m)

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1" and visited[i][j] == 0:
                dfs(i,j,grid,visited,n,m)
                count += 1
    return count

print(Islands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))

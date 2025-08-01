from collections import deque

def min_days_to_rot_all_oranges(grid, n):
    q = deque()
    fresh = 0
    days = 0

    # Directions: up, down, left, right
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    # Initialize queue with rotten oranges and count fresh ones
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 2:
                q.append((i, j, 0))  # (i, j, day)
            elif grid[i][j] == 1:
                fresh += 1

    max_days = 0
    while q:
        i, j, d = q.popleft()
        max_days = max(max_days, d)

        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                grid[ni][nj] = 2
                fresh -= 1
                q.append((ni, nj, d + 1))

    return max_days if fresh == 0 else -1


# Driver code
T = int(input())
for _ in range(T):
    n = int(input())
    grid = []
    for _ in range(n):
        row = list(map(int, list(input().strip())))
        grid.append(row)
    print(min_days_to_rot_all_oranges(grid, n))

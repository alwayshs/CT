import sys

input = sys.stdin.readline

T = int(input())

while T > 0:
    T -= 1

    m, n = map(int, input().split())

    grid = []
    for _ in range(m):
        grid.append(list(map(int, input().split())))
        
    total_move = 0

    for c in range(n):
        empty_spaces = 0

        for r in range(m - 1, -1, -1):
            if grid[r][c] == 0:
                empty_spaces += 1
            else:
                total_move += empty_spaces
                
    print(total_move)
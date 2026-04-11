import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])

matrix = []
idx = 1
for _ in range(N):
    row = []
    for _ in range(N):
        row.append(int(data[idx]))
        idx += 1
    matrix.append(row)

while N > 1:
    new_matrix = []

    for r in range(0, N, 2):
        new_row = []
        for c in range(0, N, 2):
            elements = [
                matrix[r][c], matrix[r][c+1],
                matrix[r+1][c], matrix[r+1][c+1]
            ]
            
            elements.sort()
            new_row.append(elements[2])
            
        new_matrix.append(new_row)

    matrix = new_matrix
    N //= 2

print(matrix[0][0])
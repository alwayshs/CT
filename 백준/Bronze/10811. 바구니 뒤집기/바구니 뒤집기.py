N, M = map(int, input().split())

list = []
for a in range(1, N + 1):
    list.append(a)

for b in range(0, M):
    i, j = map(int, input().split())
    list[i-1:j] = list[i-1:j][::-1]

print(*list)
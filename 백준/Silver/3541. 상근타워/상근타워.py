N, M = map(int, input().split())

min_floor = float('inf')
    
for _ in range(M):
    u, d = map(int, input().split())
        
    x = (N * d) // (u + d) + 1

    floor = x * u - (N - x) * d

    if floor < min_floor:
        min_floor = floor
            
print(min_floor)
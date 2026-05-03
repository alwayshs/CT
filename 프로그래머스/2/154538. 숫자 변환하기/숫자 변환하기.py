from collections import deque

def solution(x, y, n):
    if x == y: return 0

    q = deque([(x, 0)])
    visited = set([x])
    
    while q:
        curr, dist = q.popleft()

        for next_val in [curr + n, curr * 2, curr * 3]:
            if next_val == y:
                return dist + 1

            if next_val < y and next_val not in visited:
                visited.add(next_val)
                q.append((next_val, dist + 1))
                
    return -1
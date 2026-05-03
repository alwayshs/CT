from collections import deque

def solution(begin, target, words):
    if target not in words: return 0
    
    q = deque([(begin, 0)])
    visited = set()

    while q:
        curr, step = q.popleft()
        if curr == target: return step
        
        for word in words:
            if word not in visited and sum(c1 != c2 for c1, c2 in zip(curr, word)) == 1:
                visited.add(word)
                q.append((word, step + 1))
    return 0
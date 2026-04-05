keyboard = [
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm"
]

pos = {}
for r in range(len(keyboard)):
    for c in range(len(keyboard[r])):
        pos[keyboard[r][c]] = (r, c)
            
T = int(input().strip())
    
for _ in range(T):
    line = input().split()
    if not line: continue
        
    typed_word = line[0]
    L = int(line[1])
        
    results = []
    for _ in range(L):
        target_word = input().strip()
            
        total_dist = 0
        for c1, c2 in zip(typed_word, target_word):
            r1, c1_idx = pos[c1]
            r2, c2_idx = pos[c2]
                
            total_dist += abs(r1 - r2) + abs(c1_idx - c2_idx)
                
        results.append((total_dist, target_word))
            
    results.sort()
        
    for dist, word in results:
        print(f"{word} {dist}")
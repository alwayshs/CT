import math
from collections import defaultdict

n = int(input())
    
calls = defaultdict(int)
    
for _ in range(n):
    time_str, name = input().split()
    h, m = map(int, time_str.split(':'))
        
    calls[name] += h * 60 + m
        
ans = []
for name, total_time in calls.items():
    if total_time <= 100:
        fee = 10
    else:
        fee = 10 + math.ceil((total_time - 100) / 50) * 3
            
    ans.append((name, fee))
        
ans.sort(key=lambda x: (-x[1], x[0]))
    
for name, fee in ans:
    print(f"{name} {fee}")
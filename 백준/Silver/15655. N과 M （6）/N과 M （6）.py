n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

s = []

def dfs(start):
    if len(s) == m:
        print(*s)
        return
    
    for i in range(start, n):
        s.append(nums[i])
        dfs(i + 1)
        s.pop()

dfs(0)
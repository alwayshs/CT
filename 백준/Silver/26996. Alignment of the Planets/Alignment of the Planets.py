import sys

input = sys.stdin.readline
test_case = int(input())
cows = []
cows_set = []

for i in range(test_case):
    x, y = map(int, input().split())
    cows.append({'x' : x, 'y' : y, 'id' : i + 1})

for i in range(test_case):
    base = cows[i]
    gradients = {}
    for j in range(i + 1, test_case):
        target = cows[j]

        dy = target['y'] - base['y']
        dx = target['x'] - base['x']
        
        if dx == 0:
            gradient = float('inf')
        else:
            gradient = dy / dx
                   
        if gradient not in gradients:
            gradients[gradient] = []
        gradients[gradient].append(target['id'])

    for k in gradients:
        others = gradients[k]
        if len(others) >= 2:
            for l in range(len(others)):
                for m in range(l + 1, len(others)):
                    triplet = [base['id'], others[l], others[m]]
                    triplet.sort()
                    cows_set.append(triplet)

cows_set.sort()
    
unique_sets = sorted(list(set(tuple(x) for x in cows_set)))

print(len(unique_sets))
for s in unique_sets:
    print(f"{s[0]} {s[1]} {s[2]}")